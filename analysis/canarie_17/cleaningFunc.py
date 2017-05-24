#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

"""
Collection of function to clean the raw data collected from the different survey.
It can be reused accross surveys (UK, CANARIE,...) or being only used for one survey but for
several columns or rows
"""


def explore_other(colname, printUnique=False):
    """
    To output the unique value of the column
    and the column '[Other]' associated with it (in the Canarie survey)
    :params:
        :colnames str(): string to match the column
    :return: the colname to be used in following function without typing it again
    """
    col_other = colname + ' [Other]'
    if printUnique is True:
        print('Unique values in the normal column')
        print(df[colname].unique())
        print('Unique values in the other columns')
        print(df[col_other].unique())
    return colname


def recode_values(x, replacement_values, default=False):
    """
    Function to use with an  apply on a Serie to replace values if they match
    the values from the dictionary passed into the argument.
    :params:
        :replacement_values dict(): K are the content to match and values the content
        to replace with
        :default: if a value is given to default, this value will be return, if it is
        false, the passed value is returned instead
    :return:
        :x: the x is returned or the replacement values if found in the dictionary or the
        default if not None.
    """
    if not pd.isnull(x):
        for k in replacement_values:
            if str(k).lower() in str(x).lower():
                return replacement_values[k]
        if default:
            return default
    return x


def merging_others(df, colname, replacement_values=None):
    """
    Function to wrap the different modification applied on
    the columns that have a `other` column associated.
    Only search if some others could be merged with the prexisting answers
    and merge it to into the original column, then transform the column into
    categorical variable
    :params:
        :df pd.df(): dataframe containing the data
        :colname str(): string that have the column header to select the right column
        :replacement_values dict(): contain which value to match in the column 'other' as
        the key and which value to replace with. If it is None, skip the transformation (Default)
    :return:
        :None: The operation is a replace `inplace`
    """
    colname_other = var+ ' [Other]'
    if replacement_values:
        df[colname_other] = df[colname_other].apply(recode_values, args=(replacement_values, 'Other'))
        df[colname].replace('Other', df[colname_other], inplace=True)

    df[colname] = df[colname].str.capitalize().astype('category')



# Recategorise the answers into 10 categories
def replace_project(x):
    """
    To use with df[column].apply(replaceproject) to change the
    the number into a specific categorie
    :params:
        x int(): this is the value of the row to match with a
        category
    :return:
        str(): to replace the x with a category
    """
    if pd.isnull(x):
        return
    if x >=1 and x <=3:
        return "1-3"
    elif x >=4 and x <=6:
        return "4-6"
    elif x >=7 and x <=9:
        return "7-9"
    elif x > 10 and x <= 12:
        return "10-12"
    elif x > 13 and x <= 15:
        return "13-15"
    elif x > 16 and x <= 18:
        return "16-18"
    elif x > 19 and x <= 21:
        return "19-21"
    elif x >= 22:
        return ">=22"

