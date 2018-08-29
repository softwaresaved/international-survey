#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Olivier Philippe"

"""
Create the condition for the limesurvey.
"""

import re
import itertools


class conditionFormat:
    """
    """
    def __init__(self, questions, dict_countries, year, list_bool):
        """
        """
        self.questions = questions
        self.dict_countries = dict_countries
        self.year = year
        # create a dictionary containing all the questions code
        # and for each the order of the answers as output in the survey
        # This dict is needed for the setup_condition(self) as it
        # require the position of the answer. It is only needed
        # for the one choice type of question as it works only for Y/N and one choice
        self.order_answer_one_choice = dict()

        self.list_bool = list_bool

    @staticmethod
    def get_answer(year, file_answer):
        """
        """
        outfile = file_answer
        with open(outfile, "r") as f:
            return [x[:-1] for x in f.readlines()]

    @staticmethod
    def split_conditions(condition):
        """
        Split the condition received by the boolean operators and
        return a list of the different conditions
        :params:
            condition str: containing a text like "(cond1) AND (cond2) OR cond3)
        :return:
            list_of_conditions list: containing the different conditions
        """
        extracted_condition = re.findall("\(.*?\)", condition)
        return extracted_condition

    @staticmethod
    def get_position_bool(instring):
        """
        Check if the string contains 'and' and/or 'or' and get their index.
        then return a dict with the index position as key and the boolean as values
        :params:
            instring str: containing the text with the potential conditions
        :return:
            dict_position_bool dict: index position of the boolean as key and boolean
            as value
        """

        def find_index_word(instring, match_word):
            """
            Check the position of the match_word in the instring
            and return a list of the different index position
            :params:
                instring str: where to check the presence of the word
                match_word str: the word to check if it is in the instring

            :return:
                list_position list: list of all the index position (the index
                of the first charactere of the match word)
            """
            list_position = list()
            index = 0
            while index < len(instring):
                index = instring.lower().find(match_word.lower(), index)
                if index == -1:
                    break
                list_position.append(index)
                index += len(match_word)
            return list_position

        dict_position_bool = dict()
        for boolean in [") and (", ") or ("]:
            for i in find_index_word(instring, boolean):
                dict_position_bool[i] = (
                    boolean.replace(")", "").replace("(", "").strip()
                )
        return dict_position_bool

    def create_index_answer(self):
        """
        Create a dictionary with the index of the
        answer found in each files.
        It is needed later to do the comparison
        """
        for q in self.questions:
            n = 1
            type_question = self.questions[q]['answer_format'].lower().rstrip()
            if (type_question == "one choice" or type_question == 'multiple choices'):
                # add the answer and its position to the self.order_answer_one_choice dict for
                # the self.setup_condition()
                for text_answer in self.get_answer(self.year, self.questions[q]["answer_file"]):
                    self.order_answer_one_choice.setdefault(q, {})[n] = text_answer.split(";")[0].strip('"').lower()
                    n += 1

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
        if question['world'].lower() in self.list_bool and question['country_specific'].lower() not in self.list_bool:
            list_countries_to_add.append('world')
        return list_countries_to_add

    def check_if_condition_country_specific(self, current_question):
        """
        Check if the condition is based on a country specific question.
        In that case it replaces the code with the country specific question code
        :params:
            current_question dict(): the question that contains the condition
        :return:
            right_code_condition str(): Same list condition but with reformated code
        """
        right_code_condition = current_question['condition']
        for index, value in enumerate(current_question['condition']):
            splitted_condition = value.split(' ')
            code = splitted_condition[0][1:]
            if self.questions[code]['country_specific']:
                list_proper_code = list()
                for country in self.create_country_list(current_question):
                    new_code = '({}q{}'.format(code, country)
                    splitted_condition[0] = new_code
                    list_proper_code.append(splitted_condition)
                country_code_condition = '{}'.format(" OR ".join(list_proper_code))
                right_code_condition[index] = country_code_condition
        return right_code_condition

    def create_country_condition(self, current_question, countries, operator, existing_condition, code_question_country="socio1"):
        """
        Create the country condition based on which country need to be include or exclude from a question
        Parse the list provided and output a formated string for each of them.
        :params:
            question dict(): contains the question information
            countries list() of str(): All countries that need to formatted in the condition.
            operator str(): the type of comparison needed for the condition
            existing_condition str(): str containing the existing condition for the question
            code_question_country str(): the code of the question where the country is asked
        :return:
            formatted_condition str(): format the condition as:

                ($code_question_country $operator $country1 AND $existing_condition) OR
                (($code_question_country $operator $country2 AND $existing_condition)
            this respect the rules for limesurvey:
                https://manual.limesurvey.org/Setting_conditions/en
        """
        list_str_countries = list()
        # Split the potential conditions
        extracted_condition = re.findall("\(.*?\)", existing_condition)
        for country in countries:

            country_condition = "({} {} \"{}\")".format(code_question_country, operator, self.dict_countries[country])
            list_str_countries.append(country_condition)

        if len(extracted_condition) == 1:
            list_str_countries = ["(({} AND {}))".format(extracted_condition[0], i) for i in list_str_countries]

        if operator == '!=':
            return '{}'.format(" AND ".join(list_str_countries))
        else:
            return '{}'.format(" OR ".join(list_str_countries))

    def add_condition_about_countries(self, question):
        """
        Append the existing condition with the conditions about the countries and replace
        that value in the dictionary.
        """

        def _create_condition(current_question, list_countries_to_add, condition):
            """
            Create the condition string from a list of countries and the pre-existing condition
            :params:
                question dict(): containing the question
                list_countries_to_add list() of str(): all countries that need to be
                added in the condition in the form of a code country
                condition str(): existing condition for the question
            :return:
                final_condition str(): the condition reformated to include the countries
                exception if needed
            """

            # In case all the countries and the world option is present too, no need for conditions
            if len(list_countries_to_add) == len(self.dict_countries) +1:  # size of all potential country + 'world'
                final_condition = condition

            # In case world is not present, create an inclusive list of countries
            elif 'world' not in list_countries_to_add:
                final_condition = self.create_country_condition(current_question, list_countries_to_add, operator='=', existing_condition=condition)

            # If there is less country but world is present need to apply exclusion
            elif len(list_countries_to_add) <= len(self.dict_countries) and 'world' in list_countries_to_add:
                # To get the exclusion list, need to invert the list and passing all countries that are NOT present
                # in that list.
                list_countries_to_exclude = [i for i in self.dict_countries.keys() if i not in list_countries_to_add]
                final_condition = self.create_country_condition(current_question, list_countries_to_exclude, operator='!=', existing_condition=condition)
            return final_condition

        condition = question['condition']
        list_countries_to_add = self.create_country_list(question)

        condition_with_country = _create_condition(question, list_countries_to_add, condition)
        return condition_with_country

    def split_elements(self, list_conditions):
        """
        Get the list of conditions and for each match the appropriate
        index position of the answer that trigger it and apply some formating
        to be compatible with limesurvey
        The formatting of the condition is as follow:
            (($code_question.NAOK == "$name_answer") $BOOL ($code.NAOK == "$name_answer"))
        :params:
            list_condition list: list of strings that contain the conditions
            that are preformated as ($code_question == "$answer")
        :return:
        """
        for condition in list_conditions:
            # get the code of the question
            code = condition.split(" ")[0].replace("(", "")
            # get the comparison operator
            operator = condition.split(" ")[1]
            # check if the operator are ok
            for x in operator:
                if x not in ["=", "!", "<", ">"]:
                    raise TypeError(
                        "Error in the condition formating: {}".format(condition)
                    )
            # get the answer it is comparing with
            if operator == '=':
                operator = '=='
            try:
                answer = condition.split('"')[-2].lower()
            except IndexError:
                raise TypeError('Error in finding the answer in: {}'.format(condition))
            yield code, operator, answer

    def get_position_answer(self, current_question, answer, code):
        """
        For limesurve, the answer need to be the index position of the text in the inserted
        answers choice or Y-N in case of Y/N.
        This function take the answer and retrieve the proper index in the self.order_answer_one_choice
        """
        position_answer = None
        # set up a variable to confirm the
        # if answer is Y or N, it is simply need to be formated as 'Y' or 'N'
        if answer in ["y", "n", "yes", "no"]:
            position_answer = '"{}"'.format(answer[0].upper())  # Only need the Y or N

        # If not it means it is from a one choice question and the position of the answer
        # needs to be retrieved
        else:
            # find that answer in the dict created during the self.setup_answer() to find the index position
            # of that answer
            try:
                for n in self.order_answer_one_choice[code]:

                    if self.order_answer_one_choice[code][n].lower().rstrip() == answer.lower().rstrip():
                        position_answer = "{}".format(n)
                        break
            # If the key does not exists it is because the original code has been removed to create
            # questions specific to each countries
            except KeyError:
                list_countries_to_add = list()
                for country in self.dict_countries:
                    if current_question[country].lower() in self.list_bool:
                        list_countries_to_add.append(country)
                if len(list_countries_to_add) == 0:
                    if current_question['world'].lower() in self.list_bool:
                        list_countries_to_add.append('world')
                for country in list_countries_to_add:

                    code = '{}q{}'.format(code, country)

                for n in self.order_answer_one_choice[code]:
                    if self.order_answer_one_choice[code][n].lower().rstrip() == answer.lower().rstrip():
                        position_answer = "{}".format(n)
                        break

        # if code != 'socio1':
        #     try:
        #         print(code, position_answer, self.order_answer_one_choice[code])
        #     except KeyError:
        #         pass
        return position_answer, code

    def format_for_lime(self, code, operator, answer):
        """
        """
        # In case of exclusion for some countries, need to look like that
        # (is_empty(socio1.NAOK) || (socio1.NAOK != 236)) or (is_empty(socio1.NAOK) || (socio1.NAOK != 237)) or (is_empty(socio1.NAOK) || (socio1.NAOK != 44))))
        format_condition = None
        if operator == '!=':
            if self.questions[code]['answer_format'].lower() == 'multiple choices':
                format_condition = """(is_empty({0}_SQ00{1}.NAOK))""".format(code, answer)
                print(format_condition)
            else:
                format_condition = """(!is_empty({0}.NAOK) and ({0}.NAOK {1} {2}))""".format(code, operator, answer)
        else:
            if self.questions[code]['answer_format'].lower() == 'multiple choices':
                format_condition = """({}_SQ00{}.NAOK == 'Y')""".format(code, answer)
            else:
                format_condition = """({}.NAOK {} {})""".format(code, operator, answer)
        if format_condition is None:
            raise
        return format_condition

    def final_formating(self, list_formated_conditions, dict_of_bool):
        """
        """
        if len(list_formated_conditions) == 1:
            return "({})".format(list_formated_conditions[0])
        else:
            # get the list of the position of the different bool
            bool_list = [dict_of_bool[x].upper() for x in sorted(dict_of_bool)]
            # Create a new list by alternating the element of each list
            # Source: https://stackoverflow.com/a/21482016
            to_iterate = [x for x in itertools.chain.from_iterable(itertools.zip_longest(list_formated_conditions, bool_list)) if x]
            list_formated_conditions = "({})".format(" ".join(to_iterate))
        return list_formated_conditions

    def setup_condition(self, current_question, condition):
        """
        transform preformated 'condition' into accepted 'relevance' for limesurvey and return
        the string.
        Add a condition to the question to appears only if it satisfied conditions from previous
        questions.
        Only works with Y/N and one choice type of question for the question that trigger the condition.
        The condition is added in the question row under the "relevance" field.
        To create the appropriate 'relevance' field it needs to:
            1. Get the code of the question that trigger the condition (field 'name')
            2.1 Get the name of the answer for that question to test the question (field 'name'). In
            case of a one choice, it is a number associated to the position of the answer (incremental, starts at 1)
            In case of a Y/N questions, it is either "Y" or "N".
        The formatting of the condition is as follow:
            (($code_question.NAOK == "$name_answer") $BOOL ($code.NAOK == "$name_answer"))
        :params:
            condition str: get a pre-formatted condition such as:
                ($code_question == "$answer_text") $BOOL ($cond2)
        :return:
            relevance str: formatted condition for the question
        """
        if condition == "":
            return
        else:
            # Split the conditions by the different AND and OR present and
            # keeps the order to be sure to reconstruct later
            list_of_conditions = self.split_conditions(condition)
            formated_conditions = list()
            for code, operator, answer in self.split_elements(list_of_conditions):

                answer, code = self.get_position_answer(current_question, answer, code)
                formated_conditions.append(self.format_for_lime(code, operator, answer))
            dict_of_bool = self.get_position_bool(condition)
            formated_string = self.final_formating(formated_conditions, dict_of_bool)
            return formated_string

    def run(self):
        """
        """
        # create the answers index for all the questions
        self.create_index_answer()
        for i in self.questions:
            question = self.questions[i]
            question['condition'] = self.add_condition_about_countries(question)
            question['condition'] = self.setup_condition(question, question['condition'])
            self.questions[i]['condition'] = question['condition']
        return self.questions
