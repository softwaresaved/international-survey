import pandas as pd
import csv
import numpy as np


def get_answer_item(path_to_file):
    """
    """
    filename = '{}{}'.format(path_to_file, '.csv')
    with open(filename) as f:
        # Set the delimiter as : to avoid taking
        # the comma as delimiter
        reader = csv.reader(f, delimiter=';')
        return [i[0] for i in reader]

def writing_new_dict(new_dict, root_file_answer):
    filename = root_file_answer + 'questions.csv'
    keys = list(new_dict[0].keys())
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(new_dict)


def write_new_answer(difference, root_file_answer, code):
    filename = root_file_answer + code + '.csv'
    print(difference)
    with open(filename, 'w') as f:
        for i in difference:
            f.write(str(i))
            f.write('\n')



root_file = '../../survey_creation/2016/uk/'
root_file_answer = root_file + 'listAnswers/'

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
new_list_question = list()
for col in new_df:
    for row in complete_dict:
        if '{}. {}'.format(row['code'], row['questions']) == col:
            if row['answer_format'].lower() == 'one choice':
                answers = get_answer_item('{}{}'.format(root_file_answer, row['file_17']))
                new_answer = set(new_df[col].unique())
                try:
                    new_answer.remove(np.NaN)
                except KeyError:
                    pass
                try:
                    difference = new_answer.difference(set(answers))
                    # print(difference)
                except AttributeError:
                    difference = []
                    pass
                if len(difference) > 0:
                    write_new_answer(new_answer, root_file_answer, row['code'])
                    row['file_answer'] = row['code']
                else:
                    row['file_answer'] = row['file_17']
            else:
                row['file_answer'] = row['file_17']
        new_list_question.append(row)



writing_new_dict(new_list_question, root_file)

