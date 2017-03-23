# coding: utf-8

# # CANARIE 2017 -- Analysis of the survey

# This notebook is the first draft to analyse the results from [CANARIE]()

# ## Preparation and filtering of the dataset

# In[1]:

# Load libraries

import pandas as pd
import matplotlib

# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt

#  When using this script with ipython and vim
plt.ion()
plt.show()

import numpy as np


# In[2]:

# Load dataset
df = pd.read_csv('./dataset/2017 Cdn Research Software Developer Survey - Public data.csv')
# Number of row == number of participants
len(df.index)


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

# In[4]:

pd.crosstab(df['In which country do you work?'], columns='Countries')


# There is only 4 others. Which are only one from Japan, 2 from USA and one from UK.

# In[5]:

pd.crosstab(df['In which country do you work? [Other]'], columns='Other countries')


# As this answer are not useful for CANARIE, because these people are not working in Canada, they are removed from the dataset.

# In[6]:

df = df.loc[df['In which country do you work?'] != 'Other']
# Getting the number of row from the reduced dataframe
len(df.index)


# ### Writing software as part of the work
#
# One question asked if the participants write software for research as part of their work.

# In[7]:

pd.crosstab(df['Do you write software for research as part of your job?'], columns='Writing software')


# 13 answered 'No'. This survey, being about researcher that write codes, they are removed from the dataset

# In[8]:

df = df.loc[df['Do you write software for research as part of your job?'] == 'Yes']
# Getting the number of row from the reduced dataframe
len(df.index)


# ## Univariate analysis
#
#

# ### Languages
#
# The survey was in French and in English. The option choose by the participant was collected. It is possible then to see the proportion of participants that answered the survey in French or in English

# In[9]:

pd.crosstab(df['Start language'], columns='Language')


# In[10]:

df['Start language'].value_counts().plot(kind='bar')


# ### Education level
# The question asked the level of education

# In[11]:

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


# In[12]:

df['What is the highest level of education you have attained?'].value_counts().plot(kind='barh', sort_columns=True)


# ### Discipline
#
# In which discipline the participants obtained their highest qualification. The answers were from the [NSERC codes](http://www.nserc-crsng.gc.ca/Help-Aide/Codes-ListeDeCodes_Eng.asp).
# However, it is the option 'Other', followed by a freetext option, which is the most chosen.
# Therefore, before plotting it, we need to clean and merge these answers with the NESRC ones.

# #### Discipline -- Other
#
#

# In[19]:

df = pd.read_csv('./dataset/2017 Cdn Research Software Developer Survey - Public data.csv')
# df['In which discipline is your highest academic qualification? [Other]'] = df['In which discipline is your highest academic qualification? [Other]'].str.lower().astype('category')


# # Recode the different categories to an existing (High level NSERC code).
def recode_disciplines(x):
    """
    Recode values from Disciplines -- Others to match
    prexisting categories from NSERC code
    """
    dict_of_replacement = {'bioinfo': 'Bioinformatics',
                           'computer': 'Information technology',
                           'informatique': 'Information technology',
                           'history': 'Social sciences and humanities',
                           'biophysics': 'Physics',
                           'software': 'Information and communication services',
                           'dance': 'Social Sciences and Humanities',
                           'musique': 'Social Sciences and Humanities'}
    if not pd.isnull(x):
        for k in dict_of_replacement:
            if k.lower() in str(x).lower():
                return dict_of_replacement[k].capitalize()

        return 'Other'

# # Apply the re encoding to the column discipline Other
df['In which discipline is your highest academic qualification? [Other]'] = df['In which discipline is your highest academic qualification? [Other]'].apply(recode_disciplines)

# Now it just need to merge the two discipline column into one

# In[15]:

df['In which discipline is your highest academic qualification?'].replace('Other',df['In which discipline is your highest academic qualification? [Other]'], inplace=True)

df['In which discipline is your highest academic qualification?'] = df['In which discipline is your highest academic qualification?'].apply(str.capitalize).astype('category')



# In[82]:

pd.crosstab(df['In which discipline is your highest academic qualification?'], columns='Disciplines')


# In[83]:

df['In which discipline is your highest academic qualification?'].value_counts().plot(kind='barh', sort_columns=True)


# In[84]:
