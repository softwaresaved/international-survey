# coding: utf-8

# # CANARIE 2017 -- Analysis of the survey

# This notebook is the first draft to analyse the results from [CANARIE]()

# ## Preparation and filtering of the dataset

# In[1]:

# Load libraries
import pandas as pd
import numpy as np
import matplotlib

# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt

#  When using this script with ipython and vimss
plt.ion()
plt.show()


# Load dataset
df = pd.read_csv('./dataset/2017 Cdn Research Software Developer Survey - Public data.csv')
# Number of row == number of participants
len(df.index)

# Replacing all the answer "Prefer not to answer" by NaN, as they are not useful in the analysis
df.replace('Prefer not to answer', np.NaN, inplace=True)


# ### Date submitted
# The variable 'Date submitted' is set up when the participant finish the survey. If the row on this column is empty, it means the participant did not finish the survey. These participants are removed, even if they have submitted partial answers.

# In[3]:

# df['Date submitted'].unique
df = df[df['Date submitted'].notnull()]
# Getting the number of row from the reduced dataframe
len(df.index)


# ### Countries
# A question asked the participants in which country they were currently working and specify when it was not Canada.
#


pd.crosstab(df['In which country do you work?'], columns='Countries')


# There is only 4 others. Which are only one from Japan, 2 from USA and one from UK.


pd.crosstab(df['In which country do you work? [Other]'], columns='Other countries')


# As this answer are not useful for CANARIE, because these people are not working in Canada, they are removed from the dataset.


df = df.loc[df['In which country do you work?'] != 'Other']
# Getting the number of row from the reduced dataframe
len(df.index)


# ### Writing software as part of the work
#
# One question asked if the participants write software for research as part of their work.


pd.crosstab(df['Do you write software for research as part of your job?'], columns='Writing software')


# 13 answered 'No'. This survey, being about researcher that write codes, they are removed from the dataset


df = df.loc[df['Do you write software for research as part of your job?'] == 'Yes']
# Getting the number of row from the reduced dataframe
len(df.index)


# ########################## QUESTIONS CLEANING ###############################

# ### Languages
#
# The survey was in French and in English. The option choose by the participant was collected. It is possible then to see the proportion of participants that answered the survey in French or in English

pd.crosstab(df['Start language'], columns='Language')

df['Start language'].value_counts().plot(kind='bar')


# ### Education level
# The question asked the level of education

# Recode the column as categorical variable
df['What is the highest level of education you have attained?'] = df['What is the highest level of education you have attained?'].astype('category')

# Reorder the factors to match the education level
df['What is the highest level of education you have attained?'].cat.reorder_categories(['Some University',
                                                                                        'College Diploma',
                                                                                        'Bachelors Degree',
                                                                                        'Masters Degree',
                                                                                        'Doctorate'],
                                                                                       inplace=True)
pd.crosstab(df['What is the highest level of education you have attained?'], columns='Education level')


df['What is the highest level of education you have attained?'].value_counts().plot(kind='barh', sort_columns=True)


pd.crosstab(df['In which discipline is your highest academic qualification?'], columns='Disciplines')


df['In which discipline is your highest academic qualification?'].value_counts().plot(kind='barh', sort_columns=True)


# ### Time spend on different activities
# First it is needed to recode some values (1, 5, 10) to remove the associated text and get only the number.


# ####### QUESTION WITH NUMERICAL ANSWER ABOUT FREQUENCY

# Recategorise the answers into 10 categories

def replace_project(x):

    if pd.isnull(x):
        return
    if x >=1 and x <=3:
        return "1-3"
    elif x >=4 and x <=6:
        return "4-6"
    elif x >=7 and x <=9:
        return "7-9"
    elif x > 10 and x <= 12:
        return "10-12"
    elif x > 13 and x <= 15:
        return "13-15"
    elif x > 16 and x <= 18:
        return "16-18"
    elif x > 19 and x <= 21:
        return "19-21"
    elif x >= 22:
        return ">=22"


# ## 'How many software developers typically work on your projects?',
d = pd.crosstab(df['How many software developers typically work on your projects?'], margins=False, colnames=[''], columns='Number of software developers')
d.plot(kind='bar')


# ## 'How many software projects are you currently involved in?',

df['How many software projects are you currently involved in?[recat]'] = df['How many software projects are you currently involved in?'].apply(replace_project)

d = pd.crosstab(df['How many software projects are you currently involved in?[recat]'], margins=False, colnames=[''], columns='Number of software projects')
d
d.plot(kind='bar')


# How many years of software development experience do you have?
d = pd.crosstab(df['How many years of software development experience do you have?'], colnames=[''], columns='Year of development')
d.plot(kind='bar')

# ## 'How many software components from science.canarie.ca have you integrated into your projects?',


# ########  Questions with a potential 'Other' that may need to be recoded

def explore_other(colname):
    """
    To output the unique value of the column
    and the column '[Other]' associated with it
    :params:
        :colnames str(): string to match the column
    :return: None
    """
    col_other = colname + ' [Other]'
    print('Unique values in the normal column')
    print(df[colname].unique())
    print('Unique values in the other columns')
    print(df[col_other].unique())
    return colname


def recode_values(x, replacement_values, default=False):
    """
    Function to use with an  apply on a Serie to replace values if they match
    the values from the dictionary passed into the argument.
    :params:
        :replacement_values dict(): K are the content to match and values the content
        to replace with
        :default: if a value is given to default, this value will be return, if it is
        false, the passed value is returned instead
    :return:
        :x: the x is returned or the replacement values if found in the dictionary or the
        default if not None.
    """
    if not pd.isnull(x):
        for k in replacement_values:
            if str(k).lower() in str(x).lower():
                return replacement_values[k]
        if default:
            return default
    return x


def merging_others(df, colname, replacement_values=None):
    """
    Function to wrap the different modification applied on
    the columns that have a `other` column associated.
    Only search if some others could be merged with the prexisting answers
    and merge it to into the original column, then transform the column into
    categorical variable
    :params:
        :df pd.df(): dataframe containing the data
        :colname str(): string that have the column header to select the right column
        :replacement_values dict(): contain which value to match in the column 'other' as
        the key and which value to replace with. If it is None, skip the transformation (Default)
    :return:
        :None: The operation is a replace `inplace`
    """
    colname_other = var+ ' [Other]'
    if replacement_values:
        df[colname_other] = df[colname_other].apply(recode_values, args=(replacement_values, 'Other'))
        df[colname].replace('Other', df[colname_other], inplace=True)

    df[colname] = df[colname].str.capitalize().astype('category')


def plot_others(df, columns, colnames=False, sort_order=False, stacked=False):
    """
    Plot the others variables
    :params:
        :df pd.df(): dataframe containing the data
        :colname str(): string that have the column header to select the right column
    """
    if colnames == False:
        colnames = columns
    d = pd.crosstab(df[colname], colnames=['Amount'], columns='counts')
    d.plot(kind='bar', stacked=stacked)
    return d

# ## 'In which discipline is your highest academic qualification?'
# ## 'In which discipline is your highest academic qualification? [Other]'

# In which discipline the participants obtained their highest qualification. The answers were from the [NSERC codes](http://www.nserc-crsng.gc.ca/Help-Aide/Codes-ListeDeCodes_Eng.asp).
# However, it is the option 'Other', followed by a freetext option, which is the most chosen.
# Therefore, before plotting it, we need to clean and merge these answers with the NESRC ones.


var = explore_other('In which discipline is your highest academic qualification?')
discipline_values = {'bioinfo': 'Bioinformatics',
                     'computer': 'Information technology',
                     'informatique': 'Information technology',
                     'history': 'Social sciences and humanities',
                     'biophysics': 'Physics',
                     'software': 'Information and communication services',
                     'dance': 'Social Sciences and Humanities',
                     'musique': 'Social Sciences and Humanities',
                     'agric': 'Agricultural engineering'}
merging_others(df, var, discipline_values)
plot_others(df, var)


# ## 'What development methodology does your current project use?',
# ## 'What development methodology does your current project use? [Other]',
var = explore_other('What development methodology does your current project use?')
methodology_values = {'agile': 'Agile',
                      'scrum': 'Scrum',
                      'depends on the project': 'No formal methodology'}
merging_others(df, var, methodology_values)
plot_others(df, var)

# ## 'What type of organization do you work for?',
# ## 'What type of organization do you work for? [Other]',
var = explore_other('What type of organization do you work for?')
merging_others(df, var)
plot_others(df, var)

# ## 'In which application area do you primarily work?',
# ## 'In which application area do you primarily work? [Other]',
var = explore_other('In which application area do you primarily work?')
merging_others(df, var, discipline_values)
plot_others(df, var)



# ## 'What is the nature of your current employment?',
# ## 'What is the nature of your current employment? [Other]',
var = explore_other('What is the nature of your current employment?')
merging_others(df, var)
plot_others(df, var)



# ## 'What is your Operating System of choice for development?',
# ## 'What is your Operating System of choice for development? [Other]',
var = explore_other('What is your Operating System of choice for development?')
os_deploy_values = {' ': 'Several OS'}
merging_others(df, var, os_deploy_values)
plot_others(df, var)

# ## 'What is your Operating System of choice for deployment?',
# ## 'What is your Operating System of choice for deployment? [Other]',
var = explore_other('What is your Operating System of choice for deployment?')
os_dev_values = {'linux': 'Several OS',
                 'windows': 'Several OS',
                 'mac': 'Several OS'}
merging_others(df, var, os_dev_values)
plot_others(df, var)

# ####### QUESTIONS WITH LIKERT SCALE


# ## 'On average, how much of your time is spent developing software?',
# ## 'On average, how much of your time is spent on research?'
# ## 'On average, how much of the time you spend developing software is spent on new development/enhancement?'
# ## 'On average, how much of the time you spend developing software is devoted to maintenance and support activities?'
# ## 'On average, how much time do you spend on management?'
# ## 'On average, how much time do you spend on other activities?'
time_activity = ['On average, how much of your time is spent developing software?',
                 'On average, how much of your time is spent on research?',
                 'On average, how much of the time you spend developing software is spent on new development/enhancement?',
                 'On average, how much of the time you spend developing software is devoted to maintenance and support activities?',
                 'On average, how much time do you spend on management?',
                 'On average, how much time do you spend on other activities?']

recode_time = {'never': '1',
               '5': '5',
               '10': '10'}
for i in time_activity:
    df[i] = df[i].apply(recode_values, args=(recode_time,)).astype('category')


# Calculate the average of all the time_activity questions and plotting them

df[time_activity].mean(axis=0).plot(kind='bar')
df[time_activity].plot(kind='bar')
df[time_activity]

# ## 'What percentage of these developers are dedicated to the project full time?',

plot_others(df, 'What percentage of these developers are dedicated to the project full time?')


# ####### Questions that are splitted between several questions but about the same concepts


def count_unique_value(df, colnames, rename_columns=False, dropna=False, normalize=False):
    """
    Count the values of different columns and transpose the count
    :params:
        :df pd.df(): dataframe containing the data
        :colnames list(): list of strings corresponding to the column header to select the right column
    :return:
        :result_df pd.df(): dataframe with the count of each answer for each columns
    """
    # Subset the columns
    df_sub = df[colnames]

    if rename_columns is True:
        df_sub.columns = [s.split('[', 1)[1].split(']')[0] for s in colnames]

    # Calculate the counts for them
    df_sub = df_sub.apply(pd.Series.value_counts, dropna=dropna, normalize=normalize)
    # Transpose the column to row to be able to plot a stacked bar chart
    return df_sub.transpose()


# ## 'What would you hope to get out of such an organization? [Networking]',
# ## 'What would you hope to get out of such an organization? [Software collaborations]',
# ## 'What would you hope to get out of such an organization? [Research collaborations]',
# ## 'What would you hope to get out of such an organization? [Training]',
# ## 'What would you hope to get out of such an organization? [Research Software Standards and Interoperability]',
# ## 'What would you hope to get out of such an organization? [Job opportunities]',
# ## 'What would you hope to get out of such an organization? [Other]',

hope = ['What would you hope to get out of such an organization? [Networking]',
        'What would you hope to get out of such an organization? [Software collaborations]',
        'What would you hope to get out of such an organization? [Research collaborations]',
        'What would you hope to get out of such an organization? [Training]',
        'What would you hope to get out of such an organization? [Research Software Standards and Interoperability]',
        'What would you hope to get out of such an organization? [Job opportunities]']

### The column '[Other]' contain only one 'Colloque?' and is therefore discarded
df['What would you hope to get out of such an organization? [Other]'].unique()

# Plotting a bar chart
count_hope = count_unique_value(df, hope, rename_columns=True)
count_hope.plot(kind='bar', colnames=['Which hope to get out of such an organization'], stacked=True)


plot_others(df, 'What would you hope to get out of such an organization? [Networking]', stacked=True)
# ## 'How are your projects typically tested?  [No formal testing]',
# ## 'How are your projects typically tested?  [The developers do their own testing]',
# ## 'How are your projects typically tested?  [Dedicated test engineers]',
# ## 'How are your projects typically tested?  [User testing]',

# ## 'How is your current research software work funded? [Employer]',
# ## 'How is your current research software work funded? [CANARIE]',
# ## 'How is your current research software work funded? [Canadian Foundation for Innovation (CFI)]',
# ## 'How is your current research software work funded? [Canadian Institutes of Health Research (CIHR)]',
# ## 'How is your current research software work funded? [Genome Canada]',
# ## 'How is your current research software work funded? [Natural Sciences and Engineering Research Council of Canada (NSERC)]',
# ## 'How is your current research software work funded? [Social Sciences and Humanities Research Council (SSHRC)]',
# ## 'How is your current research software work funded? [I don't know]',
# ## 'How is your current research software work funded? [Other]',

# Get the list of the associated questions
list_var = ["How is your current research software work funded? [Employer]",
            "How is your current research software work funded? [CANARIE]",
            "How is your current research software work funded? [Canadian Foundation for Innovation (CFI)]",
            "How is your current research software work funded? [Canadian Institutes of Health Research (CIHR)]",
            "How is your current research software work funded? [Genome Canada]",
            "How is your current research software work funded? [Natural Sciences and Engineering Research Council of Canada (NSERC)]",
            "How is your current research software work funded? [Social Sciences and Humanities Research Council (SSHRC)]",
            "How is your current research software work funded? [I don't know]",
            "How is your current research software work funded? [Other]"]
list_values = [s.split('[', 1)[1].split(']')[0] for s in list_var]


# Split the string of the columns name and extract the value within the brackets
def get_type_funding(x, colname):
    if pd.notnull(x):
        replace_value = colname.split('[', 1)[1].split(']')[0]
        return replace_value


for colname in list_var:
    df['test_{}'.format(colname)] = df[colname].apply(get_type_funding, args=(colname,))
df["How is your current research software work funded? [Employer]"].unique
df['test_How is your current research software work funded? [Employer]']

# ## 'What platform(s) are your research software projects deployed on? [Compute Canada HPC]',
# ## 'What platform(s) are your research software projects deployed on? [University computer centre]',
# ## 'What platform(s) are your research software projects deployed on? [Other HPC]',
# ## 'What platform(s) are your research software projects deployed on? [Cloud service]',
# ## 'What platform(s) are your research software projects deployed on? [Stand-alone server(s)]',
# ## 'What platform(s) are your research software projects deployed on? [Laptop/desktop]',
# ## 'What platform(s) are your research software projects deployed on? [Mobile]',
# ## 'What platform(s) are your research software projects deployed on? [Other]',


# ###### QUESTIONS WITH LOGICAL FOLLOWING QUESTIONS

# ## 'Do you work within a group that provides software development help or expertise to researchers from across your organization?',
# ## 'Is there such a group within your organization?',
# ## 'Do you think such a group would have value?',
# ## 'Would you be interested in participating in such a group?',


# ## 'Have you ever presented your software work at a conference or workshop? ',
# ## 'Which conference(s)/workshop(s)?',


# ## 'When you release code, how often do you use an open source license?',
# ## 'List any open repositories (eg. GitHub) to which your software projects have been published.',
# ## 'When you release code or data, how often do you assign a Digital Object Identifier (DOI) to it?',


# ## 'Are you a member of an association of Research Software Developers (e.g UK RSE)?',
# ## 'Would you be interested in joining such an organization if one was formed in Canada?',


# ## 'Do any of your current projects make use of a data management or data archiving component?',
# ## 'Is it part of your software or an external system? (please specify)',


# ## 'Have you contributed software to research that has been published in a journal or presented at a conference?',
# ## 'In general, when your software contributes to a paper, are you acknowledged in that paper?',
# ## 'Are you generally named as the main author of the paper?',
# ## 'Are you generally named as a co-author of the paper?',
# ## 'Are you generally acknowledged in the main paper?',


# ########  QUESTIONS THAT HAVE BEEN ANSWERED BY YES OR NO

# ## 'Do your research software projects typically include a project manager?',

# ## 'Do any of your current projects accommodate the open/public sharing of data?',

# ## 'Is the creation of a Digital Object Identifier (DOI) and metadata for individual assets supported?',

# ## 'Have you developed software that is accessed from multiple institutions?',

# ## 'Do any of your current or previous projects make use of the Canadian Access Federation (CAF) Federated Identity Management (FIM) service?',

# ## 'Have you ever visited the Research Software Registry at science.canarie.ca?',


# ## 'Do you consider yourself a professional software developer?'
df['Do you consider yourself a professional software developer?']
d = pd.crosstab(df['Do you consider yourself a professional software developer?'], margins=False, colnames=[''], columns='Consider as software developer')
d.plot(kind='bar')


# ####### QUESTIONS WITH COMPLETE FREE TEXT

# ## 'What is your current job title?',


# ## 'In your opinion, what are the three most important skills that a Research Software Developer must possess? These skills can be technical and non-technical.',


# ## 'What three skills would you like to acquire or improve to help your work as a Research Software Developer? These skills can be technical and non-technical.',


# ## 'What are the three tools or services you use most often in your software work?',


# ## 'What programming languages do you use in developing research software? Please list in order, beginning with most frequently used.',


# ## 'List any public identity providers (e.g. Google, Facebook, Live, LinkedIn, Twitter, etc.) used in your current or previous projects.',
