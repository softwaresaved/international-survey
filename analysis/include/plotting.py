#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from IPython.display import display_html
from include.likertScalePlot import likert_scale, get_colors


def wrap_labels(labels, max_size=20):
    """
    Function to automatically wrap labels if they are too long
    Split only if whitespace
    params:
        :labels list(): of strings that contains the labels
        :max_size int(): 20 by Default, the size of the string
        before being wrapped
    :return:
        :list() of wrapped labels according to the max size
    """
    def split_at_whitespace(label):
        label_to_return = list()
        n = 0
        for letter in label:
            n +=1
            if n >= max_size:
                if letter == ' ':
                    letter = '\n'
                    n = 0
            label_to_return.append(letter)
        return ''.join(label_to_return)

    return [split_at_whitespace(label) for label in labels]


def remove_to_right_line(ax):
    """
    Remove the top and the right axis
    """
    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    return ax


def plot_bar_char(df, sort_order=False, stacked=False,
                  horizontal=False, dropna=True, legend=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :colname str(): string that have the column header to select the right column
    """
    def create_bars(df, type_plot, stacked, colors):
        """
        """
        return df.plot(kind=type_plot, stacked=stacked, color=colors)

    def _setup_legend():
        """
        Setting up the legend
        """
        pass

    # Create the figure object
    colors = get_colors(df, plt.cm.tab20, axis=0)

    if dropna is True:
        df.drop(np.nan, 0, inplace=True, errors='ignore')
    type_plot = 'bar'
    # if sort_order:
    #     df = df.sort_values(by=df.columns, ascending=False)
    if horizontal is True:
        type_plot='barh'

    create_bars(df, type_plot, stacked, colors)

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
        plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", ncol=nbr_col)
    else:
        plt.legend().set_visible(False)

    # Add the labels

    # To set up the label on x or y axis
    label_txt = wrap_labels(df.index)
    label_ticks = range(len(df.index))
    if horizontal is True:
        plt.yticks(label_ticks, label_txt)
    else:
        # This set the xlimits to center the xtick with the bin
        # Explanation found here:
        # https://stackoverflow.com/a/27084005/3193951
        plt.xlim([-1, len(df.index)])
        plt.xticks(label_ticks, label_txt, rotation=90)

    return plt


def plot_unique_var(df, sort_order=False, stacked=False, horizontal=False, dropna=True):
    """
    """
    # df = df.transpose()
    # Set up a bigger size
    if len(df.index) > 10:
        matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
    plt = plot_bar_char(df, sort_order=sort_order, stacked=stacked, horizontal=False, dropna=dropna)
    # plt.set_xticklabels(df.columns, rotation=0)
    plt.suptitle(df.columns[0])

    y_label = 'Percentage'
    plt.ylabel(y_label)
    plt.yticks(np.arange(0, 100, 10))

    return plt


def plot_multiple_var(df, sort_order=False, stacked=False, horizontal=False, dropna=True, legend=False, ranking=False):
    """
    """
    plt = plot_bar_char(df, sort_order=sort_order, stacked=stacked, horizontal=horizontal, dropna=dropna, legend=legend)
    plt.suptitle(df.columns[0])
    if ranking is True:
        plt.yticks(np.arange(0, 100, 10))

    y_label = 'Percentage'
    plt.ylabel(y_label)
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


def plot_y_n_multiple(df, sort_order='Yes', horizontal=False,
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
    ax = remove_to_right_line(ax)
    index = np.arange(len(df))
    colors = plt.cm.tab20
    bar_width = 0.9
    # opacity = 0.7

    # # Sorting the df with the Yes values
    # if sort_order.lower() == 'yes':
    #     df.sort_values(by='Yes', inplace=True, ascending=False)

    if horizontal is True:
        # Reverse the list otherwise the bars are build in the reverse
        # order than the dataframe
        # Not WORKING
        # df = df.reindex(index=df.index[::-1])
        for i, d in enumerate(df.index):
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
    # To set up the label on x or y axis
    label_txt = wrap_labels(df.index)
    label_ticks = range(len(df.index))
    if horizontal is True:
        plt.yticks(label_ticks, label_txt)
    else:
        # This set the xlimits to center the xtick with the bin
        # Explanation found here:
        # https://stackoverflow.com/a/27084005/3193951
        plt.xlim([-1, len(df.index)])
        plt.xticks(label_ticks, label_txt, rotation=90)
        y_label = 'Percentage'
        ax.set_ylabel(y_label)
        plt.yticks(np.arange(0, 100, 10))

    # Modifying the whitespaces between the bars and the graph
    plt.margins(0.02, 0.02)

    return fig


def plot_y_n_single(df, dropna=True):
    """
    """

    y_label = 'Percentage'

    if dropna is True:
        df.drop(np.nan, 1, inplace=True, errors='ignore')
    colormap = plt.cm.tab20
    df.sort_values(by='Yes', inplace=True, ascending=False)
    df = df.transpose()
    ax = df.plot(kind='bar', stacked=False, color=[colormap(0), colormap(3)],
                 title=df.columns[0], legend=None)
    ax.set_ylabel(y_label)
    plt.yticks(np.arange(0, 100, 10))

    return ax


def plot_likert(df, title_plot):

    return likert_scale(df, title_plot=title_plot)


def plot_numeric_var(df):
    """
    """
    print(df.describe())
    n_bins = 40
    y_label = 'Frequencies'
    # Get the first column name of the df to label the x-axis. This plot expects only one columns
    x_label = df.columns.values.tolist()[0]

    fig, ax = plt.subplots()
    ax = remove_to_right_line(ax)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.hist(df.dropna().values, n_bins, normed=False, edgecolor='grey', linewidth=1)
    min_value = int(math.floor(min(df.dropna().values)))
    max_value = int(math.ceil(max(df.dropna().values)))
    step = int(math.ceil((max_value - min_value) / n_bins))
    plt.xticks(np.arange(min_value, max_value +1, step))
    # ax.boxplot(df.dropna().values)

    return fig


def plot_freetext(wc):
    """
    """
    # In case the column only has empty value, the wc returned from
    # counting.get_words_count() is a string mentioning that. Therefore
    # nothing to plot. It is needed otherwise the previous successful wc is plotted
    if not isinstance(wc, str):
        plt.figure()
        ax = plt.imshow(wc, interpolation='bilinear')
        ax = plt.axis('off')
        return wc
    else:
        return None


def get_plot(df, type_question, title_plot=False):

    try:
        # Remove any [PERCENTAGE] strings from either the columns names or the row index name
        # remove for the columns
        df = df.rename(columns={col: col.replace('[PERCENTAGE]', '') for col in df.columns})
        # Remove for the row index
        df = df.rename(index={col: col.replace('[PERCENTAGE]', '') for col in df.index})
    except AttributeError:  # In case of numpy number in freenumeric case
        pass

    try:
        if type_question.lower() == 'y/n/na':
            if len(df.index) == 1:
                return plot_y_n_single(df)
            return plot_y_n_multiple(df, sort_order='name')

        elif type_question.lower() == 'likert':
            if len(df.index) == 1:
                df = df.transpose()
                return plot_unique_var(df)
            return plot_likert(df, title_plot)

        elif type_question.lower() == 'one choice':
            if len(df.index) == 1:
                return plot_unique_var(df, stacked=False, horizontal=False)
            return plot_multiple_var(df, stacked=False, horizontal=False)

        elif type_question.lower() == 'multiple choices':
            if len(df.index) == 1:
                return plot_unique_var(df, stacked=False, horizontal=False,
                                       sort_order=False)
            return plot_multiple_var(df, stacked=False, horizontal=False)

        elif type_question.lower() == 'freenumeric':
            return plot_numeric_var(df)

        elif type_question.lower() == 'ranking':
            return plot_multiple_var(df, stacked=True, horizontal=False, legend=True, ranking=True)

        elif type_question.lower() == 'freetext':
            # pass
            return plot_freetext(df)

        elif type_question.lower() == 'datetime':
            pass

        else:
            pass
    except TypeError:  # In Case an empty v_count is passed
        return None


def html_by_side(*args):
    """
    https://stackoverflow.com/a/44923103
    """
    html_str=''
    for df in args:
        html_str+=df.to_html()
    display_html(html_str.replace('table', 'table style="display:inline"'), raw=True)

def display_side_by_side(*args, merging=False):
    """
    Display the tables side by side.
    If the dataset can be merged in one, it is the preferred solution
    If it is not possible it return an html version of the dataframe and show them side-by-side
    :params:
        *args: list of pandas dataframes to display side by side
        merging bool(): To decide if the dataframes are merge into one or if they are displayed side-by-side
    :return:
        None
    """
    if True:
        pass
        # for df in args:
    else:
        html_by_side(args)


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
                try:
                    v_to_count = get_count(df, questions=list_questions,
                                           type_question=answer_format,
                                           file_answer=file_answer)
                    try:
                        get_plot(v_to_count, answer_format)
                    except ValueError:
                        print('list_questions')
                except KeyError:
                    print('Error for the question: {}'.format(original_question))


if __name__ == "__main__":
    main()
