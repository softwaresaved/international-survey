#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Olivier Philippe"


"""
Limesurvey offers the possibility to import/export a TSV file containing all the information
of the survey structure. Using this possibility, this script aims to translate the files used
by the different groups to creates their survey, into a compatible TSV file.
It take only the argument of the folder where all the information is stored, and create a new
compatible file.
All information about the TSV file structure can be retrieved here:
    https://manual.limesurvey.org/Tab_Separated_Value_survey_structure
"""

import re
import csv
import sys
import os
import itertools
from collections import OrderedDict
from include.get_arguments import get_arguments
from include.static_headers import creationConfig as static_headers
from include.config import config as specific_config
import importlib
from random import shuffle
from markdown import markdown
from bs4 import BeautifulSoup


class surveyCreation:
    """
    Creating a text file for limesurvey that can be imported, using the
    resources in the csv files and in the different folders for each
    country's project
    """

    def __init__(self, questions):
        """
        Get the project name (folder).
        Import the associated config file
        Create the outfile path
        :params:
            :questions dict(): All questions and details about them
        """
        self.questions = questions
        self.year = '2018'
        # create a dictionary containing all the questions code
        # and for each the order of the answers as output in the survey
        # This dict is needed for the setup_condition(self) as it
        # require the position of the answer. It is only needed
        # for the one choice type of question as it works only for Y/N and one choice
        self.order_answer_one_choice = dict()

    def init_outfile(self):
        """
        Rewrite over the existing file to avoid issue of appending and
        return the path to the file
        """
        outfile_name = "questions_to_import.txt"
        with open(outfile_name, "w") as f:
            w = csv.DictWriter(
                f,
                delimiter="\t",
                lineterminator="\n",
                quotechar='"',
                fieldnames=static_headers.main_headers,
            )
            w.writeheader()
        self.outfile = outfile_name

    @staticmethod
    def _to_modify(original_list, modified_list):
        """
        """
        return_list = list()
        for element in original_list:
            to_replace = False
            for e in modified_list:
                if element["name"] == e["name"]:
                    return_list.append(e)
                    to_replace = True
                    break
            if to_replace is False:
                return_list.append(element)
        return return_list

    @staticmethod
    def _to_add(original_list, list_to_add):
        """
        """
        for obj in list_to_add:
            original_list.insert(obj[1], obj[0])
        return original_list

    def _write_row(self, row):
        """
        Append a dictionary (a row) to the outfile.
        The dictionary as to respected the keys structure
        found in the static_headers.main_headers
        As the format accepted by limesurvey is tsv, the
        separator as setup to be tabulation ('\t')
        :params:
            :row dict(): containing the information to record
                in the file

        :return: None, record into the self.outfile
        """
        with open(self.outfile, "a") as f:
            w = csv.DictWriter(
                f,
                delimiter="\t",
                lineterminator="\n",
                quotechar='"',
                fieldnames=static_headers.main_headers,
            )
            w.writerow(row)

    def _record_list(self, list_to_copy):
        """
        Get a list of dictionary to add into the outfile.
        Get each dictionary and update the empty dictionary created
        by create_empty_row() to be sure all the headers and element are
        set up (with '' if empty)
        :params:
            :list_to_copy list(): List of dictionary to record

        :return:
            :None: record each dict from the list into the self.outfile
        """

        def create_empty_row():
            """
            Create an Ordered dictionary to be used to translate csv file to tsv
            """
            return OrderedDict((k, "") for k in static_headers.main_headers)

        for element in list_to_copy:
            row = create_empty_row()
            row.update(element)
            self._write_row(row)

    def create_header(self):
        """
        Create the headers for the outfile. The
        headers are recorded in the static_headers file.
        The specific_config file can also contain specific parameters
        to either modify or add to the headers dictionary before recording
        it into  the outfile.
        These headers needs to be added at the top of the outfile.
        The header needs to be recorded only once and does not change with
        the added translation in the case they are some

        :return:
            :None: writes the header into the outfile
        """
        # Create a copy the header to the empty file
        # Check if some parameters needs to be modify from the specific_config
        good_parameters = self._to_modify(
            static_headers.global_headers, specific_config.header_to_modify
        )
        # Check if some parameters needs to be added.
        good_parameters = self._to_add(
            good_parameters, specific_config.header_to_add
        )
        # Record the copy into the file
        self._record_list(good_parameters)

    def _get_languages(self):
        """
        Add any languages to the list that are addition to english
        :return:
            :languages list(): all languages represented by their code
                the language 'en' is always the first element to the list
        """
        languages = static_headers.languages
        try:  # Only add language if the option is in the config file
            languages.append(specific_config.languages_to_add)
        except AttributeError:
            pass
        return languages

    @staticmethod
    def _add_text_message(full_list, message, type_message):
        """
        """
        return_list = list()
        message_done = False
        for element in full_list:
            if message_done is False:
                if element["name"] == "surveyls_{}text".format(type_message):
                    message_done = True
                    element["text"] = message
            return_list.append(element)
        return return_list

    def create_survey_settings(self):
        """
        Add the welcome and the end message and set up the different setting in the survey
        """

        def get_text(type_message, lang=None):
            """
            """
            if lang and lang != "en":
                filename = "{}_message_{}.md".format(type_message, lang)
            else:
                filename = "{}_message.md".format(type_message)

            folder = os.path.join(self.year, "texts")
            path = os.path.join(folder, filename)
            with open(path, "r") as f:
                html_file = markdown(f.read())

            # Need to add target="_blank" to the link for opening in new tab in limesurvey
            soup = BeautifulSoup(html_file, "html.parser")
            links = soup.find_all("a")
            for link in links:
                link["target"] = "_blank"
            return soup

        for lang in self.languages:
            # All these None are a workaround to fix the bug that add
            # two titles for the second language. No idea why
            survey_settings = None
            setting_with_lang = None
            survey_title = None
            survey_title_row = None
            # Get the welcome message
            welcome_message = get_text("welcome", lang)
            # Get the end message
            end_message = get_text("end", lang)
            survey_settings = self._to_modify(
                static_headers.global_settings, specific_config.settings_to_modify
            )
            survey_settings = self._to_add(
                survey_settings, specific_config.settings_to_add
            )

            survey_title = specific_config.survey_title[lang]
            survey_title_row = {
                "class": "SL",
                "name": "surveyls_title",
                "text": survey_title,
            }
            survey_settings.insert(0, survey_title_row)
            survey_settings = self._add_text_message(
                survey_settings, welcome_message, "welcome"
            )
            survey_settings = self._add_text_message(
                survey_settings, end_message, "end"
            )

            # Add the appropriate language field for each of the dictionary
            setting_with_lang = list()
            for d in survey_settings:
                d["language"] = lang
                setting_with_lang.append(d)

            self._record_list(setting_with_lang)

    def check_adding_section(self, row, nbr_section, default_row, lang):
        if int(row["section"]) - 1 != nbr_section:
            # -1 because the section numbers starts at 0 but
            # in the csv survey_file it starts at 1
            nbr_section = int(row["section"]) - 1
            section = static_headers.group_format
            # type/scale are like 'G0', 'G1', etc.
            section["type/scale"] = "G" + str(nbr_section)
            section["language"] = lang
            section.update(default_row[nbr_section][lang])
            self._write_row(section)
        return nbr_section

    @staticmethod
    def read_survey_file(year):
        """
        Read the survey csv file and yield each line as a dictionary
        """
        # question_file = os.path.join(year, country, '.'.join([folder, 'csv']))
        question_file = os.path.join(year, "questions.csv")
        with open(question_file, "r") as f:
            csv_f = csv.DictReader(f)
            for row in csv_f:
                yield row

    @staticmethod
    def group_likert(indict):
        """
        Take the dictionary of all the questions and group them
        into the same group if they have to be displayed together.
        Only applicable for the type_question likert
        It also perform a check to see if a condition as been setup with
        the key 'condition'.
        In that case it does not group the questions
        """
        previous_answer_format = None
        previous_file_answer = None
        previous_code = None
        previous_file_answer = None
        group_survey_q = list()
        for q in indict:
            current_answer_format = q["answer_format"].lower()
            current_file_answer = q["answer_file"]
            current_code = "".join([i for i in q["code"] if not i.isdigit()])
            if current_answer_format == "likert":
                if len(group_survey_q) > 0:
                    if current_file_answer == previous_file_answer or previous_file_answer is None:
                        if previous_answer_format == "likert":
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

    @staticmethod
    def get_answer(year, file_answer):
        """
        """
        outfile = os.path.join(
            year, "answers", "{}.csv".format(file_answer)
        )
        with open(outfile, "r") as f:
            return [x[:-1] for x in f.readlines()]

    def setup_question(self, type_question, row, txt_lang, lang):
        """
        Return a formatted dictionary with the shared information
        accross all questions
        """

        if type_question == "multi_likert":
            question = static_headers.likert_question
        elif type_question == "one choice":
            question = static_headers.one_choice_question
        elif type_question == "ranking":
            question = static_headers.ranking_question
        elif type_question == "multiple choice":
            question = static_headers.multiple_choice_question
        elif type_question == "freenumeric":
            question = static_headers.freenumeric_question
        elif type_question == "freetext":
            question = static_headers.freetext_question
        elif type_question == "likert":
            question = static_headers.likert_question
        elif type_question == "y/n/na":
            question = static_headers.y_n_question
        elif type_question == "datetime":
            question = static_headers.datetime_question

        if type_question == "multi_likert":
            # If multi likert it means the questions are presented in an array
            # where the header is the header for the arrays and all questions
            # are created during the subquestion process. In consequences
            # The questions here cannot have the row['text'] as for the other
            # type of questions but rather an unique id that is ensure
            # by incrementing the self.code_to_multiple_question.
            question["name"] = "likert" + str(self.code_to_multiple_question)
            self.code_to_multiple_question += 1
            question["text"] = ""
        else:
            question["name"] = row["code"]
            question["text"] = row[txt_lang]

        question["relevance"] = self.setup_condition(row["condition"])

        question["language"] = lang

        if row["other"] == "Y":
            question["other"] = "Y"
        else:
            question["other"] = "N"

        if row["mandatory"] == "Y":
            question["mandatory"] = "Y"
        else:
            question["mandatory"] = ""

        if row["public"] == "N":
            question["help"] = specific_config.private_data[lang]
        else:
            question["help"] = ""
        self._write_row(question)

    def setup_subquestion(self, type_question, lang, list_likert=None, txt_lang=None):
        """
        """
        if type_question == "multi_likert":
            for row in list_likert:
                subquestion = static_headers.subquestion
                subquestion["relevance"] = "1"
                subquestion["language"] = lang
                subquestion["name"] = row["code"]
                subquestion["text"] = row[txt_lang]
                self._write_row(subquestion)

        if type_question == "ranking":
            # Create the Subquestion ranks
            for i in range(1, 9):  # To get 8 ranked questions
                subquestion = static_headers.subquestion
                subquestion["name"] = str(i)
                subquestion["text"] = "Rank" + str(i)
                subquestion["language"] = lang
                subquestion["relevance"] = "1"
                self._write_row(subquestion)

        if type_question == "likert":
            # Need to create an empty subquestion
            subquestion = static_headers.subquestion
            subquestion["name"] = "SQ001"
            subquestion["relevance"] = "1"
            subquestion["language"] = lang
            subquestion["text"] = ""
            self._write_row(subquestion)

    def setup_answer(self, type_question, row, index_lang, lang):
        """
        Create the answer itself
        """
        n = 1
        for text_answer in self.get_answer(self.year, row["answer_file"]):
            if type_question == "one choice":
                # add the answer and its position to the self.order_answer_one_choice dict for
                # the self.setup_condition()
                self.order_answer_one_choice.setdefault(row["code"], {})[
                    n
                ] = text_answer.lower()
                answer_row = static_headers.one_choice_answer
            elif type_question == "multi choice":
                answer_row = static_headers.multiple_choice_answer
            elif type_question == "likert":
                answer_row = static_headers.likert_answer
            elif type_question == "ranking":
                answer_row = static_headers.ranking_answer
            answer_row["name"] = str(n)
            # answer_row['name'] = 'A' + str(n)
            # For multichoice the answers are considered as subquestion
            # Need to change the name value
            if type_question == "multi choice":
                default_sq_value = "SQ000"
                answer_row["name"] = default_sq_value[: -len(str(n))] + str(n)
            # to get the translation  of the answers. If there is None, it takes the first
            # element (the english one). Needed because sometimes, the answers are not translated
            try:
                answer_row["text"] = text_answer.split(";")[index_lang].strip('"')
            except IndexError:
                answer_row["text"] = text_answer.split(";")[0].strip('"')
            answer_row["language"] = lang
            self._write_row(answer_row)
            n += 1

    def get_txt_lang(self, lang, index_lang):
        """
        Return the right txt key when a translation is pickup
        if it is in English, the key is only 'question', but in
        case of translation it is 'lang_trans'.format(int) for all
        the language the survey has. The order of the languages in the
        main csv file needs to be the same order as in the config file
        params:
            :lang str(): the code of the language used
            :index_lang int(): the number to know which translation it is
        return:
            :str(): the key used later to access the text of the question
        """
        # Speficify where to find the text for the question
        if lang != "en":
            return "lang_trans" + str(index_lang)
        else:
            return "question"

    def setup_condition(self, condition):
        """
        transform preformated 'condition' into accepted 'relevance' for limesurvey and return
        the string.
        Add a condition to the question to appears only if it satisfied conditions from previous
        questions.
        DISCLAIMER: Only works with Y/N and one choice type of question for the question that trigger
        the condition.
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

        def format_conditions(list_conditions):
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
                list_formated_condition list: contain the same condition but formated for limesurvey
            """
            list_formated_condition = list()
            print(list_conditions)
            for condition in list_conditions:
                # get the code of the question
                code = condition.split(" ")[1].replace("(", "")
                print('code', condition.split(" "))
                # get the comparison operator
                operator = condition.split(" ")[2]
                print('operator', operator)
                # check if the operator are ok
                for x in operator:
                    if x not in ["=", "!", "<", ">"]:
                        raise TypeError(
                            "Error in the condition formating: {}".format(condition)
                        )
                # get the answer it is comparing with
                print('condition', condition.split('"'))
                answer = condition.split('"')[-2].lower()
                # if answer is Y or N, it is simply need to be formated as 'Y' or 'N'
                if answer in ["y", "n", "yes", "no"]:
                    position_answer = '"{}"'.format( answer[0].upper())  # Only need the Y or N
                # If not it means it is from a one choice question and the position of the answer
                # needs to be retrieved
                else:
                    # find that answer in the dict created during the self.setup_answer() to find the index position
                    # of that answer
                    print('Answer to match: ', answer.lower())

                    print(self.order_answer_one_choice[code])
                    for n in self.order_answer_one_choice[code]:
                        print('position answer from dic: ', self.order_answer_one_choice[code][n])
                        if self.order_answer_one_choice[code][n].rstrip() == answer.lower().rstrip():  # Need the double quotes for the limesurvey position_answer = '"{}"'.format(n)
                            position_answer = '"{}"'.format(self.order_answer_one_choice[code][n])
                            print(position_answer)
                            break
                format_condition = "({}.NAOK {} {})".format(code, operator, position_answer)
                list_formated_condition.append(format_condition)
            return list_formated_condition

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

        def final_formating(list_formated_conditions, dict_of_bool):
            """
            """
            if len(list_formated_conditions) == 1:
                return "({})".format(list_formated_conditions[0])
            else:
                # get the list of the position of the different bool
                bool_list = [dict_of_bool[x].upper() for x in sorted(dict_of_bool)]
                # Create a new list by alternating the element of each list
                # Source: https://stackoverflow.com/a/21482016
                to_iterate = [
                    x
                    for x in itertools.chain.from_iterable(
                        itertools.zip_longest(list_formated_conditions, bool_list)
                    )
                    if x
                ]

                list_formated_conditions = "({})".format(" ".join(to_iterate))
            return list_formated_conditions

        # If condition is empty it wil be an empty string
        if condition == "":
            return

        else:
            # Split the conditions by the different AND and OR present and
            # keeps the order to be sure to reconstruct later
            list_of_conditions = split_conditions(condition)
            formated_conditions = format_conditions(list_of_conditions)
            dict_of_bool = get_position_bool(condition)
            formated_string = final_formating(formated_conditions, dict_of_bool)
            return formated_string

    def create_survey_questions(self):
        """
        """
        # Create the questions for each languages, everything has to be done each time
        # the enumerate helps for finding the right answer and the right lang_trans
        # in case of more than one translation
        for index_lang, lang in enumerate(self.languages):
            txt_lang = self.get_txt_lang(lang, index_lang)
            # Add a first section
            nbr_section = -1
            nbr_section = self.check_adding_section(
                {"section": 0}, nbr_section, specific_config.sections_txt, lang
            )

            # Need this variable to inc each time a new multiple questions is created to ensure they are unique
            # only used in the case of likert and y/n/na merged together
            self.code_to_multiple_question = 0

            # pass this generator into the function group_likert() to group Y/N and likert together
            for q in self.group_likert(self.questions):

                # If questions were grouped together, need to change how it is process
                if len(q) > 1:
                    # Check if a new section needs to be added before processing the question
                    nbr_section = self.check_adding_section(
                        q[0], nbr_section, specific_config.sections_txt, lang
                    )

                    # Check if the list of items need to be randomize
                    # if it is the case, just use shuffle() to shuffle the list in-place
                    if q[0]["random"] == "Y":
                        shuffle(q)

                    # Create the question header that needs to be created once for all the
                    # following question
                    self.setup_question("multi_likert", q[0], txt_lang, lang)
                    self.setup_subquestion("multi_likert", lang, q, txt_lang)
                    self.setup_answer("likert", q[0], index_lang, lang)

                else:
                    for row in q:
                        # Check if a new section needs to be added before processing the question
                        nbr_section = self.check_adding_section(
                            row, nbr_section, specific_config.sections_txt, lang
                        )

                        if row["answer_format"].lower() == "one choice":
                            self.setup_question("one choice", row, txt_lang, lang)
                            self.setup_answer("one choice", row, index_lang, lang)

                        if row["answer_format"].lower() == "ranking":
                            # Ranking questions work differently
                            # First a list of rank SQ class need to be created (max 8 here)
                            # Then only the questions are created
                            # As neither of them have specific value for database, they are
                            # created here and not pulled from the config file
                            self.setup_question("ranking", row, txt_lang, lang)
                            # Create the Subquestion ranks
                            self.setup_subquestion("ranking", lang)
                            self.setup_answer("ranking", row, index_lang, lang)

                        if row["answer_format"].lower() == "multiple choices":
                            self.setup_question("multiple choice", row, txt_lang, lang)

                            self.setup_answer("multi choice", row, index_lang, lang)

                        if row["answer_format"].lower() == "freenumeric":
                            self.setup_question("freenumeric", row, txt_lang, lang)

                        if row["answer_format"].lower() == "freetext":
                            self.setup_question("freetext", row, txt_lang, lang)

                        if row["answer_format"].lower() == "likert":
                            self.setup_question("likert", row, txt_lang, lang)
                            # Need to create an empty subquestion
                            self.setup_subquestion("likert", lang)
                            self.setup_answer("likert", row, index_lang, lang)

                        if row["answer_format"].lower() == "y/n/na":
                            self.setup_question("y/n/na", row, txt_lang, lang)

                        if row["answer_format"].lower() == "datetime":
                            self.setup_question("datetime", row, txt_lang, lang)

    def run(self):
        """
        Run the survey creation
        """
        self.init_outfile()
        self.create_header()
        self.languages = self._get_languages()
        self.create_survey_settings()
        self.create_survey_questions()


def main():
    pass
    # # Get which country and which year to create the analysis
    # year, country = get_arguments(sys.argv[1:])
    # create_survey = surveyCreation(country, year)
    # create_survey.run()


if __name__ == "__main__":
    main()
