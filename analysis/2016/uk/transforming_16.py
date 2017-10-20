import pandas as pd
import csv
import numpy as np


def get_information(path):
    """
    """
    complete_list = list()
    with open(path) as f:
        complete_file = csv.DictReader(f)
        for row in complete_file:
            complete_list.append(row)
    return complete_list


def subsetting_df(df, complete_info):
    """
    """
    subsetting_list = list()
    for element in complete_info:
        new_col_name = '{}. {}'.format(element['code'], element['questions'].replace(u'\xa0', ' '))
        if element['Original title'] in df.columns:
            subsetting_list.append(new_col_name)
        df.rename(columns={element['Original title']: new_col_name}, inplace=True)

    return df[subsetting_list]


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
    with open(filename, 'w') as f:
        for i in difference:
            f.write(str(i))
            f.write('\n')


def clean_one_choice(root_file_answer, row, df, col):
    """
    """
    answers = get_answer_item('{}{}'.format(root_file_answer, row['file_17']))
    new_answer = set(df[col].unique())
    try:
        new_answer.remove(np.NaN)
    except KeyError:
        pass
    try:
        difference = new_answer.difference(set(answers))
    except AttributeError:
        difference = []
    if len(difference) > 0:
        write_new_answer(new_answer, root_file_answer, row['code'])
        row['file_answer'] = row['code']
    else:
        row['file_answer'] = row['file_17']
    return row


def clean_likert(root_file_answer, row, df, col):
    """
    """
    row['file_answer'] = row['file_17']
    if row['file_17'] == 'likert_agree':
        replacing_dict = {'1 (Strongly disagree)': 'Strongly disagree',
                          '2': 'Disagree', '3': 'Neither agree or disagree',
                          '4': 'Agree', '5 (Strongly Agree)': 'Strongly Agree'}
        col_to_return = df[col].replace(replacing_dict)
    elif row['file_17'] == 'likert_time_5':
        replacing_dict = {'Sometime ': 'Sometimes', 'Sometime': 'Sometimes'}
        col_to_return = df[col].replace(replacing_dict)
    else:
        col_to_return = df[col]
    return col_to_return, row


def clean_numeric(df, col):
    """
    """
    print(col)
    print(df[col].unique())
    df.loc[col] = pd.to_numeric(df[col], errors='coerce')
    print(df[col].unique())
    return df


def main():
    """
    """
    # Location of different files
    root_file = '../../../survey_creation/2016/uk/'
    root_file_answer = root_file + 'listAnswers/'
    information_file = "../../../survey_creation/2016/uk/question_2.csv"
    original_data = './data/original_data.csv'
    raw_data = './data/raw_data.csv'

    # Create a dictionary containing the data about the questions
    complete_info = get_information(information_file)

    # Load dataset
    df = pd.read_csv(original_data)

    # Subsetting the data by creating a subset list
    sub_df = subsetting_df(df, complete_info)

    # Subsetting the data to only have the data that contains information
    new_list_question = list()
    for col in sub_df:
        for row in complete_info:
            if '{}. {}'.format(row['code'], row['questions']) == col:
                if row['answer_format'].lower() == 'one choice':
                    row = clean_one_choice(root_file_answer, row, sub_df, col)
                elif 'likert' in row['answer_format'].lower():
                    sub_df[col], row = clean_likert(root_file_answer, row, sub_df, col)
                elif row['answer_format'].lower() == 'freenumeric':
                    sub_df[col] = clean_numeric(sub_df, col)
                else:
                    row['file_answer'] = row['file_17']
                new_list_question.append(row)

    writing_new_dict(new_list_question, root_file)

    # record the subsetted dataset
    sub_df.to_csv(raw_data)


if __name__ == "__main__":
    main()
