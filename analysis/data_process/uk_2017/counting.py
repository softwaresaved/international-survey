#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from config import CleaningConfig, NotebookConfig
from cleaning import CleaningData
from action_file import grouping_likert_yn
from plotting import get_plot


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

    # Calculate the counts for them
    if multiple_choice is True:
        print(df_sub)
        df_sub = df_sub[df_sub == 'Yes'].apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    else:
        df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    if sort_values is True:
        df_sub.sort_values(by='Yes', ascending=False, inplace=True, na_position='last')
    # Transpose the column to row to be able to plot a stacked bar chart
    df_sub = df_sub.transpose()
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
        df_sub.sort_values(ascending=True, inplace=True)
    # Transpose the column to row to be able to plot a stacked bar chart
    df_sub = df_sub.transpose()
    if dropna is True:
        df_sub = df_sub[['Yes', 'No']]
    else:
        df_sub = df_sub[['Yes', 'No', np.nan]]
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
    # Transpose the column to row to be able to plot a stacked bar chart
    if likert_answer:
        likert_answer = [x for x in likert_answer if x in df_sub.index]
        df_sub = df_sub.reindex(index=likert_answer)
    return df_sub.transpose()




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
        return count_yn(df, questions, multiple=multiple,
                        dropna=False)


    elif type_question.lower() == 'one choice':
        return count_choice(df, questions, multiple_choice=False)

    elif type_question.lower() == 'multiple choices':
        return count_choice(df, questions, multiple_choice=True)

    elif type_question.lower() == 'likert':
        try:
            likert_answer = get_answer(file_answer)
        except FileNotFoundError:
            likert_answer = None
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


def main():
    """
    """
    pd.set_option('display.max_rows', 300)
    import matplotlib

    # When using Ipython within vim
    matplotlib.use('TkAgg')

    # When using within jupyter

    import matplotlib.pyplot as plt
    import time
    #  When using this script with ipython and vim
    plt.ion()
    plt.show()


    # Load dataset
    df = pd.read_csv(CleaningConfig.raw_data)

    # Cleaning_process
    cleaning_process = CleaningData(df)
    df = cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()
    for s in cleaning_process.structure_by_section:
        section = cleaning_process.structure_by_section[s]
        for group in section:
            for question in grouping_likert_yn(section[group]):
                list_questions = question[0]
                original_question = question[1]
                answer_format = question[2]
                file_answer = question[3]
                if answer_format == 'multiple choices':
                    print(answer_format)
                    try:
                        v_to_count = get_count(df, list_questions, answer_format, file_answer)
                        print(v_to_count)
                        get_plot(v_to_count, answer_format)
                    except ValueError:
                        raise
                # if v_to_count is not None:
                #     print(v_to_count)

                # notebook.add_freq_table(list_questions, answer_format)
                # notebook.add_plot(counted_value, answer_format, file_answer)
            # except KeyError:
            #     print('Error for the question: {}'.format(original_question))


if __name__ == "__main__":
    main()
