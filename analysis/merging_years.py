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


class MergingYear(CleaningConfig):
    """
    Renaming the current year df and merging it with the previous year (works for 2017 and 2018).
    It take the dataframe of 2018, search for common questions with 2017 based on the code and the
    answer format. If they are equal, it renames the columns in both 2017 and 2018 with the 2018 versions. It is needed for merging the dataframe from 2017 into the 2018.
    It also rename the survey_q in the to_plot.json file that is used for helping the analysis bit.
    """
    def __init__(self, year, country=None):
        """
        """
        super().__init__(year, country)
        self.list_bool = list_bool
        self.dict_countries = dict_countries
        self.folder_2017 = './2017/'
        self.folder_2018 = './2018/'
        self.df_countries_clean_2017, self.df_countries_public_2017 = self.get_countries_set(year=2017)
        self.df_countries_clean_2018, self.df_countries_public_2018 = self.get_countries_set(year=2018)
        self.structure_2018 = self.get_2018_survey_structure()
        self.structure_2017 = self.get_2017_survey_structure()

    def get_countries_set(self, year):
        """
        Get the different dataset from all the countries in 2017
        It parse the different folders and return two dictionaries,
        one containing the clean_data and the other containing the public_data

        return:
            df_list list(): contain dict() of all the different countries set. There is a dictionary
            for the clean data and the public data
        """
        # loading 2017 answers

        df_list = list()
        for type_data in ['cleaned_data', 'public_data']:
            if year == 2017:
                df = dict()
                df['Germany'] = pd.read_csv('{}de/data/{}.csv'.format(self.folder_2017, type_data))
                df['Netherlands'] = pd.read_csv('{}nl/data/{}.csv'.format(self.folder_2017, type_data))
                df['South Africa'] = pd.read_csv('{}zaf/data/{}.csv'.format(self.folder_2017, type_data))
                df['United Kingdom'] = pd.read_csv('{}uk/data/{}.csv'.format(self.folder_2017, type_data))
                df['United States'] = pd.read_csv('{}us/data/{}.csv'.format(self.folder_2017, type_data))

            if year == 2018:
                df = pd.read_csv('{}/data/{}.csv'.format(self.folder_2018, type_data))
            df_list.append(df)
        return df_list

    def _get_common_columns(self, df):
        """
        """
        list_columns = list()
        for data in df:
            # add a column with the country of origin
            list_columns.append(set(df[data].columns))
            # finding common columns
            set_intersection = set()
            previous_set = None
            for columns in list_columns:
                current_set = columns
                if previous_set is None:
                    previous_set = columns
                if previous_set and (len(set_intersection) == 0):
                    set_intersection = current_set.intersection(previous_set)
                if len(set_intersection) != 0:
                    set_intersection = set_intersection.intersection(current_set)
        return set_intersection

    def get_question_element(self, column_name, year):
        """
        :params:
            :column_name str(): text of the column name to split
            and extract the text according on the name format
            output by limesurvey
        """
        # Follow the structure given by limesurvey
        if year == 2017:
            splitted_col = column_name.split('. ')
        if year == 2018:

            splitted_col = column_name.split('._.')
        code_ = splitted_col[0]
        code = code_.split('[')[0]


        if code[:6] == 'likert':
            code = code_.split('[')[1][:-1]

        common_code = code
        for spec_code in ['quk', 'qcan', 'qus', 'qnl', 'qnzl', 'qaus', 'qde', 'qzaf', 'qworld']:
            common_code = common_code.replace(spec_code, '')

        code = common_code
        if len(splitted_col) == 1:
            return None, splitted_col[0], None

        else:
            question_text = ''.join(splitted_col[-1:])
            if len(question_text.split('[')) == 1:
                return code, question_text, None
            else:
                q_text = question_text.split('[')
                question_text = q_text[0]
                try:
                    if q_text[1].rstrip() != ']':
                        value = '[{}'.format(q_text[1])
                    else:
                        value = None
                except IndexError:
                    raise
                return code, question_text, value

    def rename_df(self, dict_df, year):

        if year == 2017:
            final_df = None
            for country in dict_df:
                list_question = list()
                df = dict_df[country]
                for i in df.columns:
                    code, question_text, value = self.get_question_element(i, year=2017)
                    if code:
                        try:
                            format_2017 = self.structure_2017[code]['answer_format']
                            format_2018 = self.structure_2018[code]['answer_format']
                            if format_2017.rstrip().lower() == format_2018.rstrip().lower():
                                question_text = self.structure_2018[code]['original_question']
                            else:
                                question_text = self.structure_2017[code]['original_question'] + '_2017'
                            if value:
                                final_question = '. '.join([code, question_text, value])
                            else:
                                final_question = '. '.join([code, question_text])

                            final_question = final_question.replace('..', '.')
                            final_question = final_question.replace('. . ', '. ')
                            list_question.append(final_question)
                            df.rename(columns={i: final_question}, inplace=True)
                        except KeyError:
                            pass
                df = df[list_question]

                # Add column for year and Country
                df['Country'] = country
                df['Year'] = '2017'
                try:
                    final_df = final_df.merge(df, how='outer')
                except AttributeError:  # final_df is init as None
                    final_df = df

            return final_df

        if year == 2018:
            dict_of_q_to_merge = dict()
            for i in dict_df.columns:
                code, question_text, value = self.get_question_element(i, year=2018)
                if code:
                    if value:
                        final_question = '. '.join([code, question_text, value])
                    else:
                        final_question = '. '.join([code, question_text])


                else:
                    final_question = i

                final_question = final_question.replace('. . ', '. ')
                final_question = final_question.replace('.  . ', '. ').replace(' . ', '. ')
                # try:
                #     list_q = dict_of_q_to_merge[final_question]
                #     list_q.append(i)
                #     dict_of_q_to_merge[final_question] = list_q
                # except KeyError:
                #     dict_of_q_to_merge[final_question] = [i]
                dict_of_q_to_merge.setdefault(final_question, []).append(i)

            for q in dict_of_q_to_merge:
                dict_df.rename(index=str, columns={dict_of_q_to_merge[q][0]: q}, inplace=True)
                # for original_q in dict_of_q_to_merge[q]:
                    # dict_df.rename(index=str, columns={original_q: q}, inplace=True)
                if len(dict_of_q_to_merge[q]) >1:
                    for col in dict_of_q_to_merge[q][1:]:
                        # print('Type of original column: {}'.format(dict_df[q].dtype))
                        # print('Type of new columns: {}'.format(dict_df[col].dtype))
                        # dict_df[q] = dict_df[q] + dict_df[col]
                        dict_df[q] = dict_df[q].fillna(dict_df[col])
                        dict_df.drop(col, axis=1, inplace=True)
                # print('number of columns = {}'.format(len(dict_df.columns)))
            dict_df['Year'] = '2018'
            return dict_df

    def merge_2017(self):
        """
        """
        self.df_countries_clean_2017 = self.rename_df(self.df_countries_clean_2017, year=2017)
        self.df_countries_public_2017 = self.rename_df(self.df_countries_public_2017, year=2017)

    def merge_2018(self):
        """
        """
        self.df_countries_clean_2018 = self.rename_df(self.df_countries_clean_2018, year=2018)
        self.df_countries_public_2018 = self.rename_df(self.df_countries_public_2018, year=2018)

    def _merge_both_years(self, df_2017, df_2018):
        """
        """
        # df_2017 = df_2017.astype(str)
        # df_2018 = df_2018.astype(str)
        # n = 0
        # o = 0
        # for col in df_2017.columns:
        #     n +=1
        #     if col in df_2018.columns:
        #         print(col)
        #         o +=1
        # print(n)
        # print(o)
        return df_2018.merge(df_2017, how='outer')
        # return pd.concat([df_2018, df_2017], ignore_index=True)
        # return df_2018.append(df_2017, ignore_index=True)

    def merge_both_years(self):
        """
        """
        print('Merging clean one')
        self.df_all_clean = self._merge_both_years(self.df_countries_clean_2017, self.df_countries_clean_2018)
        print('Merging public one')
        self.df_all_public = self._merge_both_years(self.df_countries_public_2017, self.df_countries_public_2018)

    def get_2018_survey_structure(self):
        """
        """
        result_dict = dict()
        structure_2018 = './../survey_creation/2018/questions.csv'
        with open(structure_2018, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_info= {'section': row['section'],
                           'original_question': row['question'],
                           'type_question': row['answer_file'],
                           'answer_format': row['answer_format'],
                           'country_specific': row['country_specific'],
                           'public': row['public']}
                code = row['code']
                result_dict[code] = all_info
        return result_dict

    def get_2017_survey_structure(self):
        """
        """
        structure_2017 = './../survey_creation/2017/summary_questions.csv'
        result_dict = dict()
        with open(structure_2017, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_info= {'original_question': row['question'],
                           'type_question': row['answer_file'],
                           'answer_format': row['answer_format']}
                code = row['code']
                result_dict[code] = all_info
        return result_dict

    def get_to_plot_2018(self):
        """
        """
        filename = '{}data/to_plot.json'.format(self.folder_2018)

        with open(filename) as f:
            self.to_plot_json = json.load(f)

    def write_config_file(self):
        """
        """
        dict_to_write = self.structure_by_section
        with open(self.json_to_plot_location, 'w') as f:
            json.dump(dict_to_write, f)

    def write_df(self):
        """
        """
        self._write_df(self.df_all_clean, self.clean_merged_location)
        self._write_df(self.df_all_public, self.public_merged_location)

    def _write_df(self, df, location):
        """
        """
        df.to_csv(location)

def main():
    """
    """
    merging_year = MergingYear('2018')
    merging_year.merge_2017()
    merging_year.merge_2018()
    merging_year.get_to_plot_2018()
    print('Merging both years')
    merging_year.merge_both_years()
    merging_year.write_df()
    # for col in merging_year.df_all_clean:
        # print(col)


if __name__ == "__main__":
    main()
