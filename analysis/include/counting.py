#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from include.likertScalePlot import compute_percentage
from include.textCleaning import wordcloud


def get_answer(file_answer):
    """
    """
    with open(file_answer, 'r') as f:
        return [x.split(';')[0].rstrip() for x in f.readlines()]


def order_answers(df, mode_reorder=None, nan_reorder='end', list_order=None):
    """
    Function to reindex the df according to
    the argument passed. It can either leave at it is
    or ordering by taking the order from  the answer file
    or ordering according to the count. The default behaviour
    is to re-order with the count

    It also decide if the NA is pushed at the end of the
    reorder or order with the number of count. The default is
    to put the np.NaN at the end.

    :params:
        :df pd.dataFrame(): The input df to sort
        :mode_reorder str(): The type or reordering
            None: Nothing is done
            count: reorder according to the count
            file_order: reorder according to the file_answer
        :nan_reorder:
            None: Nothing is done
            end: put the np.Nan at the end
            count: order the np.Nan according to the count
        :list_order list(): list of order that is required if option
            file_order is chosen

    :return:
        df pd.dataFrame(): The sorted df
    """

    def reorder_nan(df, nan_reorder):
        """
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
        elif nan_reorder is None:
            pass
        else:
            raise

        return df

    df = reorder_nan(df, nan_reorder)

    return df


def count_choice(df, colnames, rename_columns=False,
                 dropna=False, normalize=False,
                 multiple_choice=False, sort_values=False):
    """
    Count the values of different columns and transpose the count
    :params:
        :df pd.df(): dataframe containing the data
        :colnames list(): list of strings corresponding to the column header to select the right column
    :return:
        :result_df pd.df(): dataframe with the count of each answer for each columns
    """
    df_sub = df[colnames]

    if rename_columns is True:
        try:
            df_sub.columns = [s.split('[')[2][:-1] for s in colnames]
        except IndexError:
            pass

    if multiple_choice is True:
        df_sub = df_sub.fillna(value='No')

    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)

    if multiple_choice is True:
        df_sub.fillna(value=0, inplace=True)
        df_sub = df_sub.astype(int)
        df_sub = df_sub.ix['Yes']
        df_sub = df_sub.to_frame()
        df_sub.columns = ['Count']

    df_sub = order_answers(df_sub, nan_reorder='end')
    return df_sub


def count_yn(df, colnames, multiple=False, normalize=False, dropna=False):
    """
    """
    if multiple is True:
        df_sub = df[colnames]
    else:
        df_sub = df[colnames].to_frame(name=colnames)

    df_sub = df_sub.apply(pd.Series.value_counts,
                          dropna=dropna,
                          normalize=normalize)

    # Transpose the column to row to be able to plot a stacked bar chart
    df_sub = df_sub.transpose()
    if dropna is True:
        df_sub = df_sub[['Yes', 'No']]
    else:
        try:
            df_sub = df_sub[['Yes', 'No', np.nan]]
        except KeyError:
            df_sub[np.nan] = 0
            df_sub = df_sub[['Yes', 'No']]
    return df_sub


def count_likert(df, colnames, likert_answer, rename_columns=True, dropna=True, normalize=False, reindex=False):
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

    if rename_columns is True:
        try:
            df_sub.columns = [s.split('[')[2][:-1] for s in colnames]
        except IndexError:
            pass

    # Calculate the counts for them
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    if likert_answer:
        likert_answer = [x for x in likert_answer if x in df_sub.index]
        df_sub = df_sub.reindex(index=likert_answer)
    # Transpose the column to row to be able to plot a stacked bar chart
    return df_sub.transpose()


def get_percentage(df, dropna):
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
        percent_na = df.iloc[-1,: ]
        # / df.sum(axis=1)
        df = df.drop(np.nan, errors='ignore')
        # For Y/N/NAN the nan values are stored in the column nan
        # drop it for them only
        try:
            df = df.drop(np.nan, axis=1)
        except ValueError:
            pass
    value = compute_percentage(df, by_row, by_col)

    index_df = df.index
    name_df = df.columns
    if len(name_df) == 1:
        name_df = ["{} [PERCENTAGE]".format(x) for x in df.columns]
    if len(index_df) == 1:
        index_df = ["{} [PERCENTAGE]".format(x) for x in df.index]
    percent = pd.DataFrame(value, columns=name_df)
    percent.index = index_df
    # if dropna is True:
        # percent.loc['Proportion of NaN in total'] = percent_na
        # percent.loc['Proportion of NaN in total'] = percent_na
        # percent.append(percent_na.rename('Proportion of NaN to the total'))
    return percent


def get_words_count(df, column):
    """
    Get the count words using wordcloud
    """
    try:
        return wordcloud(df, column)
    except ZeroDivisionError:
        return "This question does not have values"



def get_count(df, questions, type_question, file_answer):
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
    if type_question.lower() == 'y/n/na':
        if len(questions) == 1:
            questions = questions[0]
            multiple = False
        else:
            multiple = True
        count = count_yn(df, questions, multiple=multiple, dropna=False)
        return count

    elif type_question.lower() == 'one choice':
        return count_choice(df, questions, multiple_choice=False, rename_columns=True)

    elif type_question.lower() == 'multiple choices':
        return count_choice(df, questions, multiple_choice=True, rename_columns=True)

    elif type_question.lower() == 'likert':
        likert_answer = get_answer(file_answer)
        if len(questions) == 1:
            rename_columns = False
        else:
            rename_columns = True
        return count_likert(df, questions, likert_answer, rename_columns)

    elif type_question.lower() == 'ranking':
        return count_choice(df, questions, multiple_choice=False, rename_columns=True)

    elif type_question.lower() == 'freetext':
        return get_words_count(df, questions)
        # pass

    elif type_question.lower() == 'freenumeric':
        return df[questions]

    elif type_question.lower() == 'datetime':
        pass

    else:
        pass
