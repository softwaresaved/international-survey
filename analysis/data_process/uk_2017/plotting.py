#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pandas as pd
import numpy as np
import matplotlib
# from include import plotting
# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt


def get_type_question(input_location):
    """
    """
    with open(input_location, 'r') as f:
        return json.load(f)


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


def freq_plotting(df, colnames='count', sort_order=False, stacked=False, horizontal=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :colname str(): string that have the column header to select the right column
    """
    type_plot = 'bar'
    # Call the freq_table function to create the count to plot
    # d = freq_table(df, colnames, columns)
    if sort_order:
        df = df.sort_values(by=colnames, ascending=False)
    if horizontal is True:
        type_plot='barh'

    df[colnames].plot(kind=type_plot, stacked=stacked)
#
#
# def save_freq_plotting(df, columns, colnames=False, sort_order=False, stacked=False, horizontal=False):
#     """
#     Plot the others variables
#     :params:
#         :df pd.df(): dataframe containing the data
#         :colname str(): string that have the column header to select the right column
#     """
#     type_plot = 'bar'
#     if colnames is False:
#         colnames = columns
#     # Call the freq_table function to create the count to plot
#     d = freq_table(df, colnames, columns)
#     if sort_order:
#         d = d.sort_values(by=colnames, ascending=False)
#     if horizontal is True:
#         type_plot='barh'
#
#     d.plot(kind=type_plot, stacked=stacked)
#     return d


def count_unique_value(df, colnames, rename_columns=False, dropna=False, normalize=False):
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
    return df_sub.transpose()


def plot_likert():
    """
    """
    pass


def get_colors(df, colormap=plt.cm.RdBu, vmin=None, vmax=None):
    """
    Function to automatically gets a colormap for all the values passed in,
    Have the option to normalise the colormap.
    :params:
        values list(): list of int() or str() that have all the values that need a color to be map
        to. In case of a list() of str(), the try/except use the range(len()) to map a colour
        colormap cm(): type of colormap that need to be used. All can be found here:
            https://matplotlib.org/examples/color/colormaps_reference.html
        vmin, vmax int(): Number to normalise the return of the colourmap if needed a Normalised colourmap

    :return:
        colormap cm.colormap(): An array of RGBA values

    Original version found on stackerOverflow (w/o the try/except) but cannot find it back
    """
    values = df.columns
    norm = plt.Normalize(vmin, vmax)
    try:
        return colormap(norm(values))
    except (AttributeError, TypeError):  # May happen when gives a list of categorical values
        return colormap(norm(range(len(values))))


def create_bars(df, ax, y_pos, colors, left_gap=False):
    """
    Loop through the columns and create an horizontal bar for each.
    First it creates all the left bars, for all the columns, then the
    one on the right. Each time, it add the distance from the previous bar.
    If 'left_invisible_bar' is passed, it will create a empty gap on the left
    before the first bar to centred the plot in the middle

    :params:
        df df(): The dataframe containing the information
        ax plt(): The subplot to draw on
        y_pos np.array(): an array of the number of bars (likert items)
        colors np.array(): an array containing the colors for the different answers
        left_gap np.array(): the empty left gap needed to
            centre the stacked bar

    :return:
        patch_handles list(): A list containing the drawn horizontal stacked bars
    """
    patch_handles = []
    for i, c in enumerate(df.columns):
        d = np.array(df[c])
        if left_gap:
            new_bar = ax.barh(y_pos, d, color=colors[i], align='center', left=left_gap)
            # accumulate the left-hand offsets
            left_gap += d
        else:
            new_bar = ax.barh(y_pos, d, color=colors[i], align='center', left=left_gap)
        patch_handles.append(new_bar)
    return patch_handles


def plot_y_n(df, colnames='count', sort_order=False, stacked=False, horizontal=False, set_label=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :colname str(): string that have the column header to select the right column
    """
    df = df[['Yes', 'No']]
    fig, ax = plt.subplots()
    index = np.arange(len(df))
    bar_width = 0.35
    opacity = 0.7
    yes_bar = plt.bar(index, df['Yes'], width=bar_width, bottom=None, color='blue', label='Yes')
    no_bar = plt.bar(index, df['No'], width=bar_width, bottom=df['Yes'], color='red', label='No')
    return fig


def plot_discrete():
    """
    """
    # Calculate the average of all the time_activity questions and plotting them
    # Convert the different column to an int value to be able to calculate the mean after
    # The option 'coerce' is needed to force passing the NaN values
    # df[time_activity] = df[time_activity].apply(pd.to_numeric, errors='coerce')
    # mean_activity = df[time_activity].mean(axis=0)
    pass


def process_question(df, q, type_chart):
    """
    """
    if any(isinstance(el, list) for el in q):
        return count_unique_value(df, q)
    else:
        data_to_plot = df[q]
    if type_chart == 'barchart':
        result = freq_table(data_to_plot)
        return result


def main():

    #  When using this script with ipython and vim
    plt.ion()
    plt.show()
    pd.set_option('display.max_rows', 300)

    # load the dataframe
    df = pd.read_csv('./dataset/cleaned_data.csv')
    location_type_q = './to_plot.json'
    type_questions = get_type_question(location_type_q)

    data_to_plot = count_unique_value(df, type_questions['single_questions']['yes_no'], dropna=True)
    data_to_plot.sort_values(by='Yes').plot(kind='barh', stacked=True)


    for group in type_questions['grouped_questions']:
        pass

    for group in type_questions['single_questions']:
        if group == 'yes_no':  # aggregate in case of grouped_questions
            for q in type_questions['single_questions'][group]:
                process_question(df, q, 'yes_no')

        elif q == 'decision_job':  # ranking
            pass
        elif q.startswith('likert'):  # likert
            pass
        elif q == 'messy_data':  # wordcounts
            pass
        elif q == 'single_item':  # passing
            pass
        else:  # Should be easily plotted in bar chart for all other cases
            pass

if __name__ == "__main__":
    main()
