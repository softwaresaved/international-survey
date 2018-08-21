#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Wrapper around survey_creation.py script to create only one survey file rather than separated ones as for 2016 and 2017 survey version
"""

__author__ = "Olivier Philippe"


import os
import csv
from collections import OrderedDict
from creating_survey import surveyCreation
from include.formatCondition import conditionFormat
from include.logger import logger

logger = logger(name="one_survey_creation", stream_level="DEBUG")


# # Here the list of the countries -- need to be put into a config file rather than hardcoded
# # TODO: config file!
dict_countries = {'de': "Germany",
                  'nl': "Netherlands",
                  'uk': "United Kingdom of Great Britain and Northern Ireland",
                  'us': "United States of America",
                  'zaf': "South Africa",
                  'nzl': "New Zealand",
                  'can': 'Canada',
                  'aus': "Australia"}
list_bool = ['yes', 'y', 't', 'true', 'Yes', 'YES', 'Y', 'T', 'True', 'TRUE']

filename = './2018/questions.csv'

year = '2018'


class gettingQuestions:
    """
    This class parse the file `questions.csv` and create a dictionary with all the questions.
    It also parses all the specific countries folders and create a specific question for each of them when needed.
    """

    def __init__(self, *args, **kwargs):
        """
        """
        self.year = year
        self.filename = filename
        # Dictionary containing the different questions
        self.dict_questions = self.read_original_file()
        self.dict_countries = self.get_list_countries(dict_countries)
        self.list_bool = list_bool

    def read_original_file(self):
        """
        load the file into an OrderedDict with the code of the
        question as key and respecting the order of the question
        """
        dict_questions = OrderedDict()
        with open(self.filename, "r") as f:
            csv_f = csv.DictReader(f)
            for row in csv_f:
                code = row['code']
                del row['code']
                dict_questions[code] = row
        return dict_questions

    def get_list_countries(self, dict_to_check):
        """
        Compare the existing list of countries in the config file and
        in the question file and remove the ones that are not present
        :params:
            dict_to_check dict(): contains all the potential countries
        :return:
            outdict dict(): same as dict_to_check but without the missing keys
        """
        set_country = set()
        for k in self.dict_questions:
            for i in self.dict_questions[k].keys():
                if i in dict_to_check.keys():
                    set_country.add(i)

        to_remove = list()
        for k in dict_to_check:
            if k not in set_country:
                to_remove.append(k)
        for l in to_remove:
            del dict_to_check[l]
        return dict_to_check

    def create_country_list(self, question):
        """
        Check which country is associated with the question and
        return a list containing all of them. In case of `country_specific` is
        selected, it will not add the country `world` as a new specific question
        is created within self.add_world_other()
        params:
            question dict(): containing all the params for the question
        return:
            cond_country_to_add list(): all countries that are associated with the question
        """
        list_countries_to_add = list()
        for country in self.dict_countries:
            if question[country].lower() in self.list_bool:
                list_countries_to_add.append(country)
        if question['world'].lower() in self.list_bool:  # and question['country_specific'].lower() not in self.list_bool:
            list_countries_to_add.append('world')
        return list_countries_to_add

    def create_country_q(self):
        """
        Create a specific question for each country if the question is a country_specific one
        """
        # recreate a new ordered dict
        new_dict = OrderedDict()

        for k in self.dict_questions:
            # First check if there is country_specific condition.
            # In that case, need to create a question for each possibility to be able to show the different answers
            # As limesurvey does not allow the creation of conditions for questions.
            if self.dict_questions[k]['country_specific'] in self.list_bool and self.dict_questions[k]['answer_format'].lower() in ['one choice', 'y/n/na', 'multiple choices']:
                for country in self.create_country_list(self.dict_questions[k]):
                    new_question = self.dict_questions[k].copy()
                    # check if that country has a specific answer file
                    if new_question['answer_file'] != '':
                        outfile = os.path.join(self.year, "answers", 'countries', country, "{}.csv".format(new_question['answer_file']))
                        try:
                            open(outfile)
                            new_question['answer_file'] = outfile

                        # If the specific file is not found it means that country does not need a specific version
                        # of the question. Then keep the original question.
                        except IOError:
                            outfile = os.path.join(self.year, 'answers', "{}.csv".format(new_question['answer_file']))
                            new_question['answer_file'] = os.path.join(self.year, 'answers', "{}.csv".format(new_question['answer_file']))
                            try:
                                open(outfile)
                                new_question['answer_file'] = outfile
                            # If there is no file in the answer folder. It means that for that country (more likely world), the question should be FREETEXT
                            except IOError:
                                new_question['answer_file'] = ''
                                new_question['answer_format'] = 'FREETEXT'
                                new_question['other'] = ''
                                new_question['country_specific'] = ''
                                country = 'world'

                    new_code = '{}q{}'.format(k, country)
                    new_question['country_specific'] = ''
                    for c in self.dict_countries.keys():
                        new_question[c] = ''
                    new_question['world'] = ''
                    new_question[country] = 'Y'
                    new_dict[new_code] = new_question

            else:
                new_dict[k] = self.dict_questions[k].copy()
                if new_dict[k]['answer_file'] != '':
                    new_dict[k]['answer_file'] = os.path.join(self.year, 'answers', "{}.csv".format(new_dict[k]['answer_file']))

        self.dict_questions = new_dict.copy()

    def insert_code_in_dict(self):
        """
        Creating_survey script expect each row with the code key inserted in the key-value 'code': $code,
        rather than being the keys of the dictionary and then having all row in a list
        """
        final_list = list()
        for k in self.dict_questions:
            new_dict = self.dict_questions[k]
            new_dict['code'] = k
            final_list.append(new_dict)
        self.dict_questions = final_list

    def format_condition(self):
        """
        Call to the class formatCondition by passing the information
        and receiving the self.dict_questions with the formatted conditions
        """
        condition_format = conditionFormat(self.dict_questions, self.dict_countries, self.year, self.list_bool)
        self.dict_questions = condition_format.run()

    def run(self):
        """
        Run all the steps at one time
        """
        logger.info('Add the world condition')
        logger.info('Create question for each country')
        self.create_country_q()

        # Run the condition formating for all the questions
        self.format_condition()
        for k in self.dict_questions:
            print(k)
            print(self.dict_questions[k])
            print('\n')
        self.insert_code_in_dict()


def main():

    # logger.info('Read config file')
    # config_file = "../config/" + args.config
    #
    # # set up access credentials
    # config_value = configParser()
    # config_value.read(config_file)

    # Get the file and transform it to create all the questions and conditions for each country

    logger.info('Getting the file and transforming it for the country specific conditions')
    getting_question = gettingQuestions()
    getting_question.run()

    # Init the survey creation process
    logger.info('Init the survey creation')
    creating_survey = surveyCreation(getting_question.dict_questions)
    logger.info('Running the survey creation')
    creating_survey.run()


if __name__ == "__main__":
    main()
