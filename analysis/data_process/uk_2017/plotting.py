#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib
# # When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt

from likertScalePlot import likert_scale, get_colors, add_labels


def create_bars(df, type_plot, stacked, colors):
    """
    """
    return df.plot(kind=type_plot, stacked=stacked, color=colors)


def plot_bar_char(df, sort_order=False, stacked=False,
                  horizontal=False, dropna=True, legend=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :colname str(): string that have the column header to select the right column
    """
    # Create the figure object
    fig = plt.figure(figsize=(10, 8))
    # Create an axes object in the figure
    # ax = fig.add_subplot(111)
    colors = get_colors(df, plt.cm.tab20, axis=0)

    if dropna is True:
        df.drop(np.nan, 0, inplace=True, errors='ignore')
    type_plot = 'bar'
    if sort_order:
        df = df.sort_values(by=df.columns, ascending=False)
    if horizontal is True:
        type_plot='barh'

    bars = create_bars(df, type_plot, stacked, colors)

    # Modifying the whitespaces between the bars and the graph
    plt.margins(0.02, 0.02)
    if legend:
        if len(df.columns) >= 6:
            nbr_col = 2
        elif len(df.columns) >=10:
            nbr_col = 10
            type_plot='barh'
        else:
            nbr_col = 1
        plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", ncol=nbr_col)
    else:
        plt.legend().set_visible(False)
    return plt

def plot_unique_var(df, sort_order=False, stacked=False, horizontal=False, dropna=True):
    """
    """
    df = df.transpose()
    plt = plot_bar_char(df, sort_order=sort_order, stacked=False, horizontal=False, dropna=dropna)
    # plt.set_xticklabels(df.columns, rotation=0)
    plt.suptitle(df.columns[0])
    return plt


def plot_multiple_var(df, sort_order=False, stacked=False, horizontal=False, dropna=True):
    """
    """
    df = df.transpose()
    plt = plot_bar_char(df, sort_order=sort_order, stacked=False, horizontal=False, dropna=dropna)
    # plt.set_xticklabels(df.columns, rotation=0)
    plt.suptitle(df.columns[0])
    return plt


def plot_discrete():
    """
    """
    # Calculate the average of all the time_activity questions and plotting them
    # Convert the different column to an int value to be able to calculate the mean after
    # The option 'coerce' is needed to force passing the NaN values
    # df[time_activity] = df[time_activity].apply(pd.to_numeric, errors='coerce')
    # mean_activity = df[time_activity].mean(axis=0)
    pass


def plot_y_n_multiple(df, sort_order='Yes', horizontal=True,
                      legend=True, set_label=False):
    """
    Plotting Y-N values as stacked bars when passed several questions at the same time.
    If want to plot single question Y-N see plot_single_y_n()
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :sort_order bool(): to order the value by the number of yes
        :horizontal bool(): to plot the bar horizontal rather than vertical (Default behaviour)
        :legend bool(): to show the legend or not
        :set_labels bool(): to add labels on the individuals bars
        :set_n bool(): to show the total n for each items

    :return:
        :fig matplotlib.plt.plot(): Return the plot itself
    """
    df = df[['Yes', 'No']]
    fig, ax = plt.subplots()
    index = np.arange(len(df))
    colors = plt.cm.tab20
    bar_width = 0.9
    opacity = 0.7

    # To set up the label on x or y axis
    label_txt = df.index
    label_ticks = range(len(df.index))

    # Sorting the df with the Yes values
    if sort_order.lower() == 'yes':
        df.sort_values(by='Yes', inplace=True, ascending=False)

    if horizontal is True:
        # Reverse the list otherwise the bars are build in the reverse
        # order than the dataframe
        # Not WORKING
        df = df.reindex(index=df.index[::-1])
        for i, d in enumerate(df.index[::-1]):
            yes_bar = ax.barh(index[i], width=df['Yes'][i], height=bar_width, color=colors(0), label='Yes')
            no_bar = ax.barh(index[i], width=df['No'][i], height=bar_width, left=df['Yes'][i], color=colors(3), label='No')
    else:
        yes_bar = ax.bar(index, df['Yes'], width=bar_width, bottom=None, color=colors(0), label='Yes')
        no_bar = ax.bar(index, df['No'], width=bar_width, bottom=df['Yes'], color=colors(3), label='No')

    if set_label is True:
        pass

    # Add the legend
    ax.legend((yes_bar, no_bar), ('Yes', 'No'))

    # Add the x-labels
    if horizontal is True:
        plt.yticks(label_ticks, label_txt)
    else:
        # This set the xlimits to center the xtick with the bin
        # Explanation found here:
        # https://stackoverflow.com/a/27084005/3193951
        plt.xlim([-1, len(df.index)])
        plt.xticks(label_ticks, label_txt, rotation=90)

    # Modifying the whitespaces between the bars and the graph
    plt.margins(0.02, 0.02)

    return fig


def plot_y_n_single(df, dropna=True):
    """
    """
    if dropna is True:
        df.drop(np.nan, 1, inplace=True, errors='ignore')
    colormap = plt.cm.tab20
    df.sort_values(by='Yes', inplace=True, ascending=False)
    df = df.transpose()
    ax = df.plot(kind='bar', stacked=False, color=[colormap(0), colormap(3)],
                title=df.columns[0], legend=None)
    return ax


def plot_likert(df):
    return likert_scale(df)


def get_plot(df, type_question):

    try:
        if type_question.lower() == 'y/n/na':
            if len(df.index) == 1:
                return plot_y_n_single(df)
            return plot_y_n_multiple(df, sort_order='name')

        elif type_question.lower() == 'likert':
            if len(df.index) == 1:
                return plot_unique_var(df)
            return plot_likert(df)

        elif type_question.lower() == 'one choice':
            if len(df.index) == 1:
                return plot_unique_var(df, stacked=False, horizontal=False)
            return plot_multiple_var(df, stacked=False, horizontal=False)

        elif type_question.lower() == 'multiple choices':
            if len(df.index) == 1:
                return plot_unique_var(df, stacked=False, horizontal=False,
                                      sort_order=False)
            return plot_multiple_var(df, stacked=False, horizontal=False)

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
    except TypeError:  # In Case an empty v_count is passed
        return None


def main():
    from counting import get_count
    from action_file import grouping_likert_yn
    from cleaning import CleaningData
    from config import CleaningConfig
    pd.set_option('display.max_rows', 300)

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
                # if answer_format in ['y/n/na', 'likert']:
                try:
                    v_to_count = get_count(df, questions=list_questions,
                                           type_question=answer_format,
                                           file_answer=file_answer)
                    try:
                        plot = get_plot(v_to_count, answer_format)
                    except ValueError:
                        print('list_questions')
                except KeyError:
                    print('Error for the question: {}'.format(original_question))


if __name__ == "__main__":
    main()
