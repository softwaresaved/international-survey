#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string
import itertools
import numpy as np
from wordcloud import WordCloud, STOPWORDS

to_remove = set(string.punctuation) | STOPWORDS | set(['nan', np.NaN])


def clean_column(df, column):
    """
    Function to return clean column text. Pass each cell to a cleaner
    and return the cleaned text for that specific column

    :params:
    --------
        :df dataframe(): containing the column
        :column str(): in which column the text is located

    :returns:
    ---------
        :list(): of str containing the cleaned text
    """

    # Remove all the NaN values and transform it into a list
    return list(df[column].dropna().values)


def split_within(txt_list, separators=[',', ';', '/']):
    """
    Take a list of text and separate each entry based on the
    separators and return a flatten list

    :params:
    --------
        :txt_list list(): of string to split
        :separators list(): of string to use to split each entry

    :return:
    --------
        :to_return list(): of all elements
    """
    to_return = list()

    for i in txt_list:
        for sep in separators:
            i = str(i).replace(sep, '___')
        splitted_i = [el for el in i.split('___')]
        for el in splitted_i:
            to_return.append(el)
    return to_return


def remove_punctuation(txt):
    """
    Use the list of punctuation given with wordcloud to remove it from the text

    :params:
    --------
        txt list(): of string that need to have punctuation removed

    :return:
    --------
        to_return list(): of strings with punctuation removed
    """
    to_return = list()
    for entry in txt:
        to_return.append(''.join([str(term) for term in entry if term not in set(string.punctuation)]))

    return to_return


def remove_white_space(txt_list):
    """
    Remove unwanted white space and replaced them with single white space

    params:
    -------
        txt_list list(): of str() that contains the text to clean

    :return:
    --------
        txt_list list(): of str() transformed
    """
    return [" ".join(txt.split()) for txt in txt_list]


def remove_only_numeric(txt):
    def remove_digit(word):
        return ''.join([w for w in word if not w.isdigit()])
    to_return = list()
    for entry in txt:
        to_return.append(' '.join([remove_digit(word) for word in entry.split(' ') if not word.isdigit()]))
    return to_return


def remove_empty_entry(txt_list):
    return [txt for txt in txt_list if len(txt) >2]


def keep_acronyme(txt):
    """
    """
    dict_acro = dict()
    for entry in txt:
        # Often acronyme of the conference are wrote under bracket
            # acronyme, rest_of_sentence =
            # print(entry)
        regex = re.compile(".*?\((.*?)\)")
        test = re.findall(regex, entry)
        print(test)


            # print(acronyme, rest_of_sentence)

        # # if work.isupper():
        #     dict_acro[word] = dict_acro.get(word, []).append(remaining)
        #     return word
        # else:
        #     return word.title()
    return txt

def link_words(txt):

    to_return = list()
    for entry in txt:
        to_return.append(entry.replace(' ', '_'))
    return to_return



def wrap_clean_text(df, columns, conference=False, skills=False):
    """
    """
    text_list = clean_column(df, columns)
    cleaned_text = split_within(text_list)

    cleaned_text = remove_punctuation(cleaned_text)
    cleaned_text = remove_white_space(cleaned_text)
    cleaned_text = remove_empty_entry(cleaned_text)
    if conference:
        cleaned_text = remove_only_numeric(cleaned_text)
        cleaned_text = keep_acronyme(cleaned_text)
    if skills:
        pass
    cleaned_text = link_words(cleaned_text)
    return cleaned_text


def plot_wordcloud(text_to_plot):
    """
    """
    # The width and the height match the comfiguration in generate_notebook for the size
    # of the plot width=15.0, height=8.0 inch with 100 DPI. be careful not changning these
    # value without modifying the corresponding value in _setup_matplotlib() in generate_notebook.py
    if isinstance(text_to_plot, list):
        text_to_plot = ' '.join(text_to_plot)
    return WordCloud(background_color='white', width=1500, height=800).generate(text_to_plot)


if __name__ == "__main__":

    import pandas as pd
    import matplotlib
    # When using Ipython within vim
    matplotlib.use('TkAgg')

    # When using within jupyter
    # get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

    import matplotlib.pyplot as plt

    #  When using this script with ipython and vdf = pd.read_csv('../uk_2017/data/cleaned_data.csv')

    df = pd.read_csv('../2018/data/clean_merged.csv')
    column = 'conf2can. At which conference(s)/workshop(s) have you presented your software work?'
    column2 = 'ukrse3. How did you learn the skills you need to become an Research Software Engineer / Research Software Developer?'

    cleaned_text = wrap_clean_text(df, column2, conference=True)

    # for i in cleaned_text:
    #     print(i)
    print('Size of all: {}'.format(len(cleaned_text)))
    print('Size of unique: {}'.format(len(set(cleaned_text))))
    plt.imshow(plot_wordcloud(cleaned_text), cmap=plt.cm.gray, interpolation="bilinear")

    plt.axis('off')
    plt.show()
