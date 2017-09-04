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
    Create an Ordered dictionary to be used to translate csv file to tsv
    """
    return OrderedDict((k, '') for k in creationConfig.main_headers)


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
                           fieldnames=creationConfig.main_headers)
        w.writeheader()
    return outfile


def read_survey_file(folder):
    """
    Read the survey csv file and yield each line as a dictionary
    """
    question_file = os.path.join(folder, '.'.join([folder, 'csv']))
    with open(question_file, 'r') as f:
        csv_f = csv.reader(f, delimiter=';', quotechar='"')
        for row in csv_f:
            yield row


## Insert the additional language if found one. Add it into the list

def write_row_outfile(outfile, row):
    """
    """
    with open(outfile, 'a') as f:
        f.write({k: v for k, v in row})


def main():
    folder = sys.argv[1]
    outfile = init_outfile(folder)
    output_survey = creating_dictionary()
    for k in output_survey:
        print(k, output_survey[k])
    # print(output_survey)
    for line in read_survey_file(folder):
        pass
        # print(line)


if __name__ == "__main__":
    main()
