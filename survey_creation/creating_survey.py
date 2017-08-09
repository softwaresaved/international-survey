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
from include.logger import logger

RUNNING = 'dev'

if RUNNING == 'dev':
    DEBUGGING='DEBUG'
elif RUNNING == 'prod':
    DEBUGGING='INFO'


logger = logger(name='creating survey', stream_level=DEBUGGING)




def main():
    folder = sys.argv[1]
    question_file = os.path.join(folder, folder + '.' + 'csv')
    with open(question_file, 'r') as f:
        csv_f = csv.reader(f, delimiter=';', quotechar='"')
        for row in csv_f:
            print(row)


if __name__ == "__main__":
    main()
