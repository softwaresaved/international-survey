#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Config file for the cleaning - plotting and notebook process"""


class CleaningConfig:

    def __init__(self, year, country):
        self.country = country
        self.year = year
        if int(self.year) < 2018:
            # Unprocessed dataset
            self.raw_data = './{}/{}/data/raw_data.csv'.format(self.year, self.country)
            # load the different answers to questions to classify questions based on that
            self.question_file = './../survey_creation/{}/{}/questions.csv'.format(self.year, self.country)
            self.answer_folder = './../survey_creation/{}/{}/listAnswers'.format(self.year, self.country)
            # Location for the json file of all questions
            self.json_to_plot_location = './{}/{}/data/to_plot.json'.format(self.year, self.country)
            self.cleaned_df_location = './{}/{}/data/cleaned_data.csv'.format(self.year, self.country)
            self.public_df_location = './{}/{}/data/public_data.csv'.format(self.year, self.country)
        else:
            # Unprocessed dataset
            self.raw_data = './{}/data/raw_data.csv'.format(self.year)
            # load the different answers to questions to classify questions based on that
            self.question_file = './../survey_creation/{}/questions.csv'.format(self.year)
            self.answer_folder = './../survey_creation/{}/listAnswers'.format(self.year)
            # Location for the json file of all questions
            self.json_to_plot_location = './{}/data/to_plot.json'.format(self.year)
            self.cleaned_df_location = './{}/data/cleaned_data.csv'.format(self.year)
            self.public_df_location = './{}/data/public_data.csv'.format(self.year)
        self.section_nbr_to_keep_after = 1
        self.count_na = True
        self.normalise = False


class CountingConfig(CleaningConfig):

    def __init__(self, year, country):
        super().__init__(year, country)

        # Folder where to store the dataframe in a csv format
        self.folder_df = './{}/{}/output/'.format(self.year, self.country)


class PlottingConfig(CountingConfig):

    def __init__(self, year, country):
        super().__init__(year, country)
        self.plot_na = False
        self.normalise = True
        # Different than normalise, add a freq_table with percentage
        # in addition of the table with counts
        self.show_percent = True


class NotebookConfig(PlottingConfig):

    def __init__(self, year, country):
        super().__init__(year, country)
        self.notebook_filename = '{}_{}.ipynb'.format(self.country, self.year)
        self.notebook_html = '{}_{}.html'.format(self.country, self.year)
        self.allow_errors = True
        self.to_import = ['import pandas as pd',
                          'import numpy as np',
                          'import matplotlib',
                          'import matplotlib.pyplot as plt',
                          'from IPython.display import display',
                          'import IPython.core.display as di',
                          'from IPython.core.interactiveshell import InteractiveShell',
                          'from include.config import CleaningConfig, PlottingConfig, NotebookConfig',
                          'from include.counting import get_count, get_percentage',
                          'from include.plotting import get_plot, display_side_by_side',
                          'from include.likertScalePlot import likert_scale',
                          'from include.textCleaning import wordcloud']
        self.processing_options = {'metadata': {'path': './'}}
