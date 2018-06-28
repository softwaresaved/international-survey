# How to contribute

The following are instructions on how to work with us on a new survey. Below, you will find more detail about the contents of this repository and how the surveys are conducted.
The underlying idea is we use a central csv file containing all the questions and several csv files containing the potential answers. It helps to keep track with Github of any modifications.
Later these files are transformed into a tsv file compatible for limesurvey. It create one survey with different questions and answers based on which country the participant is working in.

## Rules we try to follow

We are flexible to adapting the survey to your needs. However, we also want to make the inter-country analysis as easy as possible. For this reason, we have a few guiding principles that - in a perfect world - we can agree to stick to:

1. We make as few adaptations as possible to the core questions
1. We apply for ethics approval at the University of Southampton (where Simon Hettrick and Olivier Philippe are based) to run the survey.
1. We run the survey under the University of Southampton's Limesurvey account so that all data is processed in the same way (and we pay for it)
1. We store all anonymised data on Zenodo under a Creations Commons By Attribution licence with ourselves and yourself as joint authors
1. We destroy the data set with with non-anonymised data (i.e. those with email addresses) because it's no longer necessary

## Material

If you want to adapt the survey for your country, here the presentation of the different resources used.

1. The most important file is the [question file](https://github.com/softwaresaved/international-survey/blob/master/survey_creation/2018/questions.csv) that contains all the questions for all the surveys. The explanation of different columns are given below ([description below](#explanation-of-the-columns-in-questions-csv)). In this file you will be able to decide which question you want to include or no. It is also possible to add more question.

1. The [answer folder](https://github.com/softwaresaved/international-survey/blob/2018-survey/survey_creation/2018/questions.csv) contains all the answer for the different questions that requires them. For instance the question about the type of contract will link to a file type_contract. This file is a csv file holding all the potential answers shown to the participants.

1. The [text folder](https://github.com/softwaresaved/international-survey/tree/2018-survey/survey_creation/2018/texts) contains the welcome message and the end message.

1. Each country also has a specific folder. In this folder, each country can add questions files that will be specific to their country. For instance, the question "In which university do you work?" needs to have a specific list of university for each country. In that case each country needs to have a file called `universities.csv` in their folder. The creation of the survey will always overwrite the answers found in the default answer folder in the case a file with the same name is found in the country folder.

## Explanation of the columns in questions csv

We now provide some more detail about the columns in the questions csv file. You will not need most of this information, but we want to provide it for comprehensiveness.

* **section**: The survey is split into sections (6 usually) each of which contains a number of questions.

* **code**: This is the unique ID for each question. It mandatory because it is used to compare the same questions across results from different countries and different years. When adding a new question, please follow the format for the Code, which is: `<short description><number><country code>`

* **question**: The question in English as presented to the participant

* **answer_format**: This describes the format of the answers to the question. There are different options:

   * `Y/N/NA`: Yes or No format (with optional N/A when applicable)
   * `FREETEXT`: An open text based answer added by the participant
   * `FREENUMERIC`: A field where participant can encode any number
   * `DATETIME`: A field that only date can be chosen
   * `ONE CHOICE`: A list of answers the participant can choose from
   * `MULTIPLE CHOICE`: A list of answers the participant can choose from. (S)He can choose as many as (s)he wants.
   * `LIKERT`: any type of likert scale.
   * `RANKING`: A list of answers the participants need to rank in order

* **answer_file**: This column gives the name of the csv file located in [answer folder](https://github.com/softwaresaved/international-survey/blob/2018-survey/survey_creation/2018/questions.csv), where the appropriate answers options are stored.

* **{country_code}**: These columns are set up when a country is added to the survey. In their respective column, each country specify if they want to have the question in their survey by writting a 'Y' in the appropriate cell. If no value is set up, it assumes the questions will not be shown in the version of the survey for the country.


* **condition**: This indicates whether a question only appears if an specific answer was given to a previous question. The formatting needs to be as follow: `($code_question $operator $answer) $boolean ($code_question $operator $answer)`
    * The `$code_question` can be found in the column `code`
    * The `$operator` can be: `==`, `!=`, `>`, `<`, `<=`, `>=`
    * the `boolean` can be: `OR`, `AND`
    It is important to stick to this formating. Any condition that does not follow these rules will not work for the survey.

* **other**: Indicates when a field 'other' needs to be added to the answers. Works only for the some type of questions ('one choice', 'multiple choice'). The only value it can takes is 'Y'. There is no need to specify anything when 'other' is not wanted.

* **country_specific** * Indicate if a questions is by nature specific to a country (i.e. the list of university)

* **random**: Indicate that the questions need to be randomised. Works only when several questions sharing the same `answer_file` AND the same `code` (without including the number) AND if the questions is 'Y/N/NA' or 'Likert. The only value it can takes is 'Y'.

* **trans_{1-3}**: Column to write down the translation of the question.

## Case of translation

1. Translated welcome and end text should be placed in the same folder as the english version, in the [text folder](https://github.com/softwaresaved/international-survey/tree/2018-survey/survey_creation/2018/texts).
1. Translated questions should be done in the main [question file](https://github.com/softwaresaved/international-survey/blob/master/survey_creation/2018/questions.csv) under the columns (`trans_1`, `trans_2`, `trans_3`)
1. Translated answer should be put into each answers file and be semi colon separated.

# Organisation of the repository

* **analysis**: a directory containing Jupyter notebooks covering the results of the analysis from each country and year
* **survey_creation**: files and dirs used to create surveys for new countries or for new years


# Technical solution

We decided to use the open source [limesurvey](http://www.limesurvey.org) service to create the survey. This solution presents advantages in term of price and variety of hosting solutions.

The collaboration will be done on this repository to ensure access to the information for every one and respect the principle of transparency.
