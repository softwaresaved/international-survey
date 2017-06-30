#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import pandas as pd
import numpy as np

from config import CleaningConfig, PlottingConfig, NotebookConfig
from cleaning import CleaningData
from generate_notebook import GenerateNotebook

"""
Action file that holds all the different configuration for a
specific dataset.

Import the specific cleaning and plotting methods that are
in the same folder
"""



def main():
    pd.set_option('display.max_rows', 300)

    # Load dataset
    df = pd.read_csv(CleaningConfig.raw_data)

    # Cleaning_process
    cleaning_process = CleaningData(df)
    df = cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()

    # Plotting Process

    # Notebook writing
    notebook = GenerateNotebook(NotebookConfig.notebook_filename)

    for q in cleaning_process.survey_structure:
        question = cleaning_process.survey_structure[q]
        original_question = question['original_question']
        try:
            list_question = question['survey_q']
            notebook.add_question_title(original_question)
            print(question['survey_q'])
            notebook.add_freq_table(question['survey_q'], question['type_question'])
            notebook.add_plot(question['survey_q'], question['type_question'])
        except Exception:  #FIXME Need to record all exception in a separated logfile for further investigation
            pass
        # print(q['original_question'])
    print('Saving notebook')
    notebook.save_notebook()


if __name__ == "__main__":
    main()
