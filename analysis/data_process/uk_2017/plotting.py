#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import csv
import json
import glob
import pandas as pd
import numpy as np
import matplotlib
# from include import plotting
# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt
#  When using this script with ipython and vim
plt.ion()
plt.show()
pd.set_option('display.max_rows', 300)


def get_type_question(input_location):
    """
    """
    with open(input_location, 'r') as f:
        return json.load(f)

def main():

    # load the dataframe
    df = pd.read_csv('./dataset/cleaned_data.csv')
    location_type_q = './to_plot.json'
    type_questions = get_type_question(location_type_q)
    type_questions['grouped_questions']['bus_factor']

if __name__ == "__main__":
    main()
