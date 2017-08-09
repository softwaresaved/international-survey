#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from nltk.corpus import stopwords
import string
import itertools
import numpy as np
from wordcloud import WordCloud, STOPWORDS

# to_remove = list(string.punctuation) + stopwords.words('english')
to_remove = set(string.punctuation) | STOPWORDS | set(['nan', np.NaN])


def clean_txt(txt):
    """
    Return cleaned text after removing punctuation and stopwords
    """
    return ' '.join([str(term) for term in txt if term not in to_remove])


def wordcloud(df, column):
    """
    """
    # TODO make a quicker way than that
    txt = list(itertools.chain.from_iterable(df[column].values))
    cleaned_txt = clean_txt(txt)
    return WordCloud(background_color='white', width=1500, height=800).generate(cleaned_txt)


if __name__ == "__main__":

    import pandas as pd
    import matplotlib
    # When using Ipython within vim
    matplotlib.use('TkAgg')

    # When using within jupyter
    # get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

    import matplotlib.pyplot as plt

    #  When using this script with ipython and vim
    plt.ion()
    df = pd.read_csv('../uk_2017/data/cleaned_data.csv')

    column = 'skill2[SQ001]. What skills would you like to acquire or improve to help your work as a Research Software Engineer? The skills can be technical and non-technical. [Skill 1]'
    plot_wordcloud = wordcloud(df, column)
    plt.imshow(plot_wordcloud, cmap=plt.cm.gray, interpolation="bilinear")

    plt.axis('off')
    plt.show()
