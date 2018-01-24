#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Quick dirty script to collect all the different questions in 2017 and create a file with the ordered list of all questions
found in the different surveys
"""

import os
from collections import OrderedDict
import csv
country_questions = OrderedDict()
for root, dirs, files in os.walk('./2017'):
    for name in files:
        if name == 'questions.csv':
            with open(os.path.join(root, name), 'r') as f:
                reader = csv.DictReader(f)
                country_questions[os.path.basename(root)] = [row for row in reader]


# alphabetical order
country_questions = OrderedDict(sorted(country_questions.items(), key=lambda t: t[0]))

total_code = list()
for country in country_questions:
    index = 0
    for question in country_questions[country]:
        if question['code'] in total_code:
            index = total_code.index(question['code']) +1
        if question['code'] not in total_code:
            total_code.insert(index, question['code'])

total_code = total_code[::-1]
ordered_all_questions = OrderedDict()
for code_question in total_code:
    for country in country_questions:
        for question in country_questions[country]:
            if question['code'] == code_question:
                try:
                    ordered_all_questions[code_question][country] = ordered_all_questions[code_question].get(country, 'Y')
                except KeyError:
                    ordered_all_questions[code_question] = {'question': question['question'],
                                                            'answer_format': question['answer_format'],
                                                            'answer_file': question['answer_file'],
                                                            country: 'Y'}

fields = ['code', 'question', 'answer_format', 'answer_file']
list_country = list(country_questions.keys())
fields.extend(list_country)

for k in ordered_all_questions:
    for i in list_country:
        if i not in ordered_all_questions[k].keys():
            ordered_all_questions[k][i] = 'N'


with open("./2017/summary_questions.csv", "w") as f:
    w = csv.DictWriter(f, fields)
    w.writeheader()
    for k in ordered_all_questions:
        to_write = {'code': k}
        to_write.update({field: ordered_all_questions[k][field] for field in fields if field != 'code'})
        w.writerow(to_write)
