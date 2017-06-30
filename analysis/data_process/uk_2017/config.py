#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Config file for the cleaning - plotting and notebook process"""


class CleaningConfig:

    # Unprocessed dataset
    raw_data = './dataset/raw_results-survey245554.csv'
    # load the different answers to questions to classify questions based on that
    question_file = '../../../survey_creation/uk_17/uk_17.csv'
    answer_folder = '../../../survey_creation/uk_17/listAnswers'
    # Location for the json file of all questions
    json_to_plot_location = './to_plot.json'
    cleaned_df_location = './dataset/cleaned_data.csv'
    # If the data input in the cleaning class are structured according to the csv file
    structured = True


class PlottingConfig(CleaningConfig):

    pass


class NotebookConfig(PlottingConfig):

    root_folder = './uk_2017'
    notebook_filename = '../uk_17.ipynb'
    to_import = ['import pandas as pd',
                 'import numpy as np',
                 'get_ipython().magic("matplotlib inline")',
                 'import matplotlib',
                 'import matplotlib.pyplot as plt',
                 'from uk_2017.config import CleaningConfig, PlottingConfig, NotebookConfig',
                 'from uk_2017.frequency import freq_choose'
                 'from uk_2017.plotting import plot_choose']
