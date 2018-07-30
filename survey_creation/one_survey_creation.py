#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Wrapper around survey_creation.py script to create only one survey file rather than separated ones as for 2016 and 2017 survey version
"""

__author__ = "Olivier Philippe"


import csv
from collections import OrderedDict

class gettingQuestions:
    """
    This class parse the file `questions.csv` and create a dictionary with all the questions. It also parses all the specific countries folders and create a specific question for each of them when needed.
    """

    def __init__(self, *args, **kwargs):
        """
        """
        self.filename = "./2018/questions.csv"
        # Dictionary containing the different questions
        self.dict_questions = OrderedDict()

    def read_original_file(self):
        """
        load the file
        """
        with open(self.filename, "r") as f:
            csv_f = csv.DictReader(f)
            print(csv_f)
            for row in csv_f:
                code = row['code']
                del row['code']
                self.dict_questions[code] = row

    def add_world_other(self):
        """
        Check question if it is country specific and one choice
        and if 'world' is also selected. In that case, add a new question
        using the same code and the same text but give a freetext and add the condition
        that should be NOT any country selected
        """
        pass


    def add_condition_about_countries(self):
        """
        Append the existing condition with the conditions about the countries
        """


def main():
    getting_question = gettingQuestions()
    getting_question.read_original_file()
    print(getting_question.dict_questions)


if __name__ == "__main__":
    main()
