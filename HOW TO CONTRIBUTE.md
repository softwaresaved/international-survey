# How to contribute

The following are instructions on how to work with us on a new survey. Below, you will find more detail about the contents of this repository and how the surveys are conducted.


## Creating a new survey

We are flexible to adapting the survey to your needs. However, we also want to make the inter-country analysis as easy as possible. For this reason, we have a few guiding principles that - in a perfect world - we can agree to stick to:

1. We make as few adaptations as possible to the core questions
1. We apply for ethics approval at the University of Southampton (where Simon Hettrick and Olivier Philippe are based) to run the survey.
1. We run the survey under the University of Southampton's Limesurvey account so that all data is processed in the same way (and we pay for it)
1. We store all anonymised data on Zenodo under a Creations Commons By Attribution licence with ourselves and yourself as joint authors
1. We destroy the data set with with non-anonymised data (i.e. those with email addresses) because it's no longer necessary


### How to create a survey for your country

What we need from you:

1. There is the general question file.

2. Locate the directory related to your country's survey in [survey creation](https://github.com/softwaresaved/international-survey/tree/master/survey_creation).
3. In your country directory, you will find two folders:
   1. listAnswers directory: containing csv files that contain answers for questions where a list of potential answers is presented. This is specific to your country.

4. The listAnswers folder contains csv files that hold information that is relevant to the UK (e.g. all UK universities, standard UK academic salary ranges in pounds). We need you to provide answers that are relevant to your country (e.g. all German universities, or standard Dutch academic salary ranges in Euros).

1. The Text directory contains the welcome and end messages that are presented at the start and end of the survey. Please review these and decide on whether you are happy with the content

1. Now that the content of the questions, answers and welcome and end text is to everyone's approval, we need you to translate the text into your native language(s).

1. Once we are all happy that the survey is ready, you will disseminate the survey in your own country

Where to put translated text:

1. Translated questions should be added to the "questions_<country>_<year>.csv" under one or more of the columns "Trans lang 1", "Trans lang 2", "Trans lang 3" (contact us if you have more than three national languages).
1. Translated welcome and end text should replace the English-language version in the appropriate files in the Text directory.
1. Translated lists of answers should replace the English-language versions in the csv files held in the listAnswers directory. If multiple languages are to be contained in the file, please separate translated answers with semi-colons.


## Explanation of the columns in questions csv

We now provide some more detail about the columns in the questions csv file. You will not need most of this information, but we want to provide it for comprehensiveness.

* **section**: The survey is split into sections (6 usually) each of which contains a number of questions.

* **code**: This is the unique ID for each question. It mandatory because it is used to compare the same questions across results from different countries and different years. When adding a new question, please follow the format for the Code, which is:

```<short description><number><country code>
```

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

* **answer_file**: This column gives the name of the csv file located in `listAnswers` folder, where the appropriate answers options are stored.

* **{country_code}**: These columns are set up when a country is added to the survey. In their respective column, each country specify if they want to have the question in their survey by writting a 'Y' in the appropriate cell. If no value is set up, it assumes the questions will not be shown in the version of the survey for the country.


* **condition**: This indicates whether a question only appears if an specific answer was given to a previous question. The formatting needs to be as follow:
    ```($code_question $operator $answer) $boolean ($code_question $operator $answer)
    ```
    * The `$code_question` can be found in the column `code`
    * The `$operator` can be: `==`, `!=`, `>`, `<`, `<=`, `>=`
    * the `boolean` can be: `OR`, `AND`
    It is important to stick to this formating. Any condition that does not follow these rules will not work for the survey.

* **other**: Indicates when a field 'other' needs to be added to the answers. Works only for the some type of questions ('one choice', 'multiple choice'). The only value it can takes is 'Y'. There is no need to specify anything when 'other' is not wanted.

* **random**: Indicate that the questions need to be randomised. Works only when several questions sharing the same `answer_file` AND the same `code` (without including the number) AND if the questions is 'Y/N/NA' or 'Likert. The only value it can takes is 'Y'. There is no need to specify anything when 'other' is not wanted.

* **order_question**: Boolean column to know if the order of the answer should be following the answers given in the answer_file of should be ordered according to the question numbers.

* **lang_trans{1-3}**: Column to write down the translation of the question.


# Organisation of the repository

* **analysis**: a directory containing Jupyter notebooks covering the results of the analysis from each country and year
* **survey_creation**: files and dirs used to create surveys for new countries or for new years


# Technical solution

We decided to use the open source [limesurvey](http://www.limesurvey.org) service to create the survey. This solution presents advantages in term of price and variety of hosting solutions.

The collaboration will be done on this repository to ensure access to the information for every one and respect the principle of transparency.
