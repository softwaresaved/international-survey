#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import errno
import pandas as pd
import numpy as np

from include.likertScalePlot import compute_percentage
from include.textCleaning import wordcloud

from include.transforming_title import corresponding_title

import itertools as it


def get_answer(file_answer):
    """
    """
    with open(file_answer, 'r') as f:
        return [x.split(';')[0].rstrip() for x in f.readlines()]


def reorder_nan(df, nan_reorder):
    """
    Decide if the NA is pushed at the end of the
    reorder or order with the number of count. The default is
    to put the np.NaN at the end.
    :params:
        :df pd.dataFrame():
        :nan_reorder:
            None: Nothing is done
            end: put the np.Nan at the end
            count: order the np.Nan according to the count
        :list_order list(): list of order that is required if option
            file_order is chosen

    :return:
        df pd.dataFrame(): The sorted df
    """
    if nan_reorder == 'end':
        # Sorting with nan at the end, the in-built function is not working do not know why
        df.sort_values(by=df.columns[0], axis=0, ascending=False, inplace=True, na_position='last')
        # So implemented this dirty hack. If someone wants to fix, please do
        index_wo_nan = list()
        nan_value = False
        for x in df.index:
            if pd.isnull(x):
                nan_value = True
            else:
                index_wo_nan.append(x)
        if nan_value:
            index_wo_nan.append(np.nan)

        df = df.reindex(index=index_wo_nan)
    elif nan_reorder == 'count':
        raise NotImplementedError

    return df


def apply_rename_columns(df, by):
    """
    Sometime the question itself is the third part of the column
    names. IN that case, to extract the appropriate text it need
    to be splitted based on the [
    """
    # Some satisGen are not working with the rest of the scripts as they have different
    # title
    # For the script to match these questions with the csv file that
    # helps to the construction, it should have been reformated
    # This function just replace the text within the bracket to match the ideal case
    #
    # US VERSION Not working
    # likert3[satisgen1]. [In general, how satisfied are you with [Your current position]]
    # likert3[satisgen2]. [In general, how satisfied are you with [Your career]]
    if 'likert3[satisgen2]. [In general, how satisfied are you with [Your career]]' in df.columns:

        dict_to_match = {'likert3[satisgen1]. [In general, how satisfied are you with [Your current position]]':
                         'satisGen1[SQ001]. In general, how satisfied are you with: [Your current position]',
                         'likert3[satisgen2]. [In general, how satisfied are you with [Your career]]':
                         'satisGen1[SQ002]. In general, how satisfied are you with: [Your career]'}
        df = df.rename(columns=dict_to_match)

    try:
        if by == 'index':
            df = df.rename(index=lambda x: x.split('[')[2][:-1])
        if by == 'columns':
            df = df.rename(columns=lambda x: x.split('[')[2][:-1])
    # In case of the columns or index are not following the rules above
    # try to remove the code only (the case for y-n-na when they are multiple)
    except IndexError:
        if by == 'index':
            df = df.rename(index=lambda x: x.split('.')[1])
        if by == 'columns':
            df = df.rename(columns=lambda x: x.split('.')[1])
    return df


def remove_code_from_string(inputlist):
    """
    Receive a list and return a list without the code
    added to the question
    """
    return [s.split('. ')[1:][0] for s in inputlist]


def remove_code_from_column(df, colnames):
    """
    Function to remove the code from the columns.
    Limesurvey adds the code at the beginning of the string.
    following this patternd "code1. STRING"
    Get the dataframe and remove the code to all the columns then
    return the same dataframe.
    It also returns a transformed list of colnames as it is needed for
    later operation
    :params:
        :df DataFrame(): Input dataframe
        :colnames list(): all the columns to be modified
    :return:
        :df DataFrame(): The same df with the rename columns
        :new_col list(): the colnames w/o the code
    """
    new_col = remove_code_from_string(colnames)
    df.rename(columns=dict(zip(colnames, new_col)), inplace=True)
    return df, new_col


def extract_common_substring(string1, string2):
    """
    To get the common substring between two strings
    solution found: https://stackoverflow.com/a/18716089
    """
    return ''.join(el[0] for el in it.takewhile(lambda t: t[0] == t[1], zip(string1, string2)))


def extract_unique_substring(string1, string2, common_string):
    """
    return both of unique element
    """
    return string1.replace(common_string, ''), string2.replace(common_string, '')


def get_common_root(input_set):

    unique_element = list()
    iter_set = iter(input_set)

    previous_element = next(iter_set)
    element = next(iter_set)
    common_substring = extract_common_substring(previous_element, element)
    unique_substring = extract_unique_substring(element, previous_element, common_substring)
    for unique in unique_substring:
        if unique not in unique_element:
            unique_element.append(unique)
    previous_element = element
    for element in input_set:
        common_substring = extract_common_substring(previous_element, element)
        unique_substring = extract_unique_substring(element, previous_element, common_substring)
        for unique in unique_substring:
            if unique not in unique_element:
                unique_element.append(unique)
        previous_element = element
    all_unique_element = '_'.join(sorted(unique_element))
    return common_substring, all_unique_element


def record_df(df, colnames, path_to_record, percentage=False):
    """
    Record the produced df into a csv file.
    It creates an unique filename based on which question the df contains
    and add all the different questions in the filename in case of
    multiple question.
    In the case of percentage == True, it add [perc] at the end of the filename
    :params:
        :df DataFrame(): the df containing the data
        :path_to_record str(): the folder_name where the data will be stored
        :percentage boo(): if the df contains percentage or not
    :return:
        :filename str(): the full filename to pass to percentage_count() later
        as that function does not have access to the code after cleaning the headers
    """
    def check_directory(path):
        """
        Try to create a directory. If the directory
        exists, it ignore the error. If the error is something else
        it raises an exception
        """
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
    if path_to_record:
        check_directory(path_to_record)
        # Create a filename for the file to be saved based on the code of the question
        unique_code = set(s.split('. ')[0] for s in colnames)
        if len(unique_code) > 1:
            # Some table such as the likert scales regroup several element. If it is the case
            # it takes the different element within the bracket
            if any('[' in s for s in unique_code):
                bracket_values = set(s.split('[')[1][:-1] for s in unique_code)
                multiple_code = set(s.split('[')[0] for s in unique_code)
                if any('likert' in s for s in multiple_code):
                    all_unique_brackets = get_common_root(bracket_values)
                    filename_path = all_unique_brackets
                else:
                    filename_path = '_'.join(multiple_code)
                    filename_path = list(unique_code)[0].split('[')[0]  # to remove anything btw brackets for some q
            else:
                filename_path = get_common_root(unique_code)
        else:
            filename_path = list(unique_code)[0].split('[')[0]  # to remove anything btw brackets for some q
        filename = os.path.join(path_to_record, '{}.{}'.format(filename_path, 'csv'))
        df.to_csv(filename, index=True, encoding='utf-8')
        return filename


def count_multi_choice(df, colnames, dropna=False, normalize=False):
    """
    """
    # Subset the dataframe
    df_sub = df[colnames]
    # As the No can be considered as absence of Yes, fill the value 'No' with na to keep Yes only
    df_sub = df_sub.fillna(value='No')
    # Calculate the count for the column
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)

    # Replace all the 0 with NA
    df_sub.fillna(value=0, inplace=True)
    df_sub = df_sub.astype(int)
    df_sub = df_sub.ix['Yes']
    df_sub = df_sub.to_frame()
    df_sub.columns = ['Count']

    df_sub = reorder_nan(df_sub, nan_reorder='end')

    return df_sub


def count_one_choice(df, colnames, file_answer, order_question,
                     dropna=False, normalize=False):
    """
    Count the values of different columns and transpose the count
    :params:
        :df pd.df(): dataframe containing the data
        :colnames list(): list of strings corresponding to the column header to select the right column
    :return:
        :result_df pd.df(): dataframe with the count of each answer for each columns
    """
    df_sub = df[colnames]
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)

    df_sub = reorder_nan(df_sub, nan_reorder='end')
    if order_question == 'True':
        new_question_index = [x.strip('"') for x in get_answer(file_answer)]
        existing_answer = [x for x in new_question_index if x in df_sub.index]
        # add back the element from the answer that would not be found in the list of answer
        # such as Nan and other
        existing_answer.extend([x for x in df_sub.index.values if x not in new_question_index])
        # Transform the nan into a proper NaN
        df_sub = df_sub.reindex(existing_answer)
    return df_sub


def count_yn(df, colnames, normalize=False, dropna=False):
    """
    """
    if len(colnames) == 1:
        colnames = colnames[0]
        df_sub = df[colnames].to_frame(name=colnames)
    else:
        df_sub = df[colnames]

    df_sub = df_sub.apply(pd.Series.value_counts,
                          dropna=dropna,
                          normalize=normalize)

    df_sub = df_sub.transpose()
    if dropna is True:
        try:
            df_sub = df_sub[['Yes', 'No']]
        except KeyError:
            try:
                df_sub = df_sub[['Yes']]
            except KeyError:
                df_sub = df_sub[['No']]

    else:
        try:
            df_sub = df_sub[['Yes', 'No', np.nan]]
        except KeyError:
            df_sub[np.nan] = 0
            try:
                df_sub = df_sub[['Yes', 'No']]
            # In case one of the field has not been filled by any participants
            # the key does not exists. Need to create it to avoid error while
            # plotting, as it expect these keys
            except KeyError:
                try:
                    df_sub = df_sub[['Yes']]
                    df_sub['No'] = 0
                except KeyError:
                    df_sub = df_sub[['No']]
                    df_sub['Yes'] = 0
    return df_sub


def count_likert(df, colnames, likert_answer, dropna=False, normalize=False, reindex=False):
    """
    Count the values of different columns and transpose the count
    :params:
        :df pd.df(): dataframe containing the data
        :colnames list(): list of strings corresponding to the column header to select the right column
    :return:
        :result_df pd.df(): dataframe with the count of each answer for each columns
    """
    # Subset the columns
    df_sub = df[colnames]

    def convert_to_int(x):
        try:
            return int(x)
        except ValueError:
            return x
    # first convert the np.nan into a value that is different
    df_sub = df_sub.fillna(-1)
    # # then transform into int to loose the decimal point
    df_sub = df_sub.applymap(lambda x: convert_to_int(x))
    # # then transform into a string
    df_sub = df_sub.applymap(str)
    # # then replace the -1 into np.nan
    df_sub = df_sub.replace({'-1': np.nan})
    # df_sub = df_sub.astype(str)
    # df_sub = df_sub.replace('.0', '', regex=True)

    # Calculate the counts for them
    df_count = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    # Reorder according to the answers order found in the folder
    if likert_answer:
        for i in likert_answer:  # Add the missing likert because they have nan value and are not in the dataset
            if i not in df_count.index:
                df_count.loc[i] = np.nan
        df_count = df_count.reindex(index=likert_answer)

    # There is one exception with the questions about general satisfaction.
    # The structure of the questions is as follow:
    # likert3[satisgen1]. [In general, how satisfied are you with [Your current position]]',
    # 'likert3[satisgen2]. [In general, how satisfied are you with [Your career]]'
    # therefore if the goes through the cleaninng process it loose the question header
    return df_count


def get_percentage(df, filename=None, dropna=True):
    """
    Normalise results to be plotted
    """
    if len(df.columns) > 1 and len(df.index) > 1:
        by_row, by_col = True, False
    else:
        by_row, by_col = True, True
    if dropna is True:
        # get nan Percentage
        # 'Percentage NaN'
        df = df.drop(np.nan, errors='ignore')
        # For Y/N/NAN the nan values are stored in the column nan
        # drop it for them only
        try:
            df = df.drop(np.nan, axis=1)
        except ValueError:
            df = df.fillna(0)  # In case of likert, the df is transpose and here replace with 0 to be able to compute percentage
    value = compute_percentage(df, by_row, by_col)

    index_df = df.index
    name_df = df.columns
    if len(name_df) == 1:
        name_df = ["{} [PERCENTAGE]".format(x) for x in df.columns]
    if len(index_df) == 1:
        index_df = ["{} [PERCENTAGE]".format(x) for x in df.index]
    percent = pd.DataFrame(value, columns=name_df)
    percent.index = index_df
    if filename:
        filename = filename[:-4] + '[PERC]' + '.csv'
        percent.to_csv(filename, index=True, encoding='utf-8')
    percent.index.names = df.index.names
    return percent


def get_words_count(df, column):
    """
    Get the count words using wordcloud
    """
    try:
        return wordcloud(df, column)
    except ZeroDivisionError:
        return "This question does not have values"


def set_title(df, questions, type_question):
    """
    """

    if len(questions) == 1:
        renamed_q = [questions[0].split('.')[1].replace('[', '').replace(']', '').strip()]
        df.index.names = renamed_q
        return df
    else:
        # Get the code of the questions and check in transforming_title if it corresponds to something
        unique_code = list(set(s.split('. ')[0].strip() for s in questions))
        unique_code = ''.join(i for i in unique_code[0] if not i.isdigit())
        unique_code = unique_code.replace('[', '').replace(']', '').replace(',', '')
        # unique_code = unique_code.replace('likert, '')
        unique_code = unique_code.replace('likert', '')
        try:
            df.index.names = [corresponding_title[unique_code]]
        except KeyError:
            multichoice_title = list(set(s.split('. ')[1].split('[')[0].strip() for s in questions))
            df.index.names = [multichoice_title[0].replace('[', '').replace(']', '').strip()]

        return df


def get_count(df, questions, type_question, file_answer, order_question, path_to_record=None):
    """
    Choose which type of counting needs to be done

    :params:
        df dataframe(): dataframe containing all the data
        questions list(): list of the question strings to
        type_questions str(): type of questions that list_questions represent
        file_answer str(): path to the file containing the question's answers
    :return:
        df(): of the count value of the questions
    """
    # Only apply the remove_code for the question with one columns
    # When several columns, the rename_columns is True and get broken
    # With it. Moreover, as the title doesn't appears anywhere on the plots and
    # tables, it is not needed.
    questions_tokeep_for_writing = questions

    if type_question.lower() == 'y/n/na':
        counted_df = count_yn(df, questions, dropna=False)
        counted_df = apply_rename_columns(counted_df, by='index')

    elif type_question.lower() == 'one choice':
        counted_df = count_one_choice(df, questions, file_answer, order_question)
        if order_question is False:
            counted_df = apply_rename_columns(counted_df, by='index')

    elif type_question.lower() == 'multiple choices':
        counted_df = count_multi_choice(df, questions)
        counted_df = apply_rename_columns(counted_df, by='index')

    elif type_question.lower() == 'likert':
        likert_answer = get_answer(file_answer)
        counted_df = count_likert(df, questions, likert_answer)

        if len(questions) > 1:
            counted_df = apply_rename_columns(counted_df, by='columns')

    elif type_question.lower() == 'ranking':
        counted_df = count_one_choice(df, questions, file_answer, order_question)
        counted_df = apply_rename_columns(counted_df, by='columns')

    elif type_question.lower() == 'freetext':
        counted_df = get_words_count(df, questions)

    elif type_question.lower() == 'freenumeric':
        counted_df = df[questions]

    elif type_question.lower() == 'datetime':
        pass

    # Rename the index of the df to be able to get it later
    counted_df = set_title(counted_df, questions, type_question)

    if path_to_record:
        file_path = record_df(counted_df, questions_tokeep_for_writing, path_to_record)
        return counted_df, file_path
    else:
        return counted_df, None
