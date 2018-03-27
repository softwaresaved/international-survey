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
        for col in df.columns:
            multi_col = col.split('[')[0].strip()
            if element['question'] == col or element['question'] == multi_col:

                if element['answer_format'].lower() == 'multiple choices':
                    new_col_name = '{}[multi]. {}'.format(element['code'], col.replace(u'\xa0', ' ').strip())
                else:
                    new_col_name = '{}. {}'.format(element['code'], col.replace(u'\xa0', ' ').strip())
                print(new_col_name)
                subsetting_list.append(new_col_name)
                # print(element['Original title'])
                df.rename(columns={col: new_col_name}, inplace=True)

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


def clean_education(df):
    """
    Clean the education ['other'] and add it to the right column
    """
    replace_education = {"Software Engineering": "Computer Sciences",
                         "Computer Science & Physics": "Computer Sciences",
                         "Geography": "Social studies",
                         "Economics": "Social studies",
                         "Psychology": "Subjects allied to Medicine"}
    list_to_get = ['Social studies', 'Computer Sciences', 'Subjects allied to Medicine']
    df['edu3. Enter your academic subject'].replace(replace_education, inplace=True)
    df['edu2. What was your academic subject?'] = np.where(df['edu3. Enter your academic subject'].isin(list_to_get),
                                                           df['edu3. Enter your academic subject'],
                                                           df['edu2. What was your academic subject?'])
    return df


def clean_salary(df):
    """
    """
    df['socio4. Please select the range of your salary'] = df['socio4. Please select the range of your salary'].str.replace('&pound;', '£')
    return df


def clean_contract(df):
    """
    """
    replacing_dict = {'2018': 36}
    df['currentEmp11. What is the duration of your current contract?'].replace(replacing_dict, inplace=True)
    return df


def clean_year(df):
    """
    """
    replacing_dict = {"2006 (Seconded in 2014)": "2006",
                      "3": "2013"}
    df['currentEmp16a. In what year did you start your current position?'].replace(replacing_dict, inplace=True)
    return df


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
        row['answer_file'] = row['code']
    else:
        row['answer_file'] = row['file_17']
    return row


def clean_likert(root_file_answer, row, df, col):
    """
    """
    if row['answer_file'] == 'likert_time_10':
        replacing_dict = {'1 (Never)': '1 (None at all)',
                          '1 (never)': '1 (None at all)',
                          '5 (about half my time)': '5',
                          '10 (all my time)': '10 (All my time)'}
        col_to_return = df[col].replace(replacing_dict)
    elif row['answer_file'] == 'likert_time_5':
        replacing_dict = {'1 (Never)': 'Never',
                          '1 (never)': 'Never',
                          '2': 'Sometimes',
                          '3': 'Often',
                          '4': 'Very Often',
                          '5 (Always)': 'Always'}
        col_to_return = df[col].replace(replacing_dict)
    else:
        col_to_return = df[col]
    return col_to_return, row


def clean_numeric(df, col):
    """
    """
    df[col] = pd.to_numeric(df[col], errors='coerce')

    df[col].replace((np.inf, -np.inf), np.nan, inplace=True)
    return df[col]


def del_mails(df):
    """
    Function to delete emails from the cleaned dataset
    """
    mail = "Please enter your email address --  -- "
    return df.drop(mail, axis=1, inplace=True)


def main():
    """
    """
    # Location of different files
    root_file = '../../../survey_creation/2017/can/'
    root_file_answer = root_file + 'listAnswers/'
    information_file = "../../../survey_creation/2017/can/questions.csv"
    original_data = './data/original_data.csv'
    raw_data = './data/raw_data.csv'

    # Create a dictionary containing the data about the questions
    complete_info = get_information(information_file)

    # Load dataset
    df = pd.read_csv(original_data)

    # Subsetting the data by creating a subset list
    sub_df = subsetting_df(df, complete_info)

    # # Dropping Non-UK
    # sub_df = sub_df[sub_df['socio1. In which country do you work?'] == 'United Kingdom']
    #
    # # Clean the years
    # sub_df = clean_year(sub_df)
    # # Clean salary
    # sub_df = clean_salary(sub_df)
    # # Complete eduction
    # sub_df = clean_education(sub_df)
    #
    # # Clean duration contract
    # sub_df = clean_contract(sub_df)
    # # Subsetting the data to only have the data that contains information
    new_list_question = list()
    for col in sub_df:
        for row in complete_info:

            new_col_name = '{}. {}'.format(row['code'], row['question'].replace(u'\xa0', ' '))
            if new_col_name.lower().rstrip() == col.lower().rstrip():
                if 'likert' in row['answer_format'].lower():
                    print('Doing likert')
                    sub_df[col], row = clean_likert(root_file_answer, row, sub_df, col)
                elif row['answer_format'].lower() == 'freenumeric':
                    sub_df[col] = clean_numeric(sub_df, col)
                elif row['answer_format'].lower() == 'multiple choice':
                    print('Column with multiple choice: {}'.format(col))
                new_list_question.append(row)

    # writing_new_dict(new_list_question, root_file)

    # record the subsetted dataset
    sub_df.to_csv(raw_data)


if __name__ == "__main__":
    main()
