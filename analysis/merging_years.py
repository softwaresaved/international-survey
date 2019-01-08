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
                df['United States'] = pd.read_csv('{}us/data/{}.csv'.format(self.folder_2017, type_data))
                df['Germany'] = pd.read_csv('{}de/data/{}.csv'.format(self.folder_2017, type_data))
                df['Netherlands'] = pd.read_csv('{}nl/data/{}.csv'.format(self.folder_2017, type_data))
                df['South Africa'] = pd.read_csv('{}zaf/data/{}.csv'.format(self.folder_2017, type_data))
                df['United Kingdom'] = pd.read_csv('{}uk/data/{}.csv'.format(self.folder_2017, type_data))

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

    def get_question_element(self, column_name, year, country=None):
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
        if code[:8] == 'time1can':
            code = code_.split('[')[1][:-1]

        common_code = code
        for spec_code in ['quk', 'qcan', 'qus', 'qnl', 'qnzl', 'qaus', 'qde', 'qzaf', 'qworld']:
            common_code = common_code.replace(spec_code, '')

        code = common_code
        if len(splitted_col) == 1:
            return None, splitted_col[0], None

        else:
            question_text = ''.join(splitted_col[1:])
            if len(question_text.split('[')) == 1:
                return code, question_text, None
            else:
                q_text = question_text.split('[')
                question_text = q_text[0]
                try:
                    if question_text.rstrip() == '':
                        # In Uk only have the problem with skill2 questions
                        if country == 'United Kingdom':
                            question_text = splitted_col[1]
                            value = splitted_col[2]
                        else:
                            question_text = q_text[1].replace(']', '')
                            value = None
                    elif q_text[1].rstrip() != ']':
                        question_text = q_text[0]
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
                    code, question_text, value = self.get_question_element(i, year=2017, country=country)
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
                            final_question = final_question.replace('.  . ', '. ').replace(' . ', '. ')
                            final_question = final_question.rstrip()
                            list_question.append(final_question)
                            df.rename(columns={i: final_question}, inplace=True)

                        except KeyError:
                            pass
                df = df[list_question]

                # Add column for year and Country
                df['Country'] = country
                df['Year'] = 2017
                print('Merging: {}'.format(country))
                if final_df is None:
                    final_df = df
                else:
                    final_df = final_df.merge(df, how='outer')
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
                final_question = final_question.rstrip()
                dict_of_q_to_merge.setdefault(final_question, []).append(i)

            for q in dict_of_q_to_merge:
                dict_df.rename(index=str, columns={dict_of_q_to_merge[q][0]: q}, inplace=True)
                if len(dict_of_q_to_merge[q]) >1:
                    for col in dict_of_q_to_merge[q][1:]:
                        dict_df[q] = dict_df[q].fillna(dict_df[col])
                        dict_df.drop(col, axis=1, inplace=True)
            dict_df['Year'] = '2018'
            return dict_df

    def merge_2017(self):
        """
        """
        print('Merging 2017 -- Clean')
        self.df_countries_clean_2017 = self.rename_df(self.df_countries_clean_2017, year=2017)
        print('Merging 2017 -- Public')
        self.df_countries_public_2017 = self.rename_df(self.df_countries_public_2017, year=2017)

    def merge_2018(self):
        """
        """
        self.df_countries_clean_2018 = self.rename_df(self.df_countries_clean_2018, year=2018)
        self.df_countries_public_2018 = self.rename_df(self.df_countries_public_2018, year=2018)

    def _merge_both_years(self, df_2017, df_2018):
        """
        """
        return df_2018.merge(df_2017, how='outer')

    def merge_both_years(self):
        """
        """
        print('Merging clean one')
        self.df_all_clean = self._merge_both_years(self.df_countries_clean_2017, self.df_countries_clean_2018)
        print('Checking after merging')
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

    def _fix_remaining_issues(self, df_2017, df_2018):
        """
        Some columns still have issues with formating as they are different
        between countries
        Here, fix it manually
        """
        # Fixing time*can
        time_fix = {'time1can': 'time1can. On average, how much of your time is spent developing software?',
                    'time2can': 'time2can. On average, how much of your time is spent on research',
                    'time3can': 'time3can. On average, how much of your time is spent on management',
                    'time4can': 'time4can. On average, how much of your time is spent on teaching',
                    'time5can': 'time5can. On average, how much of your time is spent on other activities'}

        # Fixing salary for salary in US 2017
        salary = 'socio4. Please select the range of your salary'


        ## Fixing bus factor


        for year, df in [('2017', df_2017), ('2018', df_2018)]:
            print(year)
            # Fixing a typo on one timeLike10zaf. with a capital K instead of a lower one
            df.rename(index=str, columns={"timeLiKe10zaf. In an average month, how much time would you like to spend on other activities":
                                        "timeLike10zaf. In an average month, how much time would you like to spend on other activities"},
                    inplace=True)

            for col in df:
                # different columns for the same question time*can in 2017
                if col[:8] in time_fix.keys():
                    ref_q = time_fix[col[:8]]
                    if col != ref_q:
                        df[ref_q] = df[ref_q].fillna(df[col])
                        df.drop(col, axis=1, inplace=True)

                # Fixing the salary for the symbol $ in USA
                elif col == salary:
                    df[col] = df[col].str.replace('\\\\', '')
                    df[col] = df[col].str.replace('$', '\\$')

    def fix_remaining_issues(self):
        print('Merging clean one')
        self._fix_remaining_issues(self.df_countries_clean_2017, self.df_countries_clean_2018)
        print('Merging public one')
        self._fix_remaining_issues(self.df_countries_public_2017, self.df_countries_public_2018)


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
    merging_year = MergingYear(year='2018')
    merging_year.merge_2017()
    merging_year.merge_2018()
    merging_year.get_to_plot_2018()
    print('Merging both years')
    merging_year.fix_remaining_issues()
    merging_year.merge_both_years()
    merging_year.write_df()


if __name__ == "__main__":
    main()
