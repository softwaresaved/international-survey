#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
from include.config import CountingConfig, NotebookConfig
from include.generate_notebook import GenerateNotebook
from include.get_arguments import get_arguments
import nbformat
from nbconvert import HTMLExporter
import codecs

"""
Action file that holds all the different configuration for a
specific dataset.

Import the specific cleaning and plotting methods that are
in the same folder
"""


def get_json_config_section(path_to_file):
    """
    A json file is created during the cleaning process
    it group all the different sections and questions together
    by type and is necessarily for this script to work. It is
    basically the questions.csv file but reorganised for the
    notebook script
    :params:
        :path_to_file str(): path to the json to load

    :return:
        :dict(): containing all the information about the questions
            regrouped by type
    """
    with open(path_to_file, 'r') as f:
        return json.load(f)


def main():

    pd.set_option('display.max_rows', 300)

    # Get which country and which year to create the analysis
    year, country = get_arguments(sys.argv[1:])
    notebook_config = NotebookConfig(year, country)

    # Get the folder to record df
    counting_config = CountingConfig(year, country)
    folder_df = counting_config.folder_df
    # Notebook writing
    notebook = GenerateNotebook(year, country, notebook_config.notebook_filename)
    notebook.output_total_participants()
    structure_by_section = get_json_config_section(notebook_config.json_to_plot_location)

    for s in structure_by_section:
        section = structure_by_section[s]
        notebook.add_section(s)
        for group in section:
            notebook.add_group(group)
            for question in section[group]:
                list_questions = question['survey_q']
                original_question = question['original_question']
                answer_format = question['answer_format']
                file_answer = question['file_answer']
                order_question = question['order_question']
                # To avoid having each questions written in a new line
                # it joins them together before writing it
                question_to_write = '; '.join(original_question)
                notebook.add_question_title(question_to_write)

                if answer_format not in ['freetext', 'datetime', 'freenumeric']:
                    notebook.add_count(list_questions, answer_format, file_answer, order_question,
                                       folder_df)
                    notebook.add_percentage()
                    notebook.add_display_all()
                    notebook.add_plot(answer_format)

                if answer_format == 'freetext':
                    notebook.add_wordcloud(list_questions)
                    # notebook.add_count(list_questions, answer_format, file_answer)
                    # notebook.add_plot(answer_format)

                if answer_format == 'freenumeric':
                    notebook.add_count(list_questions, answer_format, file_answer, order_question,
                                       folder_df)
                    notebook.add_plot(answer_format)

    print('Running notebook')
    notebook.run_notebook()
    print('Saving notebook')
    notebook.save_notebook()

    # # https://stackoverflow.com/questions/37657547/how-to-save-jupyter-notebook-to-html-by-code
    # print('Convert the notebook into an html file')
    # filepath = notebook_config.notebook_filename
    # # export_path = '{}/{}'.format(NotebookConfig.notebook_folder,
    # #                              NotebookConfig.notebook_html)
    #
    # with open(filepath) as fh:
    #     nb = nbformat.reads(fh.read(), as_version=4)
    #
    # exporter = HTMLExporter()
    #
    # # source is a tuple of python source code
    # # meta contains metadata
    # source, meta = exporter.from_notebook_node(nb)
    # codecs.open(filepath, 'w', encoding='utf-8').write(source)


if __name__ == "__main__":
    main()
