#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import csv
import json
import glob
import pandas as pd
import numpy as np
from collections import OrderedDict
import pycountry


from include.config import CleaningConfig


class CleaningData(CleaningConfig):
    """
    Class to perfom some generic cleaning and recording an anonymized
    dataframe into a csv file at the end. Also record a json file
    that take all the questions headers from limesurvey data and match them
    with the question file to enable automatic process during the plotting
    """
    def __init__(self, year, country, df):
        """
        """
        super().__init__(year, country)
        self.df = df
        self.answers_item_dict = self.get_answer_item(self.answer_folder)
        # Some likert items need to be reverted -- need a list
        self.likert_item_to_revert = ['turnOver2', 'turnOver3']

    def cleaning(self):
        """
        Launch the different steps needed to clean the df
        """
        try:
            self.df = self.dropping_dead_participant(self.df)
        except KeyError:
            pass
        try:
            self.df = self.dropping_lime_useless(self.df)
        except ValueError:
            pass
        self.df = self.cleaning_columns_white_space(self.df)
        self.df = self.cleaning_missing_na(self.df)
        self.df = self.duplicating_other(self.df)
        self.df = self.remove_not_right_country(self.df)
        self.df = self.remove_empty_column(self.df)
        self.survey_structure = self.get_survey_structure()
        self.structure_by_question = self.grouping_question(self.df, self.survey_structure)
        self.structure_by_section = self.transform_for_notebook(self.survey_structure)
        self.df = self.revert_inverted_likert(self.likert_item_to_revert)
        # In the 2016 emails there is a columns with emails that needs to be removed
        if self.year == '2016' and self.country == 'uk':
            self.df = self.remove_email_2016(self.df)
        # In case of the German 2017 survey, they did a mistake with the answer item for the salary and left the pounds for the english
        # text while converted in euros for the translation in German. This function just convert each of the answers into the euros.
        if self.year == '2017' and self.country == 'de':
            self.df = self.clean_salary_de_2017(self.df)
        if self.year == '2017' and self.country == 'us':
            self.df = self.clean_salary_us_2017(self.df)
            self.df = self.clean_highest_education(self.df)
        if self.year == '2017' and self.country == 'can':
            self.df = self.clean_can_edu(self.df)
        self.df, self.structure_by_section = self.create_language_section(self.df, self.structure_by_section)
        return self.df

    def clean_can_edu(self, df):
        """
        In the Canada 2017, the 'other' field was exceptionally too much used.
        This function do some easy cleaning to match some others with pre-existing categories
        """

        col_to_check = {'[OTHER_RAW]. edu2. In which discipline is your highest academic qualification? [Other]': 'edu2. In which discipline is your highest academic qualification?',
                        '[OTHER_RAW]. currentEmp7. In which application area do you primarily work? [Other]': 'currentEmp7. In which application area do you primarily work?'}
        translate_fields = {'Humanities': 'Social sciences and humanities',
                            'History': 'Social sciences and humanities',
                            'Bioinformatique': 'Biomedical engineering',
                            'Bioinformatics': 'Biomedical engineering',
                            'Bioinformatics and Computational Biology': 'Biomedical engineering',
                            'Biochemistry/Bioinformatics': 'Biomedical engineering',
                            'Computational Science': 'Information technology',
                            'Computer Engineering/Science': 'Information technology',
                            'Computer Engineering': 'Information technology',
                            'computer engineering': 'Information technology',
                            'computer': 'Information technology',
                            'Computer Science': 'Information technology',
                            'Computer Engineering/Science': 'Information technology',
                            'Computer Engineering': 'Information technology',
                            'Computer science': 'Information technology',
                            'Computer & information science': 'Information technology',
                            'informatique': 'Information technology'
                            }
        for free_text_col, choice_col in col_to_check.items():
            df.loc[df[choice_col] == 'Other'][free_text_col].value_counts(dropna=False).to_frame().rename(columns={free_text_col: 'Freetext for academic subject'})
            # Mapping the dictionary into the df[choice_col] column if the value in free_text_col is in the the translate_field dictionary
            df.loc[df[free_text_col].isin(translate_fields.keys()), choice_col] = df[free_text_col].map(translate_fields)
        return df

    def clean_highest_education(self, df):
        """
        In the US 2017, the 'other' field was exceptionally too much used.
        This function do some easy cleaning to match some others with pre-existing categories
        """
        # Columns name to be used here
        free_text_col = '[OTHER_RAW]. edu2[other]. In which subject is your highest academic degree/qualification? [Other]'
        choice_col = 'edu2. In which subject is your highest academic degree/qualification?'

        # Dictionary to translate the values
        translate_fields = {'Cognitive Science': 'Psychology',
                            'Statistics': 'Mathematics',
                            'Genetics': 'Biological Sciences',
                            'bioinformatics': 'Biological Sciences',
                            'Biostatistics': 'Biological Sciences',
                            'Physics': 'Physics and Astronomy',
                            'Medical Physics': 'Medicine',
                            'Computer Systems Engineering': 'Computer Science',
                            'Artificial Intelligence and Mathematics': 'Mathematics',
                            'Evolutionary genomics': 'Biological Sciences',
                            'Epidemiology': 'Medicine',
                            'Oceanography': 'Geography & Environmental Sciences',
                            'Computational Science and Engineering': 'Computer Science'}

        df.loc[df[choice_col] == 'Other'][free_text_col].value_counts(dropna=False).to_frame().rename(columns={free_text_col: 'Freetext for academic subject'})

        # Mapping the dictionary into the df[choice_col] column if the value in free_text_col is in the the translate_field dictionary
        df.loc[df[free_text_col].isin(translate_fields.keys()), choice_col] = df[free_text_col].map(translate_fields)
        return df

    def remove_email_2016(self, df):
        """
        Function to drop the column containing email for the 2016 uk version
        """
        mail = "contact16b. Please enter your email address"
        df = df.drop(mail, axis=1)
        return df

    def clean_salary_us_2017(self, df):
        """
        This function is only used for the US data in 2017.
        The salary has the '$' symbol which is not displayed
        properly in HTML and jupyter notebook.
        """
        q_header = 'socio4. Please select the range of your salary'
        df[q_header] = df[q_header].str.replace('$', "\$")
        return df

    def clean_salary_de_2017(self, df):
        """
        This function is only used for the German data in 2017.
        The salary was not translated into euros
        """
        q_header = 'socio4. Please select the range of your salary'
        replace_dict = {'Less than £24.999': 'Less than 27.499 EUR',
                        'Between £25.000 and £29.999': 'Between 27.500 and 32.999 EUR',
                        'Between £30.000 and £34.999': 'Between 33.000 and 38.499 EUR',
                        'Between £35.000 and £39.999': "Between 38.500 and 43.999 EUR",
                        'Between £40.000 and £44.999': 'Between 44.000 and 49.999 EUR',
                        'Between £45.000 and £49.999': 'Between 50.000 and 54.999 EUR',
                        'Between £50.000 and £59.999': 'Between 55.000 and 65.999 EUR',
                        'Between £60.000 and £69.999': 'Between 66.000 and 76.999 EUR',
                        'Between £70.000 and £99.999': 'Between 77.000 and 109.999 EUR',
                        'More than £100.000': 'More than 110.000 EUR'}
        df[q_header] = df[q_header].replace(replace_dict)
        return df

    def create_language_section(self, df, structure_by_section):
        """
        Get the language column and create a new k for it in the structure_by_section
        while creating a file_answer to be able to be plot later in analysis
        """
        path_to_language = os.path.join('../survey_creation', self.year, self.country, 'listAnswers', 'languages.csv')
        try:
            list_of_languages = self.df['startlanguage. Start language'].unique()
            if len(list_of_languages) > 1:
                with open(path_to_language, 'w+') as f:
                    for language in list_of_languages:
                        f.write(language)
                        f.write('\n')
                dict_to_add = {0: {'language': [{'survey_q': ['startlanguage. Start language'],
                                                 'original_question': ['startlanguage. Start language'],
                                                 'answer_format': 'one choice',
                                                 'file_answer': path_to_language,
                                                 'order_question': False}]}}

                structure_by_section.update(dict_to_add)
                structure_by_section.move_to_end(0, last=False)
        except KeyError:
            pass
        return self.df, structure_by_section

    def revert_inverted_likert(self, item_to_revert):
        """
        Some items need to be inverted as the question is a negative form
        :params:
            :item_to_revert list(): of code contained in the column name
        :return:
            : self.df(): with the reverted items
        """
        for item in item_to_revert:
            try:
                type_question = self.structure_by_question[item]['type_question']
                answer = self.answers_item_dict[type_question]
                replacing_value = dict(zip(answer, answer[::-1]))
                col_to_revert = [col for col in self.df.columns if item in col]
                self.df[col_to_revert] = self.df[col_to_revert].replace(replacing_value)
            except KeyError:
                pass

        return self.df

    def remove_empty_column(self, df):
        """
        If a column as no values at all (all nan), the column is removed
        to avoid problem later in the analysis
        """
        return df.dropna(axis=1, how='all')

    def remove_not_right_country(self, df):
        """
        Remove rows that are not the appropriate country
        """
        # Use the package pycountry to get the language from the country code
        if len(self.country) == 2:
            if self.country == 'uk':
                country = pycountry.countries.get(alpha_2='GB'.upper())
            else:
                country = pycountry.countries.get(alpha_2=self.country.upper())
        elif len(self.country) == 3:
            country = pycountry.countries.get(alpha_3=self.country.upper())
        elif len(self.country) == 4:
            country = pycountry.countries.get(alpha_4=self.country.upper())
        else:
            raise
        return df[df['socio1. In which country do you work?'] == country.name]

    def get_survey_structure(self):
        """
        """
        result_dict = dict()
        with open(self.question_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                result_dict[row['code']] = {'section': row['section'],
                                            'original_question': row['question'],
                                            'type_question': row['answer_file'],
                                            'answer_format': row['answer_format'],
                                            'file_answer': '{}/{}.csv'.format(self.answer_folder, row['answer_file']),
                                            'order_question': row['order_question'],
                                            'public': row['public']}

        return result_dict

    def get_answer_item(self, path_to_file):
        """
        Parse all the files contained in the folder and
        create a dictionary with the data contained into the value
        and the filename as key

        :param:
            path_to_file str(): path to the folder
        :return:
            dict(): containing all the data
        """
        answer_item_dict = dict()
        for filename in glob.glob(os.path.join(path_to_file, '*.csv')):
            with open(filename) as f:
                file_key, _ = os.path.splitext(os.path.basename(filename))
                # Set the delimiter as : to avoid taking
                # the comma as delimiter
                reader = csv.reader(f, delimiter=':')
                try:
                    answer_item_dict[file_key] = [i[0] for i in reader]
                except IndexError:
                    answer_item_dict[file_key] = [i for i in reader]

        return answer_item_dict

    def dropping_dead_participant(self, df):
        """
        Use the option set up in config file `section_nbr_to_keep_after` to
        know which section is considered as the prove that the participant
        dropped and did not reply. It uses the label `Last page` to know which last
        page the participant reached
        A good way to see it is to run the following code on the df:
            nb_answer = pd.DataFrame(df['Last page'] \\
                          .value_counts()) \\
                          .sort_index(ascending=True)
            nb_answer['cumfreq'] = nb_answer.cumsum()
            nb_answer.plot(kind='bar')
        """
        return self.df.loc[self.df['lastpage. Last page']> self.section_nbr_to_keep_after]

    def dropping_empty_question(self, df):
        """
        Some question may not have any answer. If the unique value of that question is array([nan])
        the question is dropped
        """
        return self.df.dropna(axis=1, how='all')

    def dropping_lime_useless(self, df):
        """
        Dropping all the columns created by limesurvey and
        not needed for later analysis
        """
        columns_to_drop = ['id. Response ID', 'submitdate. Date submitted', 'startdate. Date started',
                           'datestamp. Date last action', 'refurl. Referrer URL', 'ipaddr. IP address']
        df = df.drop(columns_to_drop, axis=1)

        # Drop the columns about the time for each questions if present (from limesurvey)
        # FIXME See if the regex works or not
        df = df.loc[:, ~df.columns.str.contains('Question time')]
        df = df.loc[:, ~df.columns.str.contains('Group time')]
        return df

    def cleaning_some_white_space(self, string):
        """
        Clean some white space issues encountered in some text
        questions
        """
        # Some columns have a unbreakable space in their name, replace it
        string = string.replace('\xa0', ' ')
        string = string.replace('\u00a0', ' ')
        # Some columns have a tabular instead of a space
        string = string.replace('\t', ' ')
        # Some columns have double space instead of one
        string = string.replace('  ', ' ')
        # FIXME compile the regex into the __init__()
        string = re.sub('(?<=\s) +|^ +(?=\s)| (?= +[\n\0])', ' ', string)
        # Replace all ending white space
        string = string.strip()
        return string

    def cleaning_columns_white_space(self, df):
        """
        Various cleaning white spaces in columns name
        Can extend that function if some other form of errors
        are found later

        :params:
            df dataframe(): the input dataframe

        :return:
            df dataframe(): the same df but with cleaned columns
        """
        return df.rename(columns=lambda x: self.cleaning_some_white_space(x))

    def cleaning_missing_na(self, df):
        """
        Cleaning all the prefer not say and na answers
        """
        df.replace('Prefer not to answer', np.NaN, inplace=True)
        df.replace('Do not wish to declare', np.NaN, inplace=True)
        df.replace('Do not wish to answer', np.NaN, inplace=True)
        df.replace("I don't know", np.NaN, inplace=True)
        df.replace("Don't want to answer", np.NaN, inplace=True)
        return df

    def grouping_question(self, df, input_dict):

        def get_question_code(column_name, element_to_return):
            """
            :params:
                :column_name str(): text of the column name to split
                and extract the text according on the name format
                output by limesurvey
                :element_to_return int(): Which element of the code to output
                if 0, it output the expected code `edu1`, `socio2`, ...
                However in case of multiple questions presented in one grid in limesurvey
                the code is stored on the second element of the format (ie `likerttime1[perfCheck1]`)
                in that case, if it is 1, it return the second element
            """
            # Follow the structure given by limesurvey
            splitted_col = column_name.split('.')
            if element_to_return == 0:
                code = splitted_col[0].split('[')[0]
            if element_to_return == 1:
                try:
                    code = splitted_col[0].split('[')[1][:-1]  # -1 to remove the last ] in the string
                except IndexError:  # In case not splitting like that just return the other code
                    return splitted_col[0].split('[')[0]
            return code

        for col in df.columns:
            code = get_question_code(col, 0)
            try:
                print('Add a question to the code: {}'.format(code))
                print('Add the question: {}'.format(col))
                input_dict[code].setdefault('survey_q', []).append(col)
                print('Now the total of questions is: {}'.format(input_dict[code]['survey_q']))
            except KeyError:
                multiple_code = get_question_code(col, 1)
                try:
                    input_dict[multiple_code].setdefault('survey_q', []).append(col)
                except KeyError:  # Sometime the questions is stored as multiple choice in limesurvey but it is two specific question in the csv
                    special_code = code[:-1] + multiple_code[-1]
                    try:
                        input_dict[special_code].setdefault('survey_q', []).append(col)
                    except KeyError:  # FIXME Need to record all exception in a separated logfile for further investigation
                        print('Not being able to process this columns: {}'.format(col))

        return input_dict

    def transform_for_notebook(self, input_dict):
        """
        Function to parse the created dictionary 'self.survey_structure' to create
        a version of the dictionary to be parsed by 'action_file.py' in order to create
        the appropriate notebook and split the questions' parsing following the sections split
        and the similarity code to group same type of questions together

        :params: input_dict dict(): contains all the details about the columns name in the limesurvey
        data and the information stored in the csv file in the `self.question_file`.

        :return: the transformed dictionary with the following structure:
            {Section int(): {group str(): [{'original_question': list(),
                                            'type_question': list(),
                                            'file_answer': str(),
                                            'answer_format': str(),
                                            'survey_q': list()]
                                            }}}}}
        """
        def get_root_code(string):
            """
            """
            def return_until_digit(string):
                """
                """
                for x in string:
                    if x.isalpha():
                        yield x
                    else:
                        break

            return ''.join([x for x in return_until_digit(string)])

        def grouping_likert_yn(group_question):
            """
            The questions Y-N and the likert questions can be grouped
            together to have one plot for each.
            The likert questions need to be checked on their answer_format
            for not mixing different type of likert scale

            :params: group_question dict(): group of questions

            :return: gen() the original_question list(), type_question str(), file_answer str()
                               answer_format str(), survey_q list()
            """
            group_survey_q, group_original_question = list(), list()
            previous_answer_format = None
            previous_file_answer = None
            previous_order_question = None
            file_answer = None
            for q in group_question:
                current_answer_format = group_question[q]['answer_format'].lower()
                survey_q = group_question[q]['survey_q']
                original_q = group_question[q]['original_question']
                file_answer = group_question[q]['file_answer']
                order_question = group_question[q]['order_question']
                if order_question == 'TRUE':
                    order_question = True
                else:
                    order_question = False

                if previous_answer_format in ['y/n/na', 'likert'] or current_answer_format in ['y/n/na', 'likert']:
                    if current_answer_format == previous_answer_format or previous_answer_format is None:
                        if previous_answer_format == 'likert' and current_answer_format == 'likert':
                            if previous_file_answer != file_answer:
                                yield group_survey_q, group_original_question, previous_answer_format, previous_file_answer, previous_order_question
                                group_survey_q, group_original_question = list(), list()
                        group_survey_q.extend(survey_q)
                        group_original_question.append(original_q)
                    else:
                        yield group_survey_q, group_original_question, previous_answer_format, previous_file_answer, previous_order_question
                        group_survey_q, group_original_question = list(), list()
                        group_survey_q.extend(survey_q)
                        group_original_question.append(original_q)
                else:
                    if len(group_survey_q) > 0:
                        yield group_survey_q, group_original_question, previous_answer_format, previous_file_answer, previous_order_question
                    group_survey_q, group_original_question = list(), list()
                    group_survey_q.extend(survey_q)
                    group_original_question.append(original_q)

                previous_answer_format = current_answer_format
                previous_file_answer = file_answer
                previous_order_question = order_question

            yield group_survey_q, group_original_question, previous_answer_format, file_answer, previous_order_question

        def dictionary_by_section(input_dict):
            # for k in input_dict:
            #     print(k, input_dict[k])
            output_dict = dict()
            for q in input_dict:
                try:
                    input_dict[q]['survey_q']
                    section = input_dict[q]['section']
                    question = {q: input_dict[q]}
                    root_code = get_root_code(q)
                    del question[q]['section']
                    output_dict.setdefault(section, {}).setdefault(root_code, {}).update(question)
                except KeyError:
                    pass
            return output_dict

        def grouping_question(input_dict):
            for section in input_dict:
                for group in input_dict[section]:
                    group_to_parse = input_dict[section][group]
                    input_dict[section][group] = list()
                    for q in grouping_likert_yn(group_to_parse):
                        q_dict = dict()
                        q_dict['survey_q'] = q[0]
                        q_dict['original_question'] = q[1]
                        q_dict['answer_format'] = q[2]
                        q_dict['file_answer'] = q[3]
                        q_dict['order_question'] = q[4]
                        input_dict[section][group].append(q_dict)
            return input_dict

        def ordering_dict(input_dict):
            return OrderedDict(sorted(input_dict.items()))

        dict_by_section = dictionary_by_section(input_dict)
        dict_by_section = grouping_question(dict_by_section)
        return ordering_dict(dict_by_section)

    def duplicating_other(self, df):
        """
        When there is an option for 'Other', the column contains the value typed
        by the participants. However, to plot later, it is better to recode all this
        values as for the other items, then duplicating these values in another
        column with the tags [Other Raw] to keep the information for later.
        There are two cases when [OTHER] columns have been created.
            1. In case of a multiple choice question (several answer can be selected)
                - The value needs to be recoded into 'Yes' and the column kept
            2. In case of a drop down type of question (only one answer can be selected)
                - The column can be just renamed into [Other Raw] for later analysis, the
                value 'Other' being already encoded in the principal column question
        Creating the tag [Other Raw] at the beginning of the column name to avoid that
        columns being picked up by the grouping_question()

        :params:
            :df dataframe(): Dataframe containing the data
        :return:
            :df dataframe(): Return the modified dataframe
        """
        for col in df.columns:
            if col[-7:] == '[Other]':
                # Duplicate the column
                df['[OTHER_RAW]. '+ col] = df[col]
                # Replace all the values with 'Yes'
                df[col] = df[col].apply(lambda x: 'Yes' if not pd.isnull(x) else np.nan)
                # Droping the column
                df = df.drop(col, axis=1)
        return df

    def remove_private_data(self):
        """
        Check if any N in the Public column in the questions.csv.
        If it is the case, remove the data corresponding to the question for the
        uploaded dataset
        """
        self.public_df = self.df.copy()
        for entry in self.survey_structure:
            public_choice = self.survey_structure[entry]['public'].lower()
            if public_choice == 'false' or public_choice == 'n' or public_choice == 'no' or public_choice == 'f':
                try:
                    col_to_remove = self.survey_structure[entry]['survey_q'][0]
                    self.public_df.drop(col_to_remove, axis=1, inplace=True)
                except KeyError:
                    print('Not finding survey_q in: {}'.format(self.survey_structure[entry]))
        # Delete all the columns created from the 'other field' to be sure none of these are uploaded
        for col in self.public_df.columns:
            if '[OTHER_RAW]' in col:
                self.public_df.drop(col, axis=1, inplace=True)

        # Finally remove all the columns that are not in the questions.csv to be sure it remove any additional data
        # from limesurvey
        code_to_keep = [x for x in self.survey_structure.keys()]
        for col in self.public_df.columns:
            print(col)
            remove = True
            for x in code_to_keep:
                if x in col:
                    remove = False
            if remove is True:
                try:
                    self.public_df.drop(col, axis=1, inplace=True)
                except ValueError:
                    pass

        self._write_df(self.public_df, self.public_df_location)

    def write_config_file(self):
        """
        """
        dict_to_write = self.structure_by_section
        with open(self.json_to_plot_location, 'w') as f:
            json.dump(dict_to_write, f)

    def write_df(self):
        """
        """
        self._write_df(self.df, self.cleaned_df_location)

    def _write_df(self, df, location):
        """
        """
        df.to_csv(location)


def main():
    """
    """
    df = pd.read_csv(CleaningConfig.raw_data)
    cleaning_process = CleaningData(df)
    cleaning_process.cleaning()
    # cleaning_process.write_df(self.df, self.cleaned_df_location)
    cleaning_process.remove_private_data()
    # cleaning_process.write_config_file()


if __name__ == "__main__":
    main()
