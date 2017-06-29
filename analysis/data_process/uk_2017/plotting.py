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


def add_labels(df, ax, bars, rotation=0):
    """
    """
    # Create percentage for each cells to have the right annotation
    percentages = compute_percentage(df)
    # go through all of the bar segments and annotate
    for j in range(len(bars)):
        for i, bar in enumerate(bars[j].get_children()):
            bl = bar.get_xy()
            x = 0.5 *bar.get_width() +bl[0]
            y = 0.5 *bar.get_height() +bl[1]
            ax.text(x, y, "{}".format(percentages[i, j]), ha='center', rotation=rotation)




def plot_y_n_multiple(df, sort_order=False, horizontal=False,
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
    colors = plt.cm.tab10
    bar_width = 0.9
    opacity = 0.7

    # To set up the label on x or y axis
    label_txt = df.index
    label_ticks = range(len(df.index))

    # Sorting the df with the Yes values
    if sort_order is True:
        df.sort_values(by='Yes', inplace=True, ascending=False)
    else:
        pass

    if horizontal is True:
        for i, d in enumerate(df.index):
            yes_bar = ax.barh(index[i], width=df['Yes'][i], height=bar_width, color=colors(0), label='Yes')
            no_bar = ax.barh(index[i], width=df['No'][i], height=bar_width, left=df['Yes'][i], color=colors(1), label='No')
    else:
        yes_bar = ax.bar(index, df['Yes'], width=bar_width, bottom=None, color=colors(0), label='Yes')
        no_bar = ax.bar(index, df['No'], width=bar_width, bottom=df['Yes'], color=colors(1), label='No')

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




def plot_y_n_single(df):
    """
    """
    colormap = plt.cm.tab10
    return df.plot(kind='barh', stacked=True, color=[colormap(0), colormap(1)])


def plot_freq_bar_single(df):
    """
    """
    df.plot(kind='bar')

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


def plot_discrete():
    """
    """
    # Calculate the average of all the time_activity questions and plotting them
    # Convert the different column to an int value to be able to calculate the mean after
    # The option 'coerce' is needed to force passing the NaN values
    # df[time_activity] = df[time_activity].apply(pd.to_numeric, errors='coerce')
    # mean_activity = df[time_activity].mean(axis=0)
    pass


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


def main():

    #  When using this script with ipython and vim
    plt.ion()
    plt.show()
    pd.set_option('display.max_rows', 300)

    # load the dataframe
    df = pd.read_csv('./dataset/cleaned_data.csv')
    location_type_q = './to_plot.json'
    type_questions = get_type_question(location_type_q)


    # Test single question having Y_N
    single_test_y_n = count_unique_value_single(df, 'Do you consider yourself a professional software developer?')
    plot_y_n_single(single_test_y_n)

    # Test multiples questions having Y_N
    test_y_n_multiple = count_unique_value_multiple(df, type_questions['single_questions']['yes_no'],
                                         normalize=True,dropna=True)
    plot_y_n_multiple(test_y_n_multiple, sort_order=True, horizontal=False, set_label=True)

    test_bar = count_unique_value(df, type_questions['single_questions']['education'], dropna=True)
    df['What is the highest qualification you have obtained?'].value_counts().plot(kind='bar')
    test_bar.plot(kind='bar')


    # Multiple choice questions
    to_check = type_questions['grouped_questions']['yes_no'][0]
    freq_yes_test = count_unique_choice(df, to_check)
    freq_yes_test.sort_values(axis=0)
    freq_yes_test.plot(kind='bar')


    # Plot ranking



    # Calculate the counts for them
    # Likert scales

    # ## Single items

    # ## Several items









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
