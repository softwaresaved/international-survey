#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Config file for the cleaning - plotting and notebook process"""


class CleaningConfig:

    raw_data = './dataset/raw_results-survey245554.csv'
    question_file = '../../../survey_creation/uk_17/uk_17.csv'
    answer_folder = '../../../survey_creation/uk_17/listAnswers'
    json_to_plot_location = './to_plot.json'
    cleaned_df_location = './dataset/cleaned_data.csv'


class PlottingConfig(CleaningConfig):

    pass


class NotebookConfig(PlottingConfig):

    pass
