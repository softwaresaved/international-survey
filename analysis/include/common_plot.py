#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Common functions shared among all the plotting type
"""

import matplotlib.pyplot as plt


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


def remove_top_right_line(ax):
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


def get_colors(df, colormap=None, vmin=None, vmax=None, axis=1):
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
    if colormap is None:
        colormap = plt.cm.RdBu
    if axis == 0:
        values = df.index
    elif axis == 1:
        values = df.columns
    norm = plt.Normalize(vmin, vmax)
    try:
        return colormap(norm(values))
    except (AttributeError, TypeError):  # May happen when gives a list of categorical values
        return colormap(norm(range(len(values))))


def set_legend(ax):
    """
    """
    pass


def main():
    """
    """
    pass


if __name__ == "__main__":
    main()
