#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from include.likertScalePlot import likert_scale, get_colors


def plot_numeric_var(df):
    """
    """
    print(df.describe())
    n_bins = 40
    y_label = 'Frequencies'
    # Get the first column name of the df to label the x-axis. This plot expects only one columns
    x_label = df.columns.values.tolist()[0]

    fig, ax = plt.subplots()
    # ax = remove_to_right_line(ax)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.hist(df.dropna().values, n_bins, normed=False, edgecolor='white', linewidth=1, color="#3F5D7D")
    min_value = int(math.floor(min(df.dropna().values)))
    max_value = int(math.ceil(max(df.dropna().values)))
    step = int(math.ceil((max_value - min_value) / n_bins))
    plt.xticks(np.arange(min_value, max_value +1, step))

    return ax


def bar_plot(df, colormap, horizontal=False):
    """
    """
    # Get the color palette
    # colors = [colormap(np.arange(len(df)))]
    colors = get_colors(df, colormap, axis=0)
    width=0.8
    if horizontal:
        ax = df.plot.barh(label='index', width=width, color=colors)
    else:
        ax = df.plot.bar(label='index', width=width, color=colors)
    return ax


def plot_y_n_single(df, colormap):
    """
    """
    width=0.8
    # Take the colors associate to yes and no
    # colors = [np.array((colormap(0), colormap(3)))]
    colors = []
    if df.iloc[0].loc['Yes'] > 0:
        colors.append(colormap(0))
    if df.iloc[0].loc['No'] > 0:
        colors.append(colormap(3))
    ax = df.transpose().plot.bar(label='index', width=width, color=colors, fontsize=14)
    return ax


def stacked_y_n(df, colormap):
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
    width=0.8
    # Take the colors associate to yes and no
    colors = [colormap(0), colormap(3)]
    ax = df.plot.bar(width=width, color=colors, stacked=True)
    return ax


def ranking_plot(df, colormap):
    """
    """
    width = 0.8
    colors = colormap(np.arange(len(df)))
    ax = df.plot.bar(color=colors, stacked=True, width=width, fontsize=14)
    return ax


def likert_plot(df):
    df = df.transpose()
    ax = likert_scale(df)
    return ax


def get_plot(df, type_question, title_plot=False, dropna=True):
    """
    """
    colormap = plt.cm.tab20
    legend = None
    x_label = False
    wrap_label = False
    y_label = True
    dropna=True
    # Remove any [PERCENTAGE] strings from either the columns names or the row index name
    # remove for the columns
    try:
        df = df.rename(columns={col: col.replace('[PERCENTAGE]', '') for col in df.columns})
        # Remove for the row index
        df = df.rename(index={col: col.replace('[PERCENTAGE]', '') for col in df.index})
    except AttributeError:  # In case of numpy number in freenumeric case
        pass

    try:
        if type_question.lower() == 'one choice' or type_question.lower() == 'multiple choices':
            # Round the df to avoid having the column of those lower than 1 percent being showed
            df = df.round()
            ax = bar_plot(df, colormap)
            legend = False
            x_label = True

        elif type_question.lower() == 'y/n/na':
            if len(df.index) == 1:
                # Round the df to avoid having the column of those lower than 1 percent being showed
                df = df.round()
                df.sort_values(by='Yes', inplace=True, ascending=False)
                ax = plot_y_n_single(df, colormap)
                legend = False
            else:
                ax = stacked_y_n(df, colormap)
                legend = True
                x_label = True
                wrap_label = True

        elif type_question.lower() == 'ranking':
            ax = ranking_plot(df, colormap)
            legend = True
            wrap_label = True

        elif type_question.lower() == 'likert':
            # Way to check if the likert question here as only one question
            # In that case, it plot a normal barplot
            if len(df.columns) == 1:
                df = df.round()
                ax = bar_plot(df, colormap)
                legend = False
                x_label = True
                dropna = False
            else:
                ax = likert_plot(df)
                y_label = False

        elif type_question.lower() == 'freenumeric':
            ax = plot_numeric_var(df)

        cosmetic_changes_plot(df, ax, legend=legend, x_label=x_label, wrap_label=wrap_label, y_label=y_label, dropna=dropna)

    except TypeError:  # In Case an empty v_count is passed
        return None


def cosmetic_changes_plot(df, ax, legend, x_label, wrap_label, y_label, dropna):
    """
    Get the plot and return a modified one to have some
    cosmetic changes
    """

    # Remove the upper and right line
    remove_to_right_line(ax)

    # Set up legends
    setup_legend(ax, legend)
    # Add appropriate title
    add_title(df)
    #
    # # Add appropriate x labels
    if x_label is True:
        add_x_labels(df, wrap_label, dropna)
    #
    # # Add appropriate y labels
    if y_label:
        add_y_label(ax)

    # Remove the xlabel title
    ax.set_xlabel('')

    return ax


# def add_labels():
#
# # set individual bar lables using above list
#     for i in ax.patches:
#         # get_width pulls left or right; get_y pushes up or down
#         ax.text(i.get_width()+700, i.get_y()+.18, \
#                 str(round((i.get_width()), 2)), fontsize=11, color='dimgrey')


def add_title(df):
    plt.title(df.index.name, fontsize=16)


def setup_legend(ax, legend):
    if legend is True:
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    elif legend is False:
        ax.legend().set_visible(False)
    else:
        pass


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


def add_y_label(ax):
    ax.set_ylabel('Percentage', fontsize=14)
    # plt.yticks(np.arange(0, 100, 10))


def add_x_labels(df, wrap_label, dropna):

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
    # Add the x-labels
    # To set up the label on x or y axis
    if dropna is True:
        # remove the labels that have a value of zero
        if wrap_label:
            label_txt = [wrap_labels(label) for i, label in enumerate(df.index) if df.ix[i, 0] >= 1]
        else:
            label_txt = [label for i, label in enumerate(df.index) if df.ix[i, 0] >= 1]
    else:

        # remove the labels that have a value of zero
        if wrap_label:
            label_txt = [wrap_labels(label) for i, label in enumerate(df.index)]
        else:
            label_txt = [label for i, label in enumerate(df.index)]
    label_ticks = range(len(label_txt))
    # This set the xlimits to center the xtick with the bin
    # Explanation found here:
    # https://stackoverflow.com/a/27084005/3193951
    plt.xlim([-1, len(label_txt)])
    plt.xticks(label_ticks, label_txt, rotation=90, fontsize=14)


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
    # Round the value to display them
    # And remove the remaining trailing 0 by converting to str
    df2 = df2.round()
    df2.loc[:, df2.dtypes== np.float64] = df2.loc[:, df2.dtypes== np.float64].astype(str)
    df2 = df2.replace('.0', '', regex=True)
    rows, columns = df1.shape
    index_row = df2.index
    df2.index = [i.replace(' [PERCENTAGE]', '') for i in index_row]
    df2.reset_index()
    if columns == 1:
        df1['Percentage'] = df2.iloc[:, -1]
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
