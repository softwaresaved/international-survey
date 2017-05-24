# Load libraries
import pandas as pd
import numpy as np
import matplotlib
import math

# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt

#  When using this script with ipython and vim
plt.ion()
plt.show()

# Load dataset
df = pd.read_csv('./dataset/2017 Cdn Research Software Developer Survey - Public data.csv')
# Number of row == number of participants
len(df.index)

# ### Date submitted
# The variable 'Date submitted' is set up when the participant finish the survey. If the row on this column is empty, it means the participant did not finish the survey. These participants are removed, even if they have submitted partial answers.

df = df[df['Date submitted'].notnull()]
# Getting the number of row from the reduced dataframe
len(df.index)

def explore_other(colname, printUnique=False):
    """
    To output the unique value of the column
    and the column '[Other]' associated with it
    :params:
        :colnames str(): string to match the column
    :return: None
    """
    col_other = colname + ' [Other]'
    if printUnique is True:
        print('Unique values in the normal column')
        print(df[colname].unique())
        print('Unique values in the other columns')
        print(df[col_other].unique())
    return colname


def recode_values(x, replacement_values, default=False):
    """
    Function to use with an  apply on a Serie to replace values if they match
    the values from the dictionary passed into the argument.
    :params:
        :replacement_values dict(): K are the content to match and values the content
        to replace with
        :default: if a value is given to default, this value will be return, if it is
        false, the passed value is returned instead
    :return:
        :x: the x is returned or the replacement values if found in the dictionary or the
        default if not None.
    """
    if not pd.isnull(x):
        for k in replacement_values:
            if str(k).lower() in str(x).lower():
                return replacement_values[k]
        if default:
            return default
    return x


def merging_others(df, colname, replacement_values=None):
    """
    Function to wrap the different modification applied on
    the columns that have a `other` column associated.
    Only search if some others could be merged with the prexisting answers
    and merge it to into the original column, then transform the column into
    categorical variable
    :params:
        :df pd.df(): dataframe containing the data
        :colname str(): string that have the column header to select the right column
        :replacement_values dict(): contain which value to match in the column 'other' as
        the key and which value to replace with. If it is None, skip the transformation (Default)
    :return:
        :None: The operation is a replace `inplace`
    """
    colname_other = var+ ' [Other]'
    if replacement_values:
        df[colname_other] = df[colname_other].apply(recode_values, args=(replacement_values, 'Other'))
        df[colname].replace('Other', df[colname_other], inplace=True)

    df[colname] = df[colname].str.capitalize().astype('category')



def freq_table(df, colnames=False, columns='count'):
    """
    """
    return pd.crosstab(df[colnames], colnames=[''], columns=columns)


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



freq_plotting(disciplines, sort_order=True)

disciplines.index

var = explore_other('In which discipline is your highest academic qualification?')
discipline_values = {'bioinfo': 'Bioinformatics',
                     'computer': 'Information technology',
                     'informatique': 'Information technology',
                     'history': 'Social sciences and humanities',
                     'biophysics': 'Physics',
                     'software': 'Information and communication services',
                     'dance': 'Social Sciences and Humanities',
                     'musique': 'Social Sciences and Humanities',
                     'agric': 'Agricultural engineering'}
merging_others(df, var, discipline_values)
disciplines = freq_table(df, var)
disciplines

# Now the data is cleaned, it is possible to plot it
software_dev_number = freq_table(df, 'How many software developers typically work on your projects?')

# Reorganise the row names to match the normal order
software_dev_number = software_dev_number.reindex(['Just me', '2', '3-5',  '6-9', '10+'])
software_dev_number
freq_plotting(software_dev_number, sort_order=False, set_label=True)
