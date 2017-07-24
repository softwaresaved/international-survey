#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from include.config import CleaningConfig, NotebookConfig
from include.cleaning import CleaningData
from include.generate_notebook import GenerateNotebook

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

    # Notebook writing
    notebook_location = '{}{}'.format(NotebookConfig.notebook_folder,
                                      NotebookConfig.notebook_filename)
    notebook = GenerateNotebook(notebook_location)

    for s in cleaning_process.structure_by_section:
        section = cleaning_process.structure_by_section[s]
        notebook.add_section(s)
        for group in section:
            notebook.add_group(group)
            for question in section[group]:
                list_questions = question['survey_q']
                original_question = question['original_question']
                answer_format = question['answer_format']
                file_answer = question['file_answer']
                for txt in original_question:
                    notebook.add_question_title(txt)
                if answer_format not in ['freetext', 'freenumeric', 'datetime', 'ranking']:
                    notebook.add_count(list_questions, answer_format, file_answer)
                    if NotebookConfig.show_percent is True and answer_format != 'likert':
                        notebook.add_percentage()
                        notebook.add_display_all()
                    else:
                        notebook.add_display_count()
                notebook.add_plot(answer_format)

    print('Running notebook')
    notebook.run_notebook()
    # Catching error before saving
    print('Saving notebook')
    notebook.save_notebook()


if __name__ == "__main__":
    main()
