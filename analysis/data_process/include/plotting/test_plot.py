#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plotting bar chart
"""

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def freq_plotting(df, colnames='count', sort_order=False, stacked=False, horizontal=False, set_label=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :colname str(): string that have the column header to select the right column
    """

    def autolabel(barchart):

        for bar in barchart:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    if sort_order:
        df = df.sort_values(by=colnames, ascending=False)

    # Create the figure and the axis
    fig, ax = plt.subplots()

    # Get the x location of all the variable that have to be plotted on x-axis
    ind = np.arange(len(df.index))
    # The value of each bar on y-axis
    y_val = df[colnames]

    # The width of each individual bar
    width = 0.8
    bar_color = 'r'
    # Draw the barplot
    bar_plot = ax.bar(ind, y_val, width=width, color=bar_color, align='center')
    # bar_plot = ax.bar(ind, y_val, width=width, color=bar_color)

    if set_label is True:
        low = min(y_val)
        high = max(y_val)
        gap_label = 1.05

        # Set up the limits of the y-axis to taken into account the label added on each
        # bar and avoid having it being outside the plot
        # plt.ylim([math.ceil(low), math.ceil(high + 0.1 * (high))])
        # plt.ylim([math.ceil(low), math.ceil(high+(2*(gap_label-1))+(high))])
        # Add number on the bar
        autolabel(bar_plot)

    # Set the x ticks to be at the middle of each bar
    plt.xticks(ind)
    # Set the x labels
    ax.set_xticklabels(df.index)
    # Rotate the label horizontally to avoid overlapping
    plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='center')


def freq_plotting(df, colnames='count', sort_order=False, stacked=False, horizontal=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data, should be a df of frequencies
        created with crosstab
        :colname str(): string that have the column header to select the right column
    """
    type_plot = 'bar'
    if sort_order:
        df = df.sort_values(by=colnames, ascending=False)
    if horizontal is True:
        type_plot='barh'

    df[colnames].plot(kind=type_plot, stacked=stacked)


def main():
    """
    """
    pass


if __name__ == "__main__":
    main()
