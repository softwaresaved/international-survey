#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import csv
import json
import glob
import pandas as pd
import numpy as np


def get_answer_item(path_to_file):
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


def dropping_lime_useless(df):
    """
    Dropping all the columns created by limesurvey and
    not needed for later analysis
    """
    columns_to_drop = ['Response ID', 'Date submitted', 'Start language',
                       'Date started', 'Date last action', 'Referrer URL']
    df = df.drop(columns_to_drop, axis=1)

    # # Drop the columns about the time for each questions if present (from limesurvey)
    # #FIXME See if the regex works or not
    # df = df.loc[:, ~df.columns.str.contains('^Question time|Group time')]
    df = df.loc[:, ~df.columns.str.contains('Question time')]
    df = df.loc[:, ~df.columns.str.contains('Group time')]
    return df


def cleaning_columns_white_space(df):
    """
    Various cleaning white spaces in columns name
    Can extend that function if some other form of errors
    are found later

    :params:
        df dataframe(): the input dataframe

    :return:
        df dataframe(): the same df but with cleaned columns
    """
    # Some columns have a unbreakable space in their name, replace it
    df.columns = df.columns.str.replace('\xa0', ' ')
    # Some columns have a tabular instead of a space
    df.columns = df.columns.str.replace('\t', ' ')
    df = df.rename(columns=lambda x: re.sub('(?<=\s) +|^ +(?=\s)| (?= +[\n\0])', ' ', x))
    # Replace all ending white space
    df.columns = df.columns.str.strip()
    return df


def cleaning_missing_na(df):
    """
    Cleaning all the prefer not say and na answers
    """
    # Replace variation of 'Do not want to answer', Do not wish to declare', 'Prefer not to say' into nan
    # if len(df.loc[:, df.columns.to_series().str.contains('Prefer not to answer').tolist()].columns) > 0:
    df.replace('Prefer not to answer', np.NaN, inplace=True)
    df.replace('Do not wish to declare', np.NaN, inplace=True)
    df.replace('Do not wish to answer', np.NaN, inplace=True)
    return df


def duplicating_other(df):
    """
    When there is an option for 'Other', the column contains the value typed
    by the participants. However, to plot later, it is better to recode all this
    values as 'Yes', as for the other items. Then duplicating these value in another
    column with the tags [Other Raw] for later analysis if we want to analyse it in
    details.
    Creating the tag [Other Raw] at the beginning of the column name to avoid that
    columns being picked up by the grouping_question()

    :params:

    :return:
        :df dataframe(): Return the modified dataframe
    """
    for col in df.columns:
        if col[-7:] == '[Other]':
            # Duplicate the column
            df['[OTHER_RAW] '+ col] = df[col]
            # Replace all the values with 'Yes'
            df[col] = df[col].apply(lambda x: 'Yes' if not pd.isnull(x) else np.nan)
    return df


def grouping_question(df):
    """
    Group question together by merging them when they have a [TAG]
    at the end of their column name.
    They group them in a list of list to be able to parse later.
    The list as the columns name for later operation on the df.
    1. Loop through the columns of the dataframe
    2. Check if the question is similar to the previous one,
    if it is True, it add it to a list until it is False
    3. When it is False, add that list to a larger list that
    contains all the columns split in group lists.

    :params:
        pd.dataframe(): dataframe to parse all columns

    :return:
        list(): a list() of list() of columns name str(). Each list
        contains one group of question.
        If a list only contains one question, this question doesn't belong
        to any group
    """
    def compare_question(current_question, previous_question, current_particule, previous_particule):
        """
        """
        current_q = current_question.replace(current_particule, '')
        previous_q = previous_question.replace(previous_particule, '')
        if current_q == previous_q:
            # if set(df[col].unique()) == set(df[previous_col].unique()):
            return True

    def get_particule(col):
        """
        Do a regex match to get the bracket content and return the
        matched string, or None if not

        :param:
            col str(): the column name to apply the regex on it

        :return:
            last_bit str(): the str between the bracket (w/ the bracket)
            None, if no match is found
        """
        re_match_brac = '\[([^]]+)\]'
        last_bit = re.search(re_match_brac, col)
        if last_bit:
            return last_bit[0]  # If [0], output w/ [], if [1] output w/o []

    def check_similar_q(col, full_list, current_list):
        """
        Check if the colnames passed is similar to the previous
        one.
        First it check if the size of the list is
        It removed the text within brackets and the brackets
        to compare if the two strings are similar.

        :params:
            col str(): column name
            full_list list(): entire list of the all passed grouped questions
            current_list list(): the current list of the previous questions.

        :returns:
            full_list list(): the same full_list appended with the current_list
            if the current question was different than the previous one
            current_list list(): the same current_list, appended with the current
            question if similar to the last element of it or a new one only composed
            of the current question if it was different
        """
        # if len(current_list) > 0:
        current_particule = get_particule(col)
        previous_particule = get_particule(current_list[-1])
        if current_particule and previous_particule:
            if compare_question(col, current_list[-1], current_particule, previous_particule):
                current_list.append(col)
                return full_list, current_list
        full_list.append(current_list)
        current_list = [col]
        return full_list, current_list

    def split_group(group_q):
        """
        Split the list into one list with single element
        and a list with the grouped questions
        :param:
            group_q list(): list of the list
            of question previously grouped or not

        :returns:
            single_q list(): list of single question
            group_q list(): list of group of questions
        """
        single_q = list()
        i = 0
        while i < len(group_q):
            if len(group_q[i]) == 1:
                single_q.append(group_q.pop(i))
            else:
                i+=1
        return single_q, group_q

    grouped_question = list()
    for col in df.columns:
        try:
            grouped_question, current_list = check_similar_q(col, grouped_question, current_list)
        except (NameError, TypeError):  # NameError when it parsed the 1st column
            current_list = [col]

    single_q, group_q = split_group(grouped_question)
    return single_q, group_q


def check_answers(df, questions, answer_item_dict):

    def get_unique_answer(df, questions):
        """
        Create a set of unique answers for
        each of grouped questions
        """
        for group in questions:
            unique_answer = set()
            for q in group:
                unique_answer = set(unique_answer | set(df[q].unique()))
                # unique_answer.add(df[q].unique())
            # Remove the nan element
            try:
                unique_answer.remove(np.nan)
            except KeyError:
                pass
            yield group, unique_answer

    def common_element(set1, set2):
        """
        If the len of common element between the two sets
        are at least 0.5 of the len of the set1
        return True, False otherwise
        """

        # Remove the integer elements from the set because
        # They are common to all likert scales
        if len(set(set1).intersection(set2)) >= len(set1) /2:
            return True
        else:
            return False

    def check_numbers(input_set):
        """
        Check if the strings can be converted in int
        In that case, it means that it is either a discrete
        scale or a likert scale
        """
        def f(x):
            try:
                return float(x)
            except ValueError:
                None

        set_int = set([x for x in input_set if f(x)])
        if len(set_int) == len(input_set):
            return True

    def get_type_data(answer_item_dict, unique_answer):
        if len(unique_answer) <= 1:
            return 'single_item'
        if check_numbers(unique_answer):
            return 'discrete'
        for q in answer_item_dict:
            if common_element(answer_item_dict[q], unique_answer):
                return q
        return 'messy_data'

    type_question = dict()
    for group, unique_answer in get_unique_answer(df, questions):
        type_answer = get_type_data(answer_item_dict, unique_answer)
        type_question.setdefault(type_answer, []).append(group)
    return type_question


def write_config_file(output_location, single_q, group_q):
    """
    """
    dict_to_write = {'single_questions': single_q,
                     'grouped_questions': group_q}
    with open(output_location, 'w') as f:
        json.dump(dict_to_write, f)


def write_df(output_location, df):
    """
    """
    df.to_csv(output_location)

def main():
    """
    """
    import matplotlib
    # from include import plotting
    # When using Ipython within vim
    matplotlib.use('TkAgg')

    # When using within jupyter
    # get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

    import matplotlib.pyplot as plt
    #  When using this script with ipython and vim
    plt.ion()
    plt.show()
    pd.set_option('display.max_rows', 300)
    # Load dataset
    df = pd.read_csv('./dataset/raw_results-survey245554.csv')

    # load the different answers to questions to classify questions based on that
    answer_items_folder = '../../../survey_creation/uk_17/listAnswers'

    # Location for the json file of all questions
    json_location = './to_plot.json'
    cleaned_df_location = './dataset/cleaned_data.csv'

    # Parse list of files that contains all the possible created answers
    answer_item_dict = get_answer_item(answer_items_folder)

    # Number of row == number of participants
    len(df.index)

    # # The last page is the last page the participants reached. To
    # # do a compromise between keeping some and getting rid of the participants that haven't complete
    # # enough answers
    nb_answer = pd.DataFrame(df['Last page'].value_counts()).sort_index(ascending=True)
    nb_answer['cumfreq'] = nb_answer.cumsum()
    nb_answer.plot(kind='bar')

    # SPECIFIC UK
    # Overall, as soon as the participants passed the first page, they reached the last page.
    # In consequence, if a participant passed the first page, (s)he is kept.
    df = df.loc[df['Last page']> 1]

    # This reduce the size of the population to:
    len(df.index)

    # # Replace Yes and No to Boolean when it is possible
    df = dropping_lime_useless(df)
    df = cleaning_columns_white_space(df)
    df = cleaning_missing_na(df)
    df = duplicating_other(df)
    single_q, group_q = grouping_question(df)

    # Split all the groups in appropriated type of questions
    group_q = check_answers(df, group_q, answer_item_dict)
    single_q = check_answers(df, single_q, answer_item_dict)
    single_q

    write_config_file(json_location, group_q, single_q)
    write_df(cleaned_df_location, df)

if __name__ == "__main__":
    main()
