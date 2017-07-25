#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from include.likertScalePlot import compute_percentage


def get_answer(file_answer):
    """
    """
    with open(file_answer, 'r') as f:
        return [x[:-1] for x in f.readlines()]


def count_choice(df, colnames, rename_columns=True,
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

    if rename_columns is True and multiple_choice is True:
        df_sub.columns = [s.split('[')[2][:-1] for s in colnames]

    if multiple_choice is True:
        df_sub = df_sub.fillna(value='No')

    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)

    if multiple_choice is True:
        df_sub.fillna(value=0, inplace=True)
        df_sub = df_sub.astype(int)
        df_sub = df_sub.ix['Yes']
        df_sub = df_sub.to_frame()
        df_sub.columns = ['Count']

    # Sorting with nan at the end, the in-built function is not working do not know why
    df_sub.sort_values(by=df_sub.columns[0], axis=0, ascending=False, inplace=True, na_position='last')
    # So implemented this dirty hack. If someone wants to fix, please do
    index_wo_nan = list()
    nan_value = False
    for x in df_sub.index:
        if pd.isnull(x):
            nan_value = True
        else:
            index_wo_nan.append(x)
    if nan_value:
        index_wo_nan.append(np.nan)

    df_sub = df_sub.reindex(index=index_wo_nan)
    return df_sub


def count_yn(df, colnames, multiple=False, normalize=False, dropna=False, sort_values=False):
    """
    """
    if multiple is True:
        df_sub = df[colnames]
    else:
        df_sub = df[colnames].to_frame(name=colnames)

    df_sub = df_sub.apply(pd.Series.value_counts,
                          dropna=dropna,
                          normalize=normalize)
    if sort_values is True:
        df_sub.sort_values(ascending=True, inplace=True, na_position='last')

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


def count_likert(df, colnames, likert_answer, rename_columns=True, dropna=True, normalize=False):
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
        df_sub.columns = [s.split('[')[2][:-1] for s in colnames]

    # Calculate the counts for them
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    if likert_answer:
        likert_answer = [x for x in likert_answer if x in df_sub.index]
        df_sub = df_sub.reindex(index=likert_answer)
    # Transpose the column to row to be able to plot a stacked bar chart
    return df_sub.transpose()


def get_percentage(df):
    """
    Normalise results to be plotted
    """
    if len(df.columns) > 1 and len(df.index) > 1:
        value = compute_percentage(df, by_row=True, by_col=False)
    else:
        value = compute_percentage(df, by_row=True, by_col=True)

    # Add [Percent] to the end of the column name to distinc the two datasets
    index_df = df.index
    name_df = df.columns
    if len(name_df) == 1:
        name_df = ["{} [PERCENTAGE]".format(x) for x in df.columns]
    if len(index_df) == 1:
        index_df = ["{} [PERCENTAGE]".format(x) for x in df.index]
    percent = pd.DataFrame(value, columns=name_df)
    percent.index = index_df
    return percent


def get_count(df, questions, type_question, file_answer):
    """
    Choose which type of counting needs to be done

    :params:
        df dataframe(): dataframe containing all the data
        questions list(): list of the question strings to
        type_questions str(): type of questions that list_questions represent

    :return:
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
        return count_choice(df, questions, multiple_choice=False)

    elif type_question.lower() == 'multiple choices':
        return count_choice(df, questions, multiple_choice=True)

    elif type_question.lower() == 'likert':
        likert_answer = get_answer(file_answer)
        if len(questions) == 1:
            rename_columns = False
        else:
            rename_columns = True
        return count_likert(df, questions, likert_answer, rename_columns)

    elif type_question.lower() == 'ranking':
        pass

    elif type_question.lower() == 'freetext':
        pass

    elif type_question.lower() == 'freenumeric':
        pass

    elif type_question.lower() == 'datetime':
        pass

    else:
        pass
