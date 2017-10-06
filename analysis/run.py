#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getopt
import pandas as pd
from include.config import CleaningConfig, CountingConfig, NotebookConfig
from include.preprocessing import CleaningData
from include.generate_notebook import GenerateNotebook
import nbformat
from nbconvert import HTMLExporter
import codecs

"""
Action file that holds all the different configuration for a
specific dataset.

Import the specific cleaning and plotting methods that are
in the same folder
"""


def get_arguments(argv):
    """
    """
    country = None
    year = None
    try:
        opts, args = getopt.getopt(argv, 'hc:y:', ['country=', 'year='])
    except getopt.GetoptError:
        print('run.py -c <country> -y <year>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('run.py -c <country> -y <year>')
            sys.exit()
        elif opt in ('-c', '--country'):
            country = arg
        elif opt in ('-y', '--year'):
            year = arg
    if country and year:
        return country, year
    else:
        print('Need a country and a year. Please use the following command:\n' +
              '\trun.py -c <country> -y <year>')
        sys.exit(2)

def main():

    pd.set_option('display.max_rows', 300)

    # Get which country and which year to create the analysis
    country, year = get_arguments(sys.argv[1:])

    # Getting the different location files from the config file and
    folder = '{}_{}'.format(year, country)


    # Load dataset
    df = pd.read_csv(CleaningConfig.raw_data)

    # Cleaning_process
    cleaning_process = CleaningData(df)
    df = cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()

    # Get the folder to record df
    folder_df = CountingConfig.folder_df
    # Notebook writing
    notebook_location = '{}{}'.format(NotebookConfig.notebook_folder,
                                      NotebookConfig.notebook_filename)
    notebook = GenerateNotebook(notebook_location)
    notebook.output_total_participants()
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
                order_question = question['order_question']
                # To avoid having each questions written in a new line
                # it joins them together before writing it
                question_to_write = '; '.join(original_question)
                notebook.add_question_title(question_to_write)
                # for txt in original_question:
                #     # notebook.add_question_title(txt)

                if answer_format not in ['freetext', 'datetime', 'freenumeric']:
                    notebook.add_count(list_questions, answer_format, file_answer, order_question,
                                       folder_df)
                    # Need to specify != likert because if likert item == 1 it uses the barchart
                    # and will plot the percentages even if it doesn't make sense to do that for
                    # a likert scale
                    if NotebookConfig.show_percent is True and answer_format != 'likert':
                        notebook.add_percentage()
                        notebook.add_display_all()
                    else:
                        notebook.add_display_count()
                    notebook.add_plot(answer_format)

                if answer_format == 'freetext':
                    notebook.add_wordcloud(list_questions)
                    # notebook.add_count(list_questions, answer_format, file_answer)
                    # notebook.add_plot(answer_format)

                if answer_format == 'freenumeric':
                    notebook.add_count(list_questions, answer_format, file_answer, order_question,
                                       folder_df)
                    notebook.add_plot(answer_format)

                # if answer_format == 'ranking':
                #     notebook.add_count(list_questions, answer_format, file_answer, order_question,
                #                        folder_df)
                #     notebook.add_percentage()
                #     notebook.add_display_percentage()
                #     notebook.add_plot(answer_format)

    print('Running notebook')
    notebook.run_notebook()
    print('Saving notebook')
    notebook.save_notebook()

    # https://stackoverflow.com/questions/37657547/how-to-save-jupyter-notebook-to-html-by-code
    print('Convert the notebook into an html file')
    filepath = notebook_location
    export_path = '{}/{}'.format(NotebookConfig.notebook_folder,
                                 NotebookConfig.notebook_html)

    with open(filepath) as fh:
        nb = nbformat.reads(fh.read(), as_version=4)

    exporter = HTMLExporter()

    # source is a tuple of python source code
    # meta contains metadata
    source, meta = exporter.from_notebook_node(nb)
    codecs.open(export_path, 'w', encoding='utf-8').write(source)


if __name__ == "__main__":
    main()
