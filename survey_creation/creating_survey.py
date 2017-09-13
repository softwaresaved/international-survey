#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Olivier Philippe'


"""
Limesurvey offers the possibility to import/export a TSV file containing all the information
of the survey structure. Using this possibility, this script aims to translate the files used
by the different groups to creates their survey, into a compatible TSV file.
It take only the argument of the folder where all the information is stored, and create a new
compatible file.
All information about the TSV file structure can be retrieved here:
    https://manual.limesurvey.org/Tab_Separated_Value_survey_structure
"""

import csv
import sys
import os
from collections import OrderedDict
from include.logger import logger
from config.config import creationConfig as main_config
import importlib
from random import shuffle
from markdown import markdown

RUNNING = 'dev'

if RUNNING == 'dev':
    DEBUGGING='DEBUG'
elif RUNNING == 'prod':
    DEBUGGING='INFO'

logger = logger(name='creating survey', stream_level=DEBUGGING)


def import_config(folder):
    """
    Import the config file associated with the folder name
    """
    module = 'config.{}'.format(folder)
    return importlib.import_module(module).config()


def create_empty_row():
    """
    Create an Ordered dictionary to be used to translate csv file to tsv
    """
    return OrderedDict((k, '') for k in main_config.main_headers)


def init_outfile(folder):
    """
    Rewrite over the existing file to avoid issue of appending and
    return the path to the file
    """
    outfile_name = folder + '_to_import.txt'
    outfile = os.path.join(folder, outfile_name)
    with open(outfile, 'w') as f:
        w = csv.DictWriter(f, delimiter='\t',
                           lineterminator='\n',
                           quotechar='"',
                           fieldnames=main_config.main_headers)
        w.writeheader()
    return outfile


def read_survey_file(folder):
    """
    Read the survey csv file and yield each line as a dictionary
    """
    question_file = os.path.join(folder, '.'.join([folder, 'csv']))
    with open(question_file, 'r') as f:
        csv_f = csv.DictReader(f)
        for row in csv_f:
            yield row


def write_row_outfile(outfile, row):
    """
    """
    with open(outfile, 'a') as f:
        w = csv.DictWriter(f, delimiter='\t',
                           lineterminator='\n',
                           quotechar='"',
                           fieldnames=main_config.main_headers)
        w.writerow(row)


def to_modify(original_list, modified_list):
    """
    """
    return_list = list()
    for element in original_list:
        replaced = False
        for e in modified_list:
            if element['name'] == e['name']:
                return_list.append(e)
                replaced = True
                break
        if replaced is False:
            return_list.append(element)
    return return_list


def to_add(original_list, list_to_add):
    """
    """
    for obj in list_to_add:
        original_list.insert(obj[1], obj[0])
    return original_list


def create_header(main_config, specific_config):
    """
    """
    good_parameters = to_modify(main_config.global_headers, specific_config.header_to_modify)
    good_parameters = to_add(main_config.global_headers, specific_config.header_to_add)
    return good_parameters


def add_from_list(outfile, list_to_copy):
    """
    """
    for element in list_to_copy:
        row = create_empty_row()
        row.update(element)
        write_row_outfile(outfile, row)


def get_text(folder, type_message, lang=None):
    """
    """
    if lang and lang != 'en':
        filename = '{}_message_{}.md'.format(type_message, lang)
    else:
        filename = '{}_message.md'.format(type_message)

    folder = os.path.join(folder, 'texts')
    path = os.path.join(folder, filename)
    with open(path, 'r') as f:
        return markdown(f.read())


def add_text_message(full_list, message, type_message):
    """
    """
    return_list = list()
    message_done = False
    for element in full_list:
        if message_done is False:
            if element['name'] == 'surveyls_welcometext' and type_message == 'welcome':
                message_done = True
                element['text'] = message
            elif element['name'] == 'surveyls_endtext' and type_message == 'welcome':
                message_done = True
                element['text'] = message
        return_list.append(element)
    return return_list


def create_description(main_config, specific_config, welcome_message, end_message, lang):
    """
    """
    good_description = to_modify(main_config.global_description, specific_config.description_to_modify)
    good_description = to_add(main_config.global_description, specific_config.description_to_add)
    survey_title = specific_config.survey_title[lang]
    survey_title_row = {'class': 'SL', 'name': 'surveyls_title', 'text': survey_title}
    good_description.insert(0, survey_title_row)

    to_return = list()
    for d in good_description:
        d['language'] = lang
        to_return.append(d)
    to_return = add_text_message(to_return, welcome_message, 'welcome')
    to_return = add_text_message(to_return, end_message, 'end')

    return to_return


def get_answer(folder, file_answer):
    """
    """
    outfile = os.path.join(folder, 'listAnswers', '{}.csv'.format(file_answer))
    with open(outfile, 'r') as f:
        return [x[:-1] for x in f.readlines()]


def group_likert(indict):
    """
    Take the dictionary of all the questions and group them
    into the same group if they have to be displayed together.
    Only applicable for the type_question Y/N/NA and the likert ones
    """
    previous_answer_format = None
    previous_file_answer = None
    previous_code = None
    previous_file_answer = None
    group_survey_q = list()
    for q in indict:
        current_answer_format = q['answer_format'].lower()
        current_file_answer = q['answer_file']
        current_code = ''.join([i for i in q['code'] if not i.isdigit()])

        if current_answer_format == 'likert':
            if len(group_survey_q) > 0:
                if current_file_answer == previous_file_answer or previous_file_answer is None:
                    if previous_answer_format == 'likert':
                        pass
                    else:
                        yield group_survey_q
                        group_survey_q = list()
                else:
                    yield group_survey_q
                    group_survey_q = list()

        elif current_answer_format == 'y/n/na':
            if len(group_survey_q) > 0:
                if current_code == previous_code or previous_code is None:
                    if previous_answer_format == 'y/n/na':
                        pass
                    else:
                        yield group_survey_q
                        group_survey_q = list()
                else:
                    yield group_survey_q
                    group_survey_q = list()

        else:
            if len(group_survey_q) > 0:
                yield group_survey_q
            group_survey_q = list()
        group_survey_q.append(q)
        previous_answer_format = current_answer_format
        previous_file_answer = current_file_answer
        previous_code = current_code

    yield group_survey_q


def check_adding_section(row, nbr_section, default_row, lang, writing_function, outfile):
    write_row_outfile = writing_function
    if int(row['section']) - 1 != nbr_section:
        # -1 because the section numbers starts at 0 but
        # in the csv survey_file it starts at 1
        nbr_section = int(row['section']) - 1
        section = main_config.group_format
        # type/scale are like 'G0', 'G1', etc.
        section['type/scale'] = 'G' + str(nbr_section)
        section['language'] = lang
        section.update(default_row[nbr_section][lang])
        write_row_outfile(outfile, section)
    return nbr_section


def main():
    # Get which survey
    folder = sys.argv[1]

    # Import specific config file
    specific_config = import_config(folder)

    # Init an empty survey file
    outfile = init_outfile(folder)

    # Create a copy the header to the empty file
    config_header = create_header(main_config, specific_config)

    # Record the copy into the file
    add_from_list(outfile, config_header)

    # Get the languages
    languages = main_config.languages
    languages.append(specific_config.languages_to_add)



    # Now create the header for each languages
    for lang in languages:
        # Get the welcome message
        welcome_message = get_text(folder, 'welcome', lang)

        # Get the end message
        end_message = get_text(folder, 'end', lang)
        # Create the description
        config_description = create_description(main_config, specific_config,
                                                welcome_message, end_message, lang)

        # Copy the description to the header
        add_from_list(outfile, config_description)

    # Create the questions for each languages, everything has to be done each time
    # the enumerate helps for finding the right answer and the right lang_trans
    # in case of more than one translation
    for index_lang, lang in enumerate(languages):
        # Speficify where to find the text for the question
        if lang != 'en':
            txt_lang = 'lang_trans' + str(index_lang)
        else:
            txt_lang = 'question'
        # Add a first section
        nbr_section = -1
        nbr_section = check_adding_section({'section': 0}, nbr_section, specific_config.sections_txt,
                                        lang, write_row_outfile, outfile)

        # Need this variable to inc each time a new multiple questions is created to ensure they are unique
        # only used in the case of likert and y/n/na merged together
        code_to_multiple_question = 0

        # Open the csv file and read it through a dictionary (generator)
        question_to_transform = read_survey_file(folder)
        # pass this generator into the function group_likert() to group Y/N and likert together
        for q in group_likert(question_to_transform):
            # If questions were grouped together, need to change how it is process
            if len(q) > 1:
                # Check if a new section needs to be added before processing the question
                nbr_section = check_adding_section(q[0], nbr_section, specific_config.sections_txt,
                                                lang, write_row_outfile, outfile)
                # Check if the list of items need to be randomize
                # if it is the case, just use shuffle to shuffle the list in-place
                if q[0]['random'] == 'Y':
                    pass
                    # shuffle(q)

                if q[0]['answer_format'].lower() == 'likert':
                    # Create the question header that needs to be created once for all the
                    # following question

                    question = main_config.likert_question
                    question['name'] = 'likert' + str(code_to_multiple_question)
                    # question['text'] = ''
                    question['language'] = lang
                    question['other'] = 'N'
                    code_to_multiple_question +=1
                    write_row_outfile(outfile, question)

                    for row in q:
                        subquestion = main_config.likert_subquestion
                        subquestion['relevance'] = '1'
                        subquestion['language'] = lang
                        subquestion['name'] = row['code']
                        question['text'] = row[txt_lang]
                        write_row_outfile(outfile, subquestion)

                    # add the answers
                    # create an inc to add to the question code. they need unique label
                    n = 1
                    for text_answer in get_answer(folder, q[0]['answer_file']):
                        answer_row = main_config.one_choice_answer
                        answer_row['name'] = str(n)
                        answer_row['text'] = text_answer.split(';')[0].strip('"')
                        answer_row['language'] = lang

                elif q[0]['answer_format'].lower() == 'y/n/na':
                    pass

            else:
                for row in q:
                    # Check if a new section needs to be added before processing the question
                    nbr_section = check_adding_section(row, nbr_section, specific_config.sections_txt,
                                                       lang, write_row_outfile, outfile)

                    if row['answer_format'].lower() == 'one choice':
                        # Create the question
                        question = main_config.one_choice_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        if row['other'] == 'Y':
                            question['other'] = 'Y'
                        else:
                            question['other'] = 'N'
                        write_row_outfile(outfile, question)
                        # add the answers
                        # create an inc to add to the question code. they need unique label
                        n = 1
                        for text_answer in get_answer(folder, row['answer_file']):
                            answer_row = main_config.one_choice_answer
                            # answer_row['name'] = 'A' + str(n)
                            answer_row['name'] = str(n)
                            try:
                                answer_row['text'] = text_answer.split(';')[index_lang].strip('"')
                            except IndexError:
                                print(row['code'])
                                answer_row['text'] = text_answer.split(';')[0].strip('"')
                            answer_row['language'] = lang
                            write_row_outfile(outfile, answer_row)
                            n +=1

                    if row['answer_format'].lower() == 'ranking':
                        # Ranking questions work differently
                        # First a list of rank SQ class need to be created (max 8 here)
                        # Then only the questions are created
                        # As neither of them have specific value for database, they are
                        # created here and not pulled from the config file
                        question = main_config.ranking_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        write_row_outfile(outfile, question)
                        # Create the Subquestion ranks
                        for i in range(1, 9):  # To get 8 ranked questions
                            init_row = {'class': 'SQ', 'type/scale': '0', 'name': str(i), 'relevance': '1',
                                        'text': 'Rank ' + str(i), 'language': lang}
                            write_row_outfile(outfile, init_row)

                        n = 1
                        for text_answer in get_answer(folder, row['answer_file']):
                            answer_row = main_config.ranking_answer
                            answer_row['name'] = str(n)
                            answer_row['text'] = text_answer.split(';')[index_lang].strip('"')
                            answer_row['language'] = lang
                            write_row_outfile(outfile, answer_row)
                            n +=1

                    if row['answer_format'].lower() == 'multiple choices':
                        question = main_config.multiple_choice_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        # question['validation'] = lang
                        if row['other'] == 'Y':
                            question['other'] = 'Y'
                        else:
                            question['other'] = 'N'
                        write_row_outfile(outfile, question)
                        # Add the answers
                        # Create an inc to add to the question code. They need unique label
                        n = 1
                        for text_answer in get_answer(folder, row['answer_file']):
                            answer_row = main_config.multiple_choice_answer
                            answer_row['name'] = str(n)
                            answer_row['text'] = text_answer.split(';')[index_lang].strip('"')
                            answer_row['language'] = lang
                            write_row_outfile(outfile, answer_row)
                            n +=1

                    if row['answer_format'].lower() == 'freenumeric':
                        question = main_config.freenumeric_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        # question['validation'] = lang
                        question['other'] = 'N'
                        write_row_outfile(outfile, question)

                    if row['answer_format'].lower() == 'freetext':
                        question = main_config.freetext_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        question['other'] = 'N'
                        write_row_outfile(outfile, question)

                    if row['answer_format'].lower() == 'likert':
                        question = main_config.likert_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        question['other'] = 'N'
                        write_row_outfile(outfile, question)
                        # Need to create an  empty subquestion
                        subquestion = {'class': 'SQ', 'type/scale': '0',
                                    'name': 'SQ001'}
                        subquestion['relevance'] = '1'
                        subquestion['language'] = lang
                        write_row_outfile(outfile, subquestion)

                        # Add the answers
                        # Create an inc to add to the question code. They need unique label
                        n = 1
                        for text_answer in get_answer(folder, row['answer_file']):
                            answer_row = main_config.likert_answer
                            answer_row['name'] = str(n)
                            answer_row['text'] = text_answer.split(';')[index_lang].strip('"')
                            answer_row['language'] = lang
                            write_row_outfile(outfile, answer_row)
                            n +=1

                    elif row['answer_format'].lower() == 'y/n/na':
                        question = main_config.y_n_question
                        question['name'] = row['code']
                        question['text'] = row[txt_lang]
                        question['language'] = lang
                        question['other'] = 'N'
                        write_row_outfile(outfile, question)


if __name__ == "__main__":
    main()
