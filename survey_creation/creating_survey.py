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
from config import creationConfig

RUNNING = 'dev'

if RUNNING == 'dev':
    DEBUGGING='DEBUG'
elif RUNNING == 'prod':
    DEBUGGING='INFO'

logger = logger(name='creating survey', stream_level=DEBUGGING)


def creating_dictionary():
    """
    Create the dictionary to be used to translate csv file to tsv
    """
    return OrderedDict((k, None) for k in creationConfig.main_headers)
# [OrderedDict((k, d[k](v)) for (k, v) in l.iteritems()) for l in L]


def read_survey_file(folder):
    """
    Read the survey csv file and yield each line as a dictionary
    """
    question_file = os.path.join(folder, '.'.join([folder, 'csv']))
    with open(question_file, 'r') as f:
        csv_f = csv.reader(f, delimiter=';', quotechar='"')
        for row in csv_f:
            yield row


def write_row_in_file(input_file, row):
    """
    """
    with open(input_file, 'a') as f:
        # f.write({k: v for
        for key in creationConfig.main_headers:
            pass


def main():
    output_survey = creating_dictionary()
    for k in output_survey:
        print(k, output_survey[k])
    # print(output_survey)
    folder = sys.argv[1]
    for line in read_survey_file(folder):
        pass
        # print(line)


if __name__ == "__main__":
    main()
