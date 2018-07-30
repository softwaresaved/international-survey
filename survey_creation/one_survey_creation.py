#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Olivier Philippe"


import csv


class gettingQuestions:
    """
    This class parse the file `questions.csv` and create a dictionary with all the questions. It also parses all the specific countries folders and create a specific question for each of them when needed.
    """

    def __init__(self, *args, **kwargs):
        """
        """
        self.filename = "./2018/questions.csv"

    def read_original_file(self):
        """
        load the file
        """
        dict_to_return = dict()
        with open(self.filename, "r") as f:
            csv_f = csv.DictReader(f)
            print(csv_f)
            for row in csv_f:
                dict_to_return[row['code']] = row.remove('code')
                print(row['code'])


def main():
    getting_question = gettingQuestions()
    getting_question.read_original_file()


if __name__ == "__main__":
    main()
