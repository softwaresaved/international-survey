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


class PlottingConfig(CleaningConfig):
    count_na = True
    plot_na = False
    normalise = False


class NotebookConfig(PlottingConfig):

    notebook_folder = './'
    notebook_filename = 'uk_17.ipynb'
    to_import = ['import pandas as pd',
                 'import numpy as np',
                 'import matplotlib',
                 'import matplotlib.pyplot as plt',
                 'from config import CleaningConfig, PlottingConfig, NotebookConfig',
                 'from counting import get_count',
                 'from plotting import get_plot',
                 'from IPython.display import display',
                 'from likertScalePlot import likert_scale']
    processing_options = {'metadata': {'path': './',
                                       'hide_input': True}}
