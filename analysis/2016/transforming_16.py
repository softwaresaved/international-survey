import pandas as pd
import csv
import os
import glob
import numpy as np


def get_answer_item(path_to_file):
    """
    """
    filename = '{}{}'.format(path_to_file, '.csv')
    print(filename)
    with open(filename) as f:
        # Set the delimiter as : to avoid taking
        # the comma as delimiter
        reader = csv.reader(f, delimiter=';')
        return [i[0] for i in reader]



root_file_answer = '../../survey_creation/2016/uk/listAnswers/'

# Create a dictionary containing the data about the questions
complete_dict = list()
with open("../../survey_creation/2016/uk/question_2.csv") as f:
    complete_file = csv.DictReader(f)
    for row in complete_file:
        complete_dict.append(row)
# Load dataset
df = pd.read_csv('./data/raw_data.csv')

# Subsetting the data by creating a subset list
subsetting_list = list()
for row in complete_dict:
    new_col_name = '{}. {}'.format(row['code'], row['questions'].replace(u'\xa0', ' '))
    if row['Original title'] in df.columns:
        subsetting_list.append(new_col_name)
    df.rename(columns={row['Original title']: new_col_name}, inplace=True)

new_df = df[subsetting_list]
# Subsetting the data to only have the data that contains information.
for col in new_df:
    for row in complete_dict:
        if '{}. {}'.format(row['code'], row['questions']) == col:
            # print(col, row['file_17'])
            if row['answer_format'].lower() == 'one choice':

                answers = get_answer_item('{}{}'.format(root_file_answer, row['file_17']))
                difference = set(new_df[col].unique()).difference(set(answers))
                difference.remove(np.NaN)
                if len(difference) > 0:

                    print(difference)

                # print(col, row['file_17'])

