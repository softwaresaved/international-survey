#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pandas as pd
import numpy as np


def freq_table(df, colnames=False, columns='count', add_ratio=False, sort_order=False):
    """
    """
    if colnames:
        df_to_freq = df[colnames]
    else:
        df_to_freq = df
    if add_ratio:
        output = pd.concat([pd.crosstab(df_to_freq, columns='count', normalize=False),
                            pd.crosstab(df_to_freq, columns='ratio', normalize=True)],
                           axis=1)
    else:
        output = pd.crosstab(df_to_freq, colnames=[''], columns=columns)
    if sort_order:
        output = output.sort_values(by='count')
    return output

def count_unique_value_multiple(df, colnames, rename_columns=False, dropna=False, normalize=False):
    """
    Count the values of different columns and transpose the count
    :params:
        :df pd.df(): dataframe containing the data
        :colnames list(): list of strings corresponding to the column header to select the right column
    :return:
        :result_df pd.df(): dataframe with the count of each answer for each columns
    """
    # Subset the columns
    colnames = [i for j in colnames for i in j]
    df_sub = df[colnames]

    if rename_columns is True:
        df_sub.columns = [s.split('[', 1)[1].split(']')[0] for s in colnames]

    # Calculate the counts for them
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    # Transpose the column to row to be able to plot a stacked bar chart
    # return df_sub
    return df_sub.transpose()


def count_unique_value_single(df, colnames):
    """
    """
    return df[colnames].value_counts()


def count_multiple_choice(df, colnames, rename_columns=True):
    """
    """
    df_sub = df[colnames]
    if rename_columns is True:
        df_sub.columns = [s.split('[', 1)[1].split(']')[0] for s in colnames]
    df_sub = df_sub[df_sub == 'Yes'].count()
    df_sub.sort_values(ascending=False, inplace=True)
    return df_sub


def get_count():
    """
    Choose which type of counting needs to be done
    """

