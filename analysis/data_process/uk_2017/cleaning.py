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


from config import CleaningConfig


class CleaningData(CleaningConfig):
    """
    Class to perfom some generic cleaning and recording an anonimized
    dataframe into a csv file at the end. Also record a json file
    that take all the questions headers from limesurvey data and match them
    with the question file to enable automatic process during the plotting
    """
    def __init__(self, df):
        """
        """
        super().__init__()
        self.df = df
        self.answers_item_dict = self.get_answer_item(self.answer_folder)

    def cleaning(self):
        """
        Launch the different steps needed to clean the df
        """
        self.df = self.dropping_lime_useless(self.df)
        self.df = self.cleaning_columns_white_space(self.df)
        self.df = self.cleaning_missing_na(self.df)
        self.df = self.duplicating_other(self.df)
        self.survey_structure = self.get_survey_structure()
        self.structure_by_question = self.grouping_question(self.df, self.survey_structure)
        self.structure_by_section = self.transform_for_notebook(self.survey_structure)

        return self.df

    def compare_question(self):
        """
        Compare the question from the question file
        """
        pass

    def get_survey_structure(self):
        """
        """
        result_dict = dict()
        with open(self.question_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                section = row[0]
                code = row[1]
                question = self.cleaning_some_white_space(row[2])
                answer_format = row[3]
                type_question = row[4]
                file_answer = '{}/{}.csv'.format(self.answer_folder, row[4])
                result_dict[code] = {'section': section,
                                     'original_question': question,
                                     'type_question': type_question,
                                     'answer_format': answer_format,
                                     'file_answer': file_answer}
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
                answer_item_dict[file_key] = [i[0] for i in reader]

        return answer_item_dict

    def dropping_lime_useless(self, df):
        """
        Dropping all the columns created by limesurvey and
        not needed for later analysis
        """
        columns_to_drop = ['id. Response ID', 'submitdate. Date submitted', 'startdate. Date started',
                           'datestamp. Date last action', 'refurl. Referrer URL', 'startlanguage. Start language']
        df = df.drop(columns_to_drop, axis=1)

        # Drop the columns about the time for each questions if present (from limesurvey)
        # FIXME See if the regex works or not
        # df = df.loc[:, ~df.columns.str.contains('^Question time|Group time')]
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
        # Replace variation of 'Do not want to answer', Do not wish to declare', 'Prefer not to say' into nan
        # if len(df.loc[:, df.columns.to_series().str.contains('Prefer not to answer').tolist()].columns) > 0:
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
            # Follow the structure given by
            # limesurvey
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
                input_dict[code].setdefault('survey_q', []).append(col)
            except KeyError:
                code = get_question_code(col, 1)
                try:
                    input_dict[code].setdefault('survey_q', []).append(col)
                except KeyError:  # FIXME Need to record all exception in a separated logfile for further investigation

                    pass
                    # if code == 'OTHER_RAW':
                    #     input_dict['OTHER_RAW'] = dict()
                    #     input_dict['OTHER_RAW'].setdefault('survey_q', [].append(col))
                    # elif code == 'SQ001' or code == 'SQ002':
                    #     input_dict['satisGen'] = dict()
                    #     input_dict['satisGen'].setdefault('survey_q', [].append(col))
                    # else:
                    #     print(code)
                    #     print(col)

        return input_dict

    @staticmethod
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

    def transform_for_notebook(self, input_dict):
        """
        Function to parse the created dictionary 'self.survey_structure' to create
        a version of the dictionary to be parsed by 'action_file.py' in order to create
        the appropriate notebook and split the questions' parsing following the sections split
        and the similarity code to group same type of questions together

        :params: input_dict dict(): contains all the details about the columns name in the limesurvey
        data and the information stored in the csv file in the `self.question_file`.

        :return: the transformed dictionary with the following structure:
            {Section int(): {root_code int(): {q_code int(): {'original_question': str(),
                                                              'type_question': str(),
                                                              'file_answer': str(),
                                                              'answer_format': str(),
                                                              'survey_q': list()}}}}}
        """
        output_dict = dict()
        for q in input_dict:
            try:
                input_dict[q]['survey_q']

                section = input_dict[q]['section']
                question = {q: input_dict[q]}
                root_code = self.get_root_code(q)
                del question[q]['section']
                output_dict.setdefault(section, {}).setdefault(root_code, {}).update(question)
            except KeyError:
                pass

        return OrderedDict(sorted(output_dict.items()))

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

    def write_config_file(self):
        """
        """
        dict_to_write = self.survey_structure
        with open(self.json_to_plot_location, 'w') as f:
            json.dump(dict_to_write, f)

    def write_df(self):
        """
        """
        self.df.to_csv(self.cleaned_df_location)


def main():
    """
    """
    import matplotlib
    # from include import plotting
    # When using Ipython within vim
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    #  When using this script with ipython and vim
    plt.ion()
    plt.show()
    pd.set_option('display.max_rows', 300)

    # Load dataset
    df = pd.read_csv(CleaningConfig.raw_data)

    # # SPECIFIC UK
    # # Overall, as soon as the participants passed the first page, they reached the last page.
    # # In consequence, if a participant passed the first page, (s)he is kept.
    # # # The last page is the last page the participants reached. To
    # # # do a compromise between keeping some and getting rid of the participants that haven't complete
    # # # enough answers
    # nb_answer = pd.DataFrame(df['Last page'].value_counts()).sort_index(ascending=True)
    # nb_answer['cumfreq'] = nb_answer.cumsum()
    # nb_answer.plot(kind='bar')
    # df = df.loc[df['Last page']> 1]

    cleaning_process = CleaningData(df)
    cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()


if __name__ == "__main__":
    main()
