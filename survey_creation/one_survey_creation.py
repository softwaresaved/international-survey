#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Wrapper around survey_creation.py script to create only one survey file rather than separated ones as for 2016 and 2017 survey version
"""

__author__ = "Olivier Philippe"


import csv
from collections import OrderedDict


# # Here the list of the countries -- need to be put into a config file rather than hardcoded
# # TODO: config file!
list_countries = ['de', 'nl', 'uk', 'us', 'zaf', 'nzl', 'aus', 'can']
list_bool = ['yes', 'y', 't', 'true']


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
        - create a new question with
            - code: '$code_world'
            - txt: '$txt_of_the_question' (just get the same text)
            - type: freetext
            - condition: (if not countries)
        """
        def check_world_free_txt(question):
            """
            Check if the question is  either one_choice or multiple_choice
            and its is selected as 'country_specific'
            and 'world' is selected then:
            :params:
                question dict(): the question to check
            :return:
                bool: True if match the condition, False if not
            """
            if question['country_specific'].lower() in list_bool:
                if question['world'].lower() in list_bool:
                    return True

        # recreate a new ordered dict
        new_dict = OrderedDict()
        # parse all the questions to find which one has to be created for world
        for k in self.dict_questions:
            # add the question to the new dict to respect the same order
            new_dict[k] = self.dict_questions[k]
            # check if the questions need to be created
            if check_world_free_txt(new_dict[k]):
                new_question = new_dict[k]
                new_question['code'] = "{}_world".format(k)
                new_question['answer_format'] = 'FREETEXT'
                new_question['answer_file'] = ''
                new_question['other'] = ''
                for country in list_countries:
                    new_question[country] = ''

                print(new_question)
                # create the question

                # append it to the dictionary

        # replace the current dictionary with the new one
        self.dict_question = new_dict
        pass

    def add_condition_about_countries(self):
        """
        Append the existing condition with the conditions about the countries
        """
        for k in self.dict_question:
            condition = self.dict_questions[k]['condition']
            cond_country_to_add = list()
            for country in list_countries:
                if self.dict_question[k][country] in list_bool:
                    cond_country_to_add.append(country)
            if len(cond_country_to_add) and self.dict_question[k]['world'] in list_bool:
                print(k)



def main():
    getting_question = gettingQuestions()
    getting_question.read_original_file()
    getting_question.add_world_other()
    getting_question.add_condition_about_countries()
    # print(getting_question.dict_questions)


if __name__ == "__main__":
    main()
