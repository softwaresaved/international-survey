# coding: utf-8
# /usr/bin/python
import pandas as pd
import numpy as np
import matplotlib

# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt
#  When using this script with ipython and vim
plt.ion()
plt.show()


"""
Plotting function to draw a likert scale.

To plot diverging horizontal barchart as needed for a likert scale
A simple code that try to mimic what it is possible with the package HH in R.
This script is an adaptation of the answers found:
    Source 1: http://stackoverflow.com/questions/23142358/create-a-diverging-stacked-bar-chart-in-matplotlib
    Source 2: http://stackoverflow.com/questions/21397549/stack-bar-plot-in-matplotlib-and-add-label-to-each-section-and-suggestions
"""


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


# TODO Simplify this function
def compute_percentage(df, by_row=True, by_col=False):
    """
    Transform every cell into a percentage
    """
    def compute_percentage(row, total=None):
        if total is None:
            total = np.sum(row)
        return [np.round(((x /total) *100), 2) for x in row]

    if by_row is True and by_col is False:
        return np.array(df.apply(compute_percentage, axis=1))

    elif by_col is True and by_row is False:
        return np.array(df.apply(compute_percentage, axis=0))

    elif by_row is True and by_col is True:
        total = df.values.sum()
        return np.array(df.apply(compute_percentage, total=total))


def create_bars(df, ax, y_pos, colors, left_invisible_bar):
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
        left_invisible_bar np.array(): the empty left gap needed to
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
                          left=left_invisible_bar)
        patch_handles.append(new_bar)
        # accumulate the left-hand offsets
        left_invisible_bar += d
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


def likert_scale(df, labels=True, middle_line=True, legend=True):
    """
    The idea is to create a fake bar on the left to center the bar on the same point.
    :params:
    :return:
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    # Generate an array of colors based on different colormap. The default value
    # Use a divergent colormap.
    colors = get_colors(df)
    y_pos = np.arange(len(df.index))

    # Compute the middle of the possible answers. Assuming the answers are columns
    # Get the sum of the middles +.5 if middle value and without .5 if splitted in 2
    # equal divides
    middles = get_total_mid_answers(df)
    longest = middles.max()

    # Create the left bar to centre the barchart in the middle
    left_invisible_bar = np.array((middles - longest).abs())
    # Calculate the longest bar with the left gap in it to plot the x_value at the end
    # Calculate the total of the longest bar to have the appropriate width
    complete_longest = (df.sum(axis=1) + left_invisible_bar).max()
    bars = create_bars(df, ax, y_pos, colors, left_invisible_bar)

    if labels:
        # Create percentage for each cells to have the right annotation
        percentages = compute_percentage(df)
        # go through all of the bar segments and annotate
        for j in range(len(bars)):
            for i, bar in enumerate(bars[j].get_children()):
                bl = bar.get_xy()
                x = 0.5 *bar.get_width() +bl[0]
                y = 0.5 *bar.get_height() +bl[1]
                ax.text(x, y, "%d%%" % (percentages[i, j]), ha='center')

    if middle_line:
        # Draw a dashed line on the middle to visualise it
        z = plt.axvline(longest, linestyle='--', color='black', alpha=.5)
        # Plot the line behind the barchart
        z.set_zorder(-1)

    if legend:
        pass

    # Set up the limit from 0 to the longest total barchart
    plt.xlim(0, complete_longest +.5)
    # Create the values with the same length as the xlim
    xvalues = range(0, int(complete_longest), 2)

    # Create label by using the absolute value of the
    xlabels = [str(abs(x - longest)) for x in xvalues]
    plt.xticks(xvalues, xlabels)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df.index)
    ax.set_xlabel('Distance')
    plt.show()


def main():
    """
    """
    def get_likert_score():

        # #### Generating the dataset for testing
        # Load dataset
        df = pd.read_csv('./dataset/2017 Cdn Research Software Developer Survey - Public data.csv')

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
                df_sub.columns = [s.split('[', 1)[1].split(']')[0] for s in colnames]

            # Calculate the counts for them
            df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
            # Transpose the column to row to be able to plot a stacked bar chart
            return df_sub.transpose()

        open_code_YN = ['When you release code, how often do you use an open source license?',
                        'When you release code or data, how often do you assign a Digital Object Identifier (DOI) to it?']

        count_open = df[open_code_YN].apply(pd.Series.value_counts, dropna=True).transpose()
        count_open = count_unique_value(df, open_code_YN, dropna=True)
        # Only likert values without the 'Prefer not to answer'
        likert_value = count_open.ix[:, count_open.columns != 'Prefer not to answer']
        return likert_value

    # Overload the data with a df type
    df = get_likert_score()
    likert_scale(df)

    dummy = pd.DataFrame([[1, 2, 3, 4, 5], [5, 6, 7, 8, 5], [10, 4, 2, 10, 5]],
                         columns=["SD", "D", "N", "A", "SA"],
                         index=["Key 1", "Key B", "Key III"])
    dummy.values.sum()
    compute_percentage(dummy, True, True)


if __name__ == "__main__":
    main()
