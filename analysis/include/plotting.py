#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from include.likertScalePlot import likert_scale, get_colors
from include.barplot import barPlot


def plot_multiple_var(df, sort_order=False, stacked=False, horizontal=False, dropna=True, legend=False, ranking=False, title_plot=False):
    """
    """
    ax = plot_bar_char(df, sort_order=sort_order, stacked=stacked, horizontal=horizontal, dropna=dropna, legend=legend)
    # if ranking is True:
    #     plot.yticks(np.arange(0, 100, 10))
    #
    # y_label = 'Percentage'
    # plt.ylabel(y_label)
    return df, ax




def plot_likert(df):

    df = df.transpose()
    fig, ax = plt.subplots()
    plot = likert_scale(df)
    return df, fig, ax


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
    ax.hist(df.dropna().values, n_bins, normed=False, edgecolor='white', linewidth=1, color="#3F5D7D")
    min_value = int(math.floor(min(df.dropna().values)))
    max_value = int(math.ceil(max(df.dropna().values)))
    step = int(math.ceil((max_value - min_value) / n_bins))
    plt.xticks(np.arange(min_value, max_value +1, step))

    return df, fig, ax


def bar_plot(df, colormap):
    """
    """
    # Get the color palette
    colors = [colormap(np.arange(len(df)))]
    width=0.8
    ax = df.plot.bar(label='index', width=width, color=colors)

    return ax

def plot_y_n_multiple(df, sort_order='Yes', legend=True, set_label=False, title_plot=False):
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
    fig, ax = plt.subplots()
    df = df[['Yes', 'No']]
    index = np.arange(len(df))
    colors = plt.cm.tab20
    bar_width = 0.9
    # opacity = 0.7

    # # Sorting the df with the Yes values
    # if sort_order.lower() == 'yes':
    #     df.sort_values(by='Yes', inplace=True, ascending=False)

    # if horizontal is True:
    #     # Reverse the list otherwise the bars are build in the reverse
    #     # order than the dataframe
    #     # Not WORKING
    #     # df = df.reindex(index=df.index[::-1])
    #     for i, d in enumerate(df.index):
    #         yes_bar = ax.barh(index[i], width=df['Yes'][i], height=bar_width, color=colors(0), label='Yes')
    #         no_bar = ax.barh(index[i], width=df['No'][i], height=bar_width, left=df['Yes'][i], color=colors(3), label='No')
    yes_bar = ax.bar(index, df['Yes'], width=bar_width, bottom=None, color=colors(0), label='Yes')
    no_bar = ax.bar(index, df['No'], width=bar_width, bottom=df['Yes'], color=colors(3), label='No')

    if set_label is True:
        pass

    # Add the legend
    ax.legend((yes_bar, no_bar), ('Yes', 'No'))

    # Add the x-labels
    # To set up the label on x or y axis
    # remove the labels that have a value of zero
    label_txt = [wrap_labels(label) for i, label in enumerate(df.index) if df.ix[i, 0] >= 1]
    label_ticks = range(len(label_txt))
    # This set the xlimits to center the xtick with the bin
    # Explanation found here:
    # https://stackoverflow.com/a/27084005/3193951
    plt.xlim([-1, len(label_txt)])
    plt.xticks(label_ticks, label_txt, rotation=90)
    y_label = 'Percentage'
    ax.set_ylabel(y_label)
    plt.yticks(np.arange(0, 100, 10))

    # Modifying the whitespaces between the bars and the graph
    plt.margins(0.02, 0.02)

    return df, fig, ax


def plot_y_n_single(df, colormap):
    """
    """
    width=0.8
    # Take the colors associate to yes and no
    colors = [np.array((colormap(0), colormap(3)))]
    ax = df.plot.bar(label='index', width=0.8, color=colors)
    return ax


def get_plot(df, type_question, title_plot=False, dropna=True):

    colormap = plt.cm.tab20
    y_label = 'Percentage'
    # Remove any [PERCENTAGE] strings from either the columns names or the row index name
    # remove for the columns
    try:
        df = df.rename(columns={col: col.replace('[PERCENTAGE]', '') for col in df.columns})
        # Remove for the row index
        df = df.rename(index={col: col.replace('[PERCENTAGE]', '') for col in df.index})
    except AttributeError:  # In case of numpy number in freenumeric case
        pass

    # Check if dropna is True. In this case, remove the data that have a nan value

    try:
        if type_question.lower() == 'one choice' or type_question.lower() == 'multiple choices':
            ax = bar_plot(df, colormap)

        elif type_question.lower() == 'y/n/na':
            df = df.transpose()
            ax = plot_y_n_single(df, colormap)
        cosmetic_changes_plot(df, ax, title_plot=False, y_label=y_label)
    except TypeError:  # In Case an empty v_count is passed
        return None


def add_x_labels(df):

    def wrap_labels(label, max_size=20):
        """
        Function to automatically wrap labels if they are too long
        Split only if whitespace
        params:
            :labels str(): string that contains the labels
            :max_size int(): 20 by Default, the size of the string
            before being wrapped
        :return:
            :str() of wrapped labels according to the max size
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

        return split_at_whitespace(label)
    label_txt = [wrap_labels(label) for label in df.index]
    label_ticks = range(len(label_txt))
    # This set the xlimits to center the xtick with the bin
    # Explanation found here:
    # https://stackoverflow.com/a/27084005/3193951
    plt.xlim([-1, len(label_txt)])
    plt.xticks(label_ticks, label_txt, rotation=90)


def cosmetic_changes_plot(df, ax, title_plot=False, y_label='', x_index='index'):
    """
    Get the plot and return a modified one to have some
    cosmetic changes
    """
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
        # return ax

    def add_title(title_plot):
        if title_plot:
            plt.title(title_plot)
        else:
            plt.title('hdsjkadjskaldjaskljdsalkjdaslkjdaslkjdsalk')

    def add_y_label(y_label):
        ax.set_ylabel(y_label)

    # Remove the upper and right line
    remove_to_right_line(ax)

    # Add appropriate title
    add_title(title_plot)

    # Add appropriate x labels
    # add_x_labels(df)

    # Add appropriate y labels
    add_y_label(y_label)

    # Add or remove the legend
    # add_legend()
    print(ax)
    return ax

def display_side_by_side(*args):
    """
    Merging two dataframe into one were the first one contains the count values and the second
    one contains the percentage. They needs to have the same index name
    https://stackoverflow.com/a/44923103
    """
    original_df1 = args[0]
    df1 = original_df1.copy()
    original_df2 = args[1]
    df2 = original_df2.copy()
    rows, columns = df1.shape
    index_row = df2.index
    df2.index = [i.replace(' [PERCENTAGE]', '') for i in index_row]
    df2.reset_index()
    if columns == 1:
        df1['Percentage'] = df2.iloc[:, -1]
        df1.index.name = df1.columns[0]
        if df1.index.name == 'Count':
            df1.index.name = ''
        df1.columns = ['Count', 'Percentage']

    else:  # In case of Y-N, the df has Yes and No as columns
        if df1.columns[0] == 'Yes':
            df1['Yes_P'] = df2.iloc[:, 0]
            df1['No_P'] = df2.iloc[:, 1]
            try:
                df1.columns = ['Yes [Count]', 'No [Count]', 'NaN value', 'Yes [Percentage]', 'No [Percentage]']
            except ValueError:  # In case there is not a Nan
                df1.columns = ['Yes [Count]', 'No [Count]', 'Yes [Percentage]', 'No [Percentage]']
        else:
            df1.columns = ['{} [Count]'.format(l) for l in df1.columns]
            for i, colname in enumerate(df2.columns):
                df1['{} [Percentage]'.format(colname)] = df2.iloc[:, i]
    return df1


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
