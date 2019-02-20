#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plotting function to draw a likert scale.

To plot diverging horizontal barchart as needed for a likert scale
A simple code that try to mimic what it is possible with the package HH in R.
This script is an adaptation of the answers found:
 http://stackoverflow.com/questions/23142358/create-a-diverging-stacked-bar-chart-in-matplotlib
 http://stackoverflow.com/questions/21397549/stack-bar-plot-in-matplotlib-and-add-label-to-each-section-and-suggestions
"""

__author__ = 'Olivier PHILIPPE'
__licence__ = 'BSD 3-clause'

import math
import pandas as pd
import numpy as np

# When using Ipython within vim
# matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter


import matplotlib.pyplot as plt
#  When using this script with ipython and vim
plt.ion()
plt.show()


def get_colors(df, colormap=plt.cm.RdBu, vmin=None, vmax=None, axis=1):
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
    if axis == 0:
        values = df.index
    elif axis == 1:
        values = df.columns
    norm = plt.Normalize(vmin, vmax)
    try:
        return colormap(norm(values))
    except (AttributeError, TypeError):  # May happen when gives a list of categorical values
        return colormap(norm(range(len(values))))


def wrap_labels(label, max_size=30):
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


def create_bars(df, ax, y_pos, colors, left_gap):
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
        new_bar = ax.barh(y_pos,
                          d,
                          color=colors[i],
                          align='center',
                          left=left_gap)
        patch_handles.append(new_bar)
        # accumulate the left-hand offsets
        left_gap += d
    return patch_handles


def compute_middle_sum(df, first_half, middle):
    try:
        return df[first_half].sum(axis=1) + df[middle] *.5
    except ValueError:  # In case middle value is none
        return df[first_half].sum(axis=1)


def get_middle(inputlist):
    """
    Return the first half of a list and the middle element
    In case the list can be splitted in two equal element,
    return only the first half
    :params:
        inputlist list(): list to split
    :returns:
        first_half list(): list of the first half element
        middle_elmenet int():
    """
    middle = float(len(inputlist) /2)
    if len(inputlist) % 2 !=0:
        # If the list has a true middle element it needs
        # to be accessed by adding 0.5 to the index
        middle = int(middle + 0.5) - 1
        # In the case of a true middle is found, the first half
        # is all elements except the middle
        first_half = middle
        return inputlist[middle], inputlist[0:first_half]
    # In case of not true middle can be found (in case the
    # list has a lenght of an even number, it can only
    # return the first half. The middle value is None
    return None, inputlist[:int(middle)]


def get_total_mid_answers(df):
    """
    Get the list of the columns
    """
    middle, first_half = get_middle(df.columns)
    return compute_middle_sum(df, first_half, middle)


def compute_percentage(df, by_row=True, by_col=False):
    """
    Transform every cell into a percentage
    """
    def compute_perc(row, total=None):
        if total is None:
            total = np.sum(row)
        return [((x /total) *100) for x in row]

    if by_row is True and by_col is False:
        return np.array(df.apply(compute_perc, axis=1))

    elif by_col is True and by_row is False:
        return np.array(df.apply(compute_perc, axis=0))

    elif by_row is True and by_col is True:
        total = df.values.sum()
        return np.array(df.apply(compute_perc, total=total))


def normalise_per_row(df):
    df = df.div(df.sum(axis=1), axis=0)
    return df.multiply(100)


def add_labels(df, ax, bars, rotation=0, rounding=True):
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
            # Avoid labels when percentage is under 5 (the bar is too small)
            if percentages[i][j] > 5:
                if rounding is True:
                    ax.text(x, y, "{}".format(str(int(round(percentages[i][j])))), ha='center', rotation=rotation)
                else:
                    ax.text(x, y, "{}".format(percentages[i][j]), ha='center', rotation=rotation)


def draw_middle_line(ax, normalise, longest_middle):
    """
    """
    # Draw a dashed line on the middle to visualise it
    if normalise:
        z = ax.axvline(100, linestyle='--', color='black', alpha=.5)
    else:
        z = ax.axvline(longest_middle, linestyle='--', color='black', alpha=.5)
    # Plot the line behind the barchart
    z.set_zorder(-1)


def drawing_x_labels(ax, normalise, complete_longest, longest_middle):
    """
    """
    # Create the values with the same length as the xlim
    if normalise:
        xvalues = range(0, 210, 10)
        xlabels = [str(math.floor(abs(x - 100))) for x in xvalues]
    else:
        xvalues = [math.floor(i - (longest_middle %5))
                   for i in range(0, int(complete_longest),
                                  int(int(longest_middle)/ 5))]
        xlabels = [str(math.floor(abs(x - longest_middle))) for x in xvalues]
    # Set the tick positions
    ax.set_xticks(xvalues)
    # Set the tick labels
    ax.set_xticklabels(xlabels)


def likert_scale(df, ax=None, normalise=True, labels=True, middle_line=True, legend=True, rotation=0, title_plot=False, rounding=True):
    """
    The idea is to create a fake bar on the left to center the bar on the same point.
    :params:
    :return:
    """
    # Replace the Nan value by 0 for plotting
    df = df.fillna(0)
    try:
        # Create the figure object
        # if figsize is None:
        #     fig = plt.figure(figsize=(10, 8))
        # else:
        #     fig = plt.figure(figsize=figsize)
        # # Create an axes object in the figure
        # ax = fig.add_subplot(111)
        # fig, ax = plt.subplots()
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1) # make a blank plotting area

        # Generate an array of colors based on different colormap. The default value
        # Use a divergent colormap.
        colors = get_colors(df)

        # Get the position of each bar for all the items
        y_pos = np.arange(len(df.index))

        if normalise:
            df = normalise_per_row(df)

        # Compute the middle of the possible answers. Assuming the answers are columns
        # Get the sum of the middles +.5 if middle value and without .5 if splitted in 2
        # equal divides
        middles = get_total_mid_answers(df)

        # Calculate the longest middle bar to set up the middle of the x-axis for the x-lables
        # and plot the middle line
        if normalise:
            longest_middle = 100
        else:
            longest_middle = middles.max()

        # Create the left bar to centre the barchart in the middle
        left_invisible_bar = np.array((middles - longest_middle).abs())

        # Calculate the longest bar with the left gap in it to plot the x_value at the end
        # Calculate the total of the longest bar to have the appropriate width +
        # the invisible bar in case it is used to center everything
        complete_longest = (df.sum(axis=1) + left_invisible_bar).max()

        # Create the horizontal bars
        bars = create_bars(df, ax, y_pos, colors, left_invisible_bar)

        # Set up the limit from 0 to the longest total barchart
        # Keeping this drawing before drawing_x_labels or it will failed to draw
        # all the labels on the right side
        ax.set_xlim([-0.5, complete_longest + 0.5])

        # Drawing x_labels
        drawing_x_labels(ax, normalise, complete_longest, longest_middle)
        ax.set_xlabel('Percentage')

        # Setting up the y-axis
        ax.set_yticks(y_pos)
        ax.set_yticklabels([wrap_labels(labels) for labels in df.index], fontsize=14)

        # Add labels to each box
        if labels:
            add_labels(df, ax, bars, rotation, rounding=rounding)

        # Create a line on the middle
        if middle_line:
            draw_middle_line(ax, normalise, longest_middle)

        # Add legend
        if legend:
            ax.legend(bars, df.columns, fontsize=14)

        # Change the plot title
        if title_plot:
            plt.suptitle(title_plot)
        return ax
    except Exception:
        raise


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
    df_sub = df[colnames]

    if rename_columns is True:
        df_sub.columns = [s.split('[')[2][:-1] for s in colnames]

    # Calculate the counts for them
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    # Transpose the column to row to be able to plot a stacked bar chart
    return df_sub.transpose()


def main():
    """
    """

    # df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=list('XYZ'))
    dummy = pd.DataFrame([[1, 2, 3, 4, 5, 2], [5, 6, 7, 8, 5, 2], [10, 4, 2, 10, 5, 2]],
                         columns=["SD", "D", "N", "A", "SA", 'TEST'],
                         index=["Key 1", "Key B", "Key III"])
    #
    # dummy = pd.DataFrame([[1], [2], [3]],
    #                      columns=['TEST'],
    #                      index=['Key1', 'Key2', 'Key3'])

    likert_scale(dummy)


if __name__ == "__main__":
    main()
