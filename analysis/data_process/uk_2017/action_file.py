#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import pandas as pd
import numpy as np

from config import CleaningConfig, PlottingConfig, NotebookConfig
from cleaning import CleaningData
from counting import get_count
from generate_notebook import GenerateNotebook

"""
Action file that holds all the different configuration for a
specific dataset.

Import the specific cleaning and plotting methods that are
in the same folder
"""


def group_and_split_q(group_question):
    """
    """
    regroup_q, regroup_txt_q = list(), list()
    previous_type = None
    for q in group_question:
        current_type = group_question[q]['answer_format'].lower()
        if previous_type is not None:
            if current_type != previous_type:
                yield regroup_q, regroup_txt_q, previous_type
                regroup_q, regroup_txt_q = list(), list()

        survey_q = group_question[q]['survey_q']
        original_q = group_question[q]['original_question']
        regroup_q.extend(survey_q)
        regroup_txt_q.append(original_q)
        previous_type = current_type

    yield regroup_q, regroup_txt_q, previous_type


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
        for group in section:
            # In that case, there is only one question in the group and
            # the list of question should be passed too the counting
            # and plotting directly
            # key_group = list(section[group].keys())[0]
            # original_question = section[group][key_group]['original_question']
            # notebook.add_question_title(original_question)
            notebook.add_group(group)
            for question in group_and_split_q(section[group]):
                list_questions = question[0]
                original_questions = question[1]
                answer_format = question[2]
                try:
                    notebook.add_count(list_questions, answer_format)
                    # notebook.add_freq_table(list_questions, answer_format)
                    # notebook.add_plot(counted_value, answer_format, file_answer)
                except KeyError:
                    print('Error for the question: {}'.format(original_question))

    print('Running notebook')
    notebook.run_notebook()
    # Catching error before saving
    print('Saving notebook')
    notebook.save_notebook()


if __name__ == "__main__":
    main()
