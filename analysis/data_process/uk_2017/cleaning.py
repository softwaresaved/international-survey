#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pandas as pd
import numpy as np
import matplotlib
from include import plotting
# When using Ipython within vim
matplotlib.use('TkAgg')

# When using within jupyter
# get_ipython().magic('matplotlib inline')  # Activat that line to use in Jupyter

import matplotlib.pyplot as plt
#  When using this script with ipython and vim
plt.ion()
plt.show()
pd.set_option('display.max_rows', 300)
# Load dataset
df = pd.read_csv('./dataset/raw_results-survey245554.csv')
# Number of row == number of participants
len(df.index)

# # Drop unused fields
columns_to_drop = ['Response ID', 'Date submitted', 'Start language',
                   'Date started', 'Date last action', 'Referrer URL']
df = df.drop(columns_to_drop, axis=1)


# # The last page is the last page the participants reached. To
# # do a compromise between keeping some and getting rid of the participants that haven't complete
# # enough answers
nb_answer = pd.DataFrame(df['Last page'].value_counts()).sort_index(ascending=True)
nb_answer['cumfreq'] = nb_answer.cumsum()
nb_answer.plot(kind='bar')

# Overall, as soon as the participants passed the first page, they reached the last page.
# In consequence, if a participant passed the first page, (s)he is kept.
df = df.loc[df['Last page']> 1]
# This reduce the size of the population to:
len(df.index)

# # Check if there is Prefer not to answer
if len(df.loc[:, df.columns.to_series().str.contains('Prefer not to answer').tolist()].columns) > 0:
    # Replacing all the answer "Prefer not to answer" by NaN, as they are not useful in the analysis
    df.replace('Prefer not to answer', np.NaN, inplace=True)

# Some columns have a unbreakable space in their name, replace it
df.columns = df.columns.str.replace('\xa0', '')

## Replace all ending white space
df.columns = df.columns.str.strip()

# Replace Yes and No to Boolean when it is possible
y_n_bool = {'Yes': True, 'No': False}
df.replace(y_n_bool)



def check_similar_q(col, previous_q=None, previous_col=None, current_list=None):
    last_bit = re.search(re_match_brac, col)
    if last_bit:
        first_q = col.replace(last_bit[1], '')
        if first_q == previous_q:
            if set(df[col].unique()) == set(df[previous_col].unique()):
                previous_col = col
                previous_q = first_q
                print(last_bit[1])


re_match_brac = '\[([^]]+)\]'
open_question = list()
previous_q = None
previous_col = None
current_list = None
for col in df.columns:
    previous_q, previous_col, current_list = check_similar_q(col,
                                                             previous_q,
                                                             previous_col,
                                                             current_list)




df['Please rate the following propositions. There are no right or wrong answers [I am satisfied with the encouragement from my supervisor/line manager while doing my job]'].unique()

list(df.columns)

 'In which country do you work?',
 'What is the highest qualification you have obtained?',
 'What is the highest qualification you have obtained?    [Other]',
 'In which subject is your highest academic qualification?',
 'Enter your academic subject',
 'Do you hold any professional qualifications?',
 'Do you write code as part of your job?',
 'Who uses the code that you write? []',
 'Do you consider yourself a professional software developer?',
 'How many years of software development experience do you have?',
 'In an average month, how much time do you spend on: [Software development]',
 'In an average month, how much time do you spend on: [Research]',
 'In an average month, how much time do you spend on: [People management]',
 'In an average month, how much time do you spend on: [Project management]',
 'In an average month, how much time do you spend on: [Teaching]',
 'In an average month, how much time do you spend on: [Other activities]',
 'What type of organisation do you work for?',
 'Which university?',
 'Which university? [Other]',
 'Please enter the university',
 'Which organisation do you workfor?',
 'What is your official job title',
 'Are you known in your group by a different job title? If so, please enter the job title you use',
 'Do you work full time or part time?',
 'What type ofcontract are you employed on?',
 'What is the duration of your current contract in months?',
 'When did you start your contract',
 'In which disciplines do you work (select as many as apply)? [Accounting & Finance]',
 'In which disciplines do you work (select as many as apply)? [Aeronautical & Manufacturing Engineering]',
 'In which disciplines do you work (select as many as apply)? [Agriculture & Forestry]',
 'In which disciplines do you work (select as many as apply)? [American Studies]',
 'In which disciplines do you work (select as many as apply)? [Anatomy & Physiology]',
 'In which disciplines do you work (select as many as apply)? [Anthropology]',
 'In which disciplines do you work (select as many as apply)? [Architecture]',
 'In which disciplines do you work (select as many as apply)? [Art & Design]',
 'In which disciplines do you work (select as many as apply)? [Biological Sciences]',
 'In which disciplines do you work (select as many as apply)? [Business & Management Studies]',
 'In which disciplines do you work (select as many as apply)? [Chemical Engineering]',
 'In which disciplines do you work (select as many as apply)? [Chemistry]',
 'In which disciplines do you work (select as many as apply)? [Civil Engineering]',
 'In which disciplines do you work (select as many as apply)? [Classics & Ancient History]',
 'In which disciplines do you work (select as many as apply)? [Communication & Media Studies]',
 'In which disciplines do you work (select as many as apply)? [Complementary Medicine]',
 'In which disciplines do you work (select as many as apply)? [Computer Science]',
 'In which disciplines do you work (select as many as apply)? [Counselling]',
 'In which disciplines do you work (select as many as apply)? [Criminology]',
 'In which disciplines do you work (select as many as apply)? [Dentistry]',
 'In which disciplines do you work (select as many as apply)? [East & South Asian Studies]',
 'In which disciplines do you work (select as many as apply)? [Economics]',
 'In which disciplines do you work (select as many as apply)? [Education]',
 'In which disciplines do you work (select as many as apply)? [Electrical & Electronic Engineering]',
 'In which disciplines do you work (select as many as apply)? [English]',
 'In which disciplines do you work (select as many as apply)? [Fashion]',
 'In which disciplines do you work (select as many as apply)? [Food Science]',
 'In which disciplines do you work (select as many as apply)? [French]',
 'In which disciplines do you work (select as many as apply)? [Geography & Environmental Sciences]',
 'In which disciplines do you work (select as many as apply)? [Geology]',
 'In which disciplines do you work (select as many as apply)? [General Engineering]',
 'In which disciplines do you work (select as many as apply)? [German]',
 'In which disciplines do you work (select as many as apply)? [History]',
 'In which disciplines do you work (select as many as apply)? [History of Art, Architecture & Design]',
 'In which disciplines do you work (select as many as apply)? [Hospitality, Leisure, Recreation & Tourism]',
 'In which disciplines do you work (select as many as apply)? [Iberian Languages/Hispanic Studies]',
 'In which disciplines do you work (select as many as apply)? [Land & Property Management]',
 'In which disciplines do you work (select as many as apply)? [Law]',
 'In which disciplines do you work (select as many as apply)? [Librarianship & Information Management]',
 'In which disciplines do you work (select as many as apply)? [Linguistics]',
 'In which disciplines do you work (select as many as apply)? [Marketing]',
 'In which disciplines do you work (select as many as apply)? [Materials Technology]',
 'In which disciplines do you work (select as many as apply)? [Mathematics]',
 'In which disciplines do you work (select as many as apply)? [Mechanical Engineering]',
 'In which disciplines do you work (select as many as apply)? [Medicine]',
 'In which disciplines do you work (select as many as apply)? [Middle Eastern and African Studies]',
 'In which disciplines do you work (select as many as apply)? [Music]',
 'In which disciplines do you work (select as many as apply)? [Nursing]',
 'In which disciplines do you work (select as many as apply)? [Ophthalmics]',
 'In which disciplines do you work (select as many as apply)? [Pharmacology & Pharmacy]',
 'In which disciplines do you work (select as many as apply)? [Philosophy]',
 'In which disciplines do you work (select as many as apply)? [Physics and Astronomy]',
 'In which disciplines do you work (select as many as apply)? [Physiotherapy]',
 'In which disciplines do you work (select as many as apply)? [Politics]',
 'In which disciplines do you work (select as many as apply)? [Psychology]',
 'In which disciplines do you work (select as many as apply)? [Robotics]',
 'In which disciplines do you work (select as many as apply)? [Russian & East European Languages]',
 'In which disciplines do you work (select as many as apply)? [Social Policy]',
 'In which disciplines do you work (select as many as apply)? [Social Work]',
 'In which disciplines do you work (select as many as apply)? [Sociology]',
 'In which disciplines do you work (select as many as apply)? [Sports Science]',
 'In which disciplines do you work (select as many as apply)? [Theology & Religious Studies]',
 'In which disciplines do you work (select as many as apply)? [Town & Country Planning and Landscape Design]',
 'In which disciplines do you work (select as many as apply)? [Veterinary Medicine]',
 'In which disciplines do you work (select as many as apply)? [Youth Work]',
 'In which disciplines do you work (select as many as apply)? [Other]',
 'Where was your previous job based?',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 1]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 2]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 3]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 4]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 5]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 6]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 7]',
 'Rank the following factors dependent on how strongly they influenced your decision to accept your current position [Rank 8]',
 'Do you always work with the same researcher(s), or do you regularly change theresearcher(s) you work with?',
 'Do you work for a Research Software Group?',
 'Hasyour software contributed to research that has been publishedina journal or at a conference?',
 'In general, when your software contributes to a paper, are you acknowledged in that paper?',
 'Are you generally named as the main author of the paper?',
 'Are you generally named as a co-author of the paper?',
 'Are you generally acknowledged in the main text of the paper?',
 'Have you ever presented your software work at a conference or workshop?',
 'Which conferences or workshops?',
 'How many software projects are you currently involved with?',
 'What is the bus factor of your most important software project?',
 'Is there atechnical handover plan for your most important software project?',
 'In general, what sort of testing do you conduct on your software? (check all that apply) [No formal testing]',
 'In general, what sort of testing do you conduct on your software? (check all that apply) [Developers conduct testing]',
 'In general, what sort of testing do you conduct on your software? (check all that apply) [Test engineers conduct testing]',
 'In general, what sort of testing do you conduct on your software? (check all that apply) [Users conduct testing]',
 'In general, what sort of testing do you conduct on your software? (check all that apply) [Other]',
 'Have you ever released your software under an open-source licence?',
 "How often do you release the software projects you've worked on under an open-source licence? []",
 'Have you ever used a Digital Object Identifier (DOI)to identify your software?',
 'How often do you associate your software with aDigital Object Identifier (DOI)? []',
 'Have you ever trained researchers in computational techniques?',
 'On average, how many times a year do you take part in providing training?',
 'What training programs are you involved with (comma separated list)?',
 'Do you know the source of the funding used to support you and your current, largest project?',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [I volunteer my time]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Donation button]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Crowdfunding (one-time)]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Crowdfunding (recurring)]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Books & merchandise]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Advertising & sponsorships]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Industry support]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Consulting & services]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Grants]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [SaaS]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Membership]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Dual license]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Open core]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Foundations & consortiums]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Venture capital]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Trademark licensing & franchising]',
 'Which of the following sources are used to pay for your effort as an RSE/equivalent? [Other]',
 'Which of the following sources are used to fundyour current, largest project? [Volunteers]',
 'Which of the following sources are used to fundyour current, largest project? [Donation button]',
 'Which of the following sources are used to fundyour current, largest project? [Crowdfunding (one-time)]',
 'Which of the following sources are used to fundyour current, largest project? [Crowdfunding (recurring)]',
 'Which of the following sources are used to fundyour current, largest project? [Books & merchandise]',
 'Which of the following sources are used to fundyour current, largest project? [Advertising & sponsorships]',
 'Which of the following sources are used to fundyour current, largest project? [Industry support]',
 'Which of the following sources are used to fundyour current, largest project? [Consulting & services]',
 'Which of the following sources are used to fundyour current, largest project? [Grants]',
 'Which of the following sources are used to fundyour current, largest project? [SaaS]',
 'Which of the following sources are used to fundyour current, largest project? [Membership]',
 'Which of the following sources are used to fundyour current, largest project? [Dual license]',
 'Which of the following sources are used to fundyour current, largest project? [Open core]',
 'Which of the following sources are used to fundyour current, largest project? [Foundations & consortiums]',
 'Which of the following sources are used to fundyour current, largest project? [Venture capital]',
 'Which of the following sources are used to fundyour current, largest project? [Trademark licensing & franchising]',
 'Which of the following sources are used to fundyour current, largest project? [Other]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [My previous project is less than 3 years old]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Volunteers]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Donation button]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Crowdfunding (one-time)]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Crowdfunding (recurring)]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Books & merchandise]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Advertising & sponsorships]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Industry support]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Consulting & services]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Grants]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [SaaS]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Membership]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Dual license]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Open core]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Foundations & consortiums]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Venture capital]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Trademark licensing & franchising]',
 'Which of the following sources were used to fundyour current, largest project three years ago? [Other]',
 'Please rate the following propositions. There are no right or wrong answers [I find real enjoyment in my job]',
 'Please rate the following propositions. There are no right or wrong answers [I can think of a number of organisations that would probably offer me a job]',
 'Please rate the following propositions. There are no right or wrong answers [I am satisfied with the recognition I receive from my supervisor/line manager for doing my job]',
 'Please rate the following propositions. There are no right or wrong answers [Most days I am enthusiastic about my job]',
 'Please rate the following propositions. There are no right or wrong answers [I am satisfied with a word of thanks from my supervisor/line manager]',
 'Please rate the following propositions. There are no right or wrong answers [Do you receive sufficient information on the results of your work?]',
 'Please rate the following propositions. There are no right or wrong answers [How often do you consider leaving your job?]',
 'Please rate the following propositions. There are no right or wrong answers [Do you get the opportunity to check on how well you are doing your work?]',
 'Please rate the following propositions. There are no right or wrong answers [Do you have access to sufficient data and information to do your work?]',
 'Please rate the following propositions. There are no right or wrong answers [How often do you dream about getting another job that will better suit your needs?]',
 'Please rate the following propositions. There are no right or wrong answers [Do your colleagues inform you about how well you are doing your work?]',
 'Please rate the following propositions. There are no right or wrong answers [My experience is in demand on the labour market]',
 'Please rate the following propositions. There are no right or wrong answers [My current job satisfies my personal needs]',
 'Please rate the following propositions. There are no right or wrong answers [I am satisfied with the compliments from my supervisor/line manager concerning my work]',
 'Please rate the following propositions. There are no right or wrong answers [I feel satisfied with my job]',
 'Please rate the following propositions. There are no right or wrong answers [It would not be very difficult for me to get an equivalent job in a different organisation]',
 'Please rate the following propositions. There are no right or wrong answers [Does your work provide you with direct feedback on how well you are doing?]',
 'Please rate the following propositions. There are no right or wrong answers [How often do you look forward to another day at work?]',
 'Please rate the following propositions. There are no right or wrong answers [Do you receive sufficient information on the purpose of your work?]',
 'Please rate the following propositions. There are no right or wrong answers [How often do you feel frustrated when not given the opportunity to achieve your personal work-related goals?]',
 'Please rate the following propositions. There are no right or wrong answers [Does your supervisor/line manager inform you about how well you are doing your work?]',
 'Please rate the following propositions. There are no right or wrong answers [I like my job more than average]',
 'Please rate the following propositions. There are no right or wrong answers [I would accept another job at the same compensation level if I was offered it]',
 "Please rate the following propositions. There are no right or wrong answers [I am satisfied with my supervisor/line manager's confidence in me]",
 'Please rate the following propositions. There are no right or wrong answers [Given my qualifications and experience, getting a new job would not be very hard at all]',
 'Please rate the following propositions. There are no right or wrong answers [I am satisfied with the encouragement from my supervisor/line manager while doing my job]',
 'In general, how satisfied are you with: [Your current position]',
 'In general, how satisfied are you with: [Your career]',
 'Please select your gender',
 'Please select your age',
 'How would you describe your ethnic origin? This refers to people who share the same cultural background and identity, not country of birth or nationality.',
 'Do you have a condition that is defined as a disability by the Equality Act 2010*',
 'Please select the range of your salary',
 'What Operating System do you prefer to use at work?',
 'What programming languages do you use at work? (Select as many as apply) [Assembly]',
 'What programming languages do you use at work? (Select as many as apply) [C]',
 'What programming languages do you use at work? (Select as many as apply) [C#]',
 'What programming languages do you use at work? (Select as many as apply) [C++]',
 'What programming languages do you use at work? (Select as many as apply) [Clojure]',
 'What programming languages do you use at work? (Select as many as apply) [CoffeeScript]',
 'What programming languages do you use at work? (Select as many as apply) [Common Lisp]',
 'What programming languages do you use at work? (Select as many as apply) [CUDA]',
 'What programming languages do you use at work? (Select as many as apply) [Dart]',
 'What programming languages do you use at work? (Select as many as apply) [Elixir]',
 'What programming languages do you use at work? (Select as many as apply) [Erlang]',
 'What programming languages do you use at work? (Select as many as apply) [F#]',
 'What programming languages do you use at work? (Select as many as apply) [FORTRAN]',
 'What programming languages do you use at work? (Select as many as apply) [Go]',
 'What programming languages do you use at work? (Select as many as apply) [Groovy]',
 'What programming languages do you use at work? (Select as many as apply) [Hack]',
 'What programming languages do you use at work? (Select as many as apply) [Haskell]',
 'What programming languages do you use at work? (Select as many as apply) [Java]',
 'What programming languages do you use at work? (Select as many as apply) [JavaScript]',
 'What programming languages do you use at work? (Select as many as apply) [Julia]',
 'What programming languages do you use at work? (Select as many as apply) [Lua]',
 'What programming languages do you use at work? (Select as many as apply) [Markup languages (HTML, markdown,...)]',
 'What programming languages do you use at work? (Select as many as apply) [Matlab]',
 'What programming languages do you use at work? (Select as many as apply) [Objective-C]',
 'What programming languages do you use at work? (Select as many as apply) [Perl]',
 'What programming languages do you use at work? (Select as many as apply) [PHP]',
 'What programming languages do you use at work? (Select as many as apply) [Python]',
 'What programming languages do you use at work? (Select as many as apply) [R]',
 'What programming languages do you use at work? (Select as many as apply) [Ruby]',
 'What programming languages do you use at work? (Select as many as apply) [Rust]',
 'What programming languages do you use at work? (Select as many as apply) [Scala]',
 'What programming languages do you use at work? (Select as many as apply) [Smalltalk]',
 'What programming languages do you use at work? (Select as many as apply) [SQL]',
 'What programming languages do you use at work? (Select as many as apply) [Swift]',
 'What programming languages do you use at work? (Select as many as apply) [Unix Shell Scripting]',
 'What programming languages do you use at work? (Select as many as apply) [TypeScript]',
 'What programming languages do you use at work? (Select as many as apply) [VB.NET]',
 'What programming languages do you use at work? (Select as many as apply) [VBA]',
 'What programming languages do you use at work? (Select as many as apply) [Visual Basic]',
 'What programming languages do you use at work? (Select as many as apply) [Other]',
 'Are you a member of the UK RSE Association? (Members are people who have signed up to the UK RSE mailing list at www.rse.ac.uk)',
 'How do you meet other RSEs? [UK RSE Association]',
 'How do you meet other RSEs? [Local RSE group/network]',
 'How do you meet other RSEs? [N/A]',
 'How do you meet other RSEs? [Other]',
 'What skills would you like to acquire or improve to helpyour work as aResearch Software Engineer? The skills can be technical and non-technical. [Skill 1]',
 'What skills would you like to acquire or improve to helpyour work as aResearch Software Engineer? The skills can be technical and non-technical. [Skill 2]',
 'What skills would you like to acquire or improve to helpyour work as aResearch Software Engineer? The skills can be technical and non-technical. [Skill 3]',
 'How did you learn the skills you need to become an RSE?',
 'Total time',
 'Group time: Questions about you',
 'Question time: socio1',
 'Question time: edu1',
 'Question time: edu2',
 'Question time: edu3',
 'Question time: edu4',
 'Question time: rse1',
 'Question time: rse3',
 'Question time: soft2can',
 'Question time: soft1can',
 'Question time: time1can',
 'Group time: Your current employment',
 'Question time: currentEmp1',
 'Question time: currentEmp2',
 'Question time: currentEmp3',
 'Question time: currentEmp4',
 'Question time: currentEmp5',
 'Question time: currentEmp6',
 'Question time: currentEmp12',
 'Question time: currentEmp10',
 'Question time: currentEmp11',
 'Question time: currentEmp9',
 'Question time: currentEmp13',
 'Group time: Your employment history',
 'Question time: prevEmp1',
 'Question time: prevEmp2',
 'Group time: Your working practices',
 'Question time: currentWork1',
 'Question time: currentWork2',
 'Question time: paper1',
 'Question time: paper2',
 'Question time: paper3',
 'Question time: paper4',
 'Question time: paper5',
 'Question time: conf1can',
 'Question time: conf2can',
 'Question time: proj1can',
 'Question time: stability1',
 'Question time: stability2',
 'Question time: proj4can',
 'Question time: open01can',
 'Question time: open1can',
 'Question time: open03can',
 'Question time: open3can',
 'Question time: train1',
 'Question time: train2',
 'Question time: train3',
 'Question time: fund1',
 'Question time: fund2',
 'Question time: fund3',
 'Question time: fund4',
 'Group time: Your perception of your current position',
 'Question time: likertagree2',
 'Question time: likerttime1',
 'Question time: likertagree1',
 'Question time: likertime2',
 'Question time: likertagree3',
 'Question time: satisGen1',
 'Group time: Demographic questions',
 'Question time: socio2',
 'Question time: socio3',
 'Question time: socio5',
 'Question time: disa1',
 'Question time: socio4',
 'Group time: Final questions',
 'Question time: tool2',
 'Question time: tool4can',
 'Question time: ukrse1',
 'Question time: ukrse2',
 'Question time: skill2',
 'Question time: ukrse3'
