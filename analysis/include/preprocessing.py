#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import json
import glob
import pandas as pd
import numpy as np
from collections import OrderedDict

try:
    from include.config import CleaningConfig
except ModuleNotFoundError:
    from config import CleaningConfig

dict_countries = {'de': "Germany",
                  'nl': "Netherlands",
                  'uk': "United Kingdom of Great Britain and Northern Ireland",
                  'us': "United States of America",
                  'zaf': "South Africa",
                  'nzl': "New Zealand",
                  'can': 'Canada',
                  'aus': "Australia"}
list_bool = ['yes', 'y', 't', 'true', 'Yes', 'YES', 'Y', 'T', 'True', 'TRUE']


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
        self.list_bool = list_bool
        self.dict_countries = dict_countries

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

    def clean_errors(self, df):
        """
        Some error such as typo can be present and discovered during the analysis
        They are specific to the year, so this one is for the 2018 survey
        It correct the errors in the df before any further analysis
        """
        # Typo in the code of one question. It is timeLie and should be timeLike
        df.rename(columns={'likert1[timeLie9zaf]._. [In an average month, how much time would you like to spend on teaching]':
                           'likert1[timeLike9zaf]._. [In an average month, how much time would you like to spend on teaching]'},
                  inplace=True)

        return df

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

        def cleaning_some_white_space(string):
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
            # string = re.sub("""(?<=\s) +|^ +(?=\s)| (?= +[\n\0])""", " ", string)
            # Replace all ending white space
            string = string.rstrip()
            return string

        return df.rename(columns=lambda x: cleaning_some_white_space(x))

    def dropping_lime_useless(self, df):
        """
        Dropping all the columns created by limesurvey and
        not needed for later analysis
        """
        columns_to_drop = ['id._.Response ID', 'startdate._.Date started',
                           'datestamp._.Date last action', 'refurl._.Referrer URL', 'ipaddr._.IP address',
                           'seed._.Seed']
        df = df.drop(columns_to_drop, axis=1)

        # Drop the columns about the time for each questions if present (from limesurvey)
        # FIXME See if the regex works or not
        df = df.loc[:, ~df.columns.str.contains('Question time')]
        df = df.loc[:, ~df.columns.str.contains('Group time')]
        return df

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
        return self.df.loc[self.df['lastpage._.Last page']> self.section_nbr_to_keep_after]

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

    def get_answer(self, year, file_answer):
        """
        """
        outfile = file_answer
        with open(outfile, "r") as f:
            list_answer = [x[:-1] for x in f.readlines()]
            return [x.split(";")[0].strip('"') for x in list_answer]

    def get_survey_structure(self):
        """
        """
        result_dict = dict()
        with open(self.question_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_info= {'section': row['section'],
                           'original_question': row['question'],
                           'type_question': row['answer_file'],
                           'answer_format': row['answer_format'],
                           'country_specific': row['country_specific'],
                           'public': row['public']}
                if row['answer_file'] != '':
                    if row['country_specific'] not in self.list_bool:

                        # try:
                        filename = '{}/{}.csv'.format(self.answer_folder,
                                                      row['answer_file'])
                        all_info['file_answer'] = self.get_answer(self.year, filename)
                else:
                    all_info['file_answer'] = None
                code = row['code']
                if row['country_specific'] in self.list_bool:
                    for country in self.dict_countries:
                        if row[country] in self.list_bool:
                            new_code = '{}q{}'.format(code, country)
                            if row['answer_file'] != '':

                                try:
                                    filename = '{}/countries/{}/{}.csv'.format(self.answer_folder,
                                                                               country,
                                                                               row['answer_file'])
                                    all_info['file_answer'] = self.get_answer(self.year, filename)
                                except FileNotFoundError:  # In case of despite being a country specific, it used the common one
                                    filename = '{}/{}.csv'.format(self.answer_folder,
                                                                  row['answer_file'])
                                    all_info['file_answer'] = self.get_answer(self.year, filename)
                            else:
                                all_info['file_answer'] = None
                            result_dict[new_code] = all_info.copy()

                    if row['world'] in self.list_bool:
                        new_code = '{}q{}'.format(code, 'world')
                        result_dict[new_code] = all_info
                else:
                    result_dict[code] = all_info
        return result_dict

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
            splitted_col.remove('_')  # the new outformat from limesurve is '._.' btw the code
            if element_to_return == 0:
                return splitted_col[0].split('[')[0]
            if element_to_return == 1:
                try:
                    return splitted_col[0].split('[')[1][:-1]  # -1 to remove the last ] in the string

                except IndexError:  # In case not splitting like that just return the other code
                    print('Index_error: {}'.format(splitted_col))
                    return splitted_col[0].split('[')[0]
                    # code = splitted_col[0].split('[')[0]

        def add_question_to_dict(input_dict, code, col):
            """
            Add the questions from the responses to the dictionary
            It can have several questions for several columns (in case of multiple choice, likert, one choice
            It return the dictionary with the list of all questions that are similar

            :params:
                input_dict dict(): The dictionary to update
                code str(): the code extracted from the column to match the key in the input_dict
                col str(): the complete columns string to add

            :return:
                input_dict dict(): the updated dictionary
            """
            try:
                input_dict[code].setdefault('survey_q', []).append(col)
            except KeyError:
                multiple_code = get_question_code(col, 1)
                try:
                    input_dict[multiple_code].setdefault('survey_q', []).append(col)
                except KeyError:  # Sometime the questions is stored as multiple choice in limesurvey but it is two specific question in the csv
                    pass
            return input_dict

        for col in df.columns:
            code = get_question_code(col, 0)
            input_dict = add_question_to_dict(input_dict, code, col)
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
            file_answer = None
            for q in group_question:
                current_answer_format = group_question[q]['answer_format'].lower()
                survey_q = group_question[q]['survey_q']
                original_q = group_question[q]['original_question']
                file_answer = group_question[q]['file_answer']

                if previous_answer_format in ['y/n/na', 'likert'] or current_answer_format in ['y/n/na', 'likert']:
                    if current_answer_format == previous_answer_format or previous_answer_format is None:
                        if previous_answer_format == 'likert' and current_answer_format == 'likert':
                            if previous_file_answer != file_answer:
                                yield group_survey_q, group_original_question, previous_answer_format, previous_file_answer
                                group_survey_q, group_original_question = list(), list()
                        group_survey_q.extend(survey_q)
                        group_original_question.append(original_q)
                    else:
                        yield group_survey_q, group_original_question, previous_answer_format, previous_file_answer
                        group_survey_q, group_original_question = list(), list()
                        group_survey_q.extend(survey_q)
                        group_original_question.append(original_q)
                else:
                    if len(group_survey_q) > 0:
                        yield group_survey_q, group_original_question, previous_answer_format, previous_file_answer
                    group_survey_q, group_original_question = list(), list()
                    group_survey_q.extend(survey_q)
                    group_original_question.append(original_q)

                previous_answer_format = current_answer_format
                previous_file_answer = file_answer

            yield group_survey_q, group_original_question, previous_answer_format, file_answer

        def dictionary_by_section(input_dict):
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

        def grouping_question_for_notebook(input_dict):
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
                        input_dict[section][group].append(q_dict)
            return input_dict

        def ordering_dict(input_dict):
            return OrderedDict(sorted(input_dict.items()))

        dict_by_section = dictionary_by_section(input_dict)
        dict_by_section = grouping_question_for_notebook(dict_by_section)
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

        self.df = self.clean_errors(self.df)
        self.df = self.cleaning_columns_white_space(self.df)
        self.df = self.cleaning_missing_na(self.df)
        self.df = self.duplicating_other(self.df)
        self.survey_structure = self.get_survey_structure()

        self.structure_by_question = self.grouping_question(self.df, self.survey_structure)
        self.structure_by_section = self.transform_for_notebook(self.structure_by_question)
        # self.df = self.revert_inverted_likert(self.likert_item_to_revert)
        return self.df

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
    pass


if __name__ == "__main__":
    main()
