#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import csv
import json
import glob
import pandas as pd
import numpy as np

from config import CleaningConfig
from cleaning import CleaningData
import generate_notebook
import plotting

"""
Action file that holds all the different configuration for a
specific dataset.

Import the specific cleaning and plotting methods that are
in the same folder
"""



def main():
    import matplotlib
    # from include import plotting
    # When using Ipython within vim
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    #  When using this script with ipython and vim
    plt.ion()
    plt.show()
    pd.set_option('display.max_rows', 300)

    # Load dataset
    df = pd.read_csv(CleaningConfig.raw_data)
    cleaning_process = CleaningData(df)
    cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()
    for q in cleaning_process.survey_structure:
        print(cleaning_process.survey_structure[q]['original_question'])
        # print(q['original_question'])



if __name__ == "__main__":
    main()
