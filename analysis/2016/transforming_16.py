import pandas as pd
import csv


def get_answer_item(self, path_to_file):
    """
    Parse all the files contained in the folder and
    create a dictionary with the data contained into the value
    and the filename as key

    :param:
        path_to_file str(): path to the folder
    :return:
        dict(): containing all the data
    """
    answer_item_dict = dict()
    for filename in glob.glob(os.path.join(path_to_file, '*.csv')):
        with open(filename) as f:
            file_key, _ = os.path.splitext(os.path.basename(filename))
            # Set the delimiter as : to avoid taking
            # the comma as delimiter
            reader = csv.reader(f, delimiter=':')
            answer_item_dict[file_key] = [i[0] for i in reader]

    return answer_item_dict

# Create a dictionary containing the data about the questions
complete_dict = list()
with open("../../survey_creation/2016/uk/question_2.csv") as f:
    complete_file = csv.DictReader(f)
    for row in complete_file:
        complete_dict.append(row)
complete_dict
# Load dataset
df = pd.read_csv('./data/raw_data.csv')

# Subsetting the data by creating a subset list
subsetting_list = list()
for row in complete_dict:
    new_col_name = '{}. {}'.format(row['code'], row['questions'].replace(u'\xa0', ' '))
    if row['Original title'] in df.columns:
        subsetting_list.append(new_col_name)
    df.rename(columns={row['Original title']: new_col_name}, inplace=True)

list(df.columns)
new_df = df[subsetting_list]
# Subsetting the data to only have the data that contains information.
list(new_df.columns)
for col in new_df:
    for row in complete_dict:
        if '{}. {}'.format(row['code'], row['Original title']) == col:
            if row['answer_format'] == 'ONE CHOICE':
                print(col, row['file_17'])


            # print(col, row['file_17'])
            if row['file_17'] != '':
                # if row['file_17'] not in ['likert_agree', 'likert_time_5']:
                print(col, row['file_17'])
    # print(df[col].unique())

