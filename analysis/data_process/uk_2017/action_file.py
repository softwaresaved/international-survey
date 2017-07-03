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

    for s in cleaning_process.structure_by_section:
        section = cleaning_process.structure_by_section[s]
        notebook.add_section(s)
        for question in section:
            original_question = section[question]['original_question']
            try:
                list_question = section[question]['survey_q']
                answer_format = section[question]['answer_format']
                file_answer = section[question]['file_answer']
                notebook.add_question_title(original_question)
                notebook.add_freq_table(list_question, answer_format)
                notebook.add_plot(question['survey_q'], answer_format, file_answer)
            except Exception:  #FIXME Need to record all exception in a separated logfile for further investigation
                pass
    print('Running notebook')
    notebook.run_notebook()
    # Catching error before saving
    print('Saving notebook')
    notebook.save_notebook()


if __name__ == "__main__":
    main()
