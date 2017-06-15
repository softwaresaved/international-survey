# International collaboration for survey

In 2016 the Software Sustainability Institute ran the first survey of Research Software Engineers (RSEs) - the people who write code in academia. This produced the first insight into the demographics, job satisfaction, and practices of RSEs. To support and broaden this work, the Institute will run the UK survey every year and - it is hoped - will expand the survey so that insight and comparison can be made across different countries. Ultimately, we hope that these results, the anonymised version of which will all be open licensed, will act as a valuable resource to understand and improve the working conditions for RSEs.

In 2017, we have conducted surveys in the UK and in Canada. We now have German and Dutch collaborators, and we are looking at expanding into Norway, South Africa and the US.

# Working with us on a new survey

The following are instructions on how to work with us on a new survey. Below, you will find more detail about the contents of this repository and how the surveys are conducted.

## Creating a new survey

We are flexible to adapting the survey to your needs. However, we also want to make the inter-country analysis as easy as possible. For this reason, we have a few guiding principles that - in a perfect world - we can agree to stick to:

1. We make as few adaptations as possible to the core questions
1. We apply for ethics approval at the University of Southampton (where Simon Hettrick and Olivier Philippe are based) to run the survey.
1. We run the survey under the University of Southampton's Limesurvey account so that all data is processed in the same way (and we pay for it)
1. We store all anonymised data on Zenodo under a Creations Commons By Attribution licence with ourselves and yourself as joint authors
1. We destroy the data set with with non-anonymised data (i.e. those with email addresses) because it's no longer necessary

What we need from you:

1. Locate the directory related to your country's survey in [survey creation](https://github.com/softwaresaved/international-survey/tree/master/survey_creation).
1. In your country directory, you will find three files
   1. listAnswers directory: containing csv file that contain answers for questions where a list of potential answers is presented
   1. Text directory: containing md files that contain the welcome and end message for the survey
   1. question csv file: containing a csv that contains the core questions for your survey
1. Review the core questions (in "questions_<country>_<year>.csv") and decide if there are any changes (additions, removals or edits) that you think will be necessary. Simon Hettrick and Olivier Philippe at the Institute will organise a discussion with you to discuss these changes.
1. The listAnswers folder contains csv files that hold information that is relevant to the UK (e.g. all UK universities, standard UK academic salary ranges in pounds). We need you to provide answers that are relevant to your country (e.g. all German universities, or standard Dutch academic salary ranges in Euros).
1. The Text directory contains the welcome and end messages that are presented at the start and end of the survey. Please review these and decide on whether you are happy with the content
1. Now that the content of the questions, answers and welcome and end text is to everyone's approval, we need you to translate the text into your native language(s).
1. Once we are all happy that the survey is ready, you will disseminate the survey in your own country

Where to put translated text:

1. Translated questions should be added to the "questions_<country>_<year>.csv" under one or more of the columns "Trans lang 1", "Trans lang 2", "Trans lang 3" (contact us if you have more than three national languages).
1. Translated welcome and end text should replace the English-language version in the appropriate files in the Text directory.
1. Tranlsated lists of answers should replace the English-language versions in the csv files held in the listAnswers directory

Creating new questions:

1. 


## Explanation of the columns in ['summary_questions.csv']('summary_questions.csv')

* **Section**: The sections are the actual separation of the survey in different thematic sections. Some overlap may exists when some questions are used as distractors or in case of sensitive questions needed to be asked at the end of the survey

* **Type**: The type is a code to identify to which concept the question is associated too. When several questions are about the same aspect, they are numbered.

* **Question**: The question as presented to the participant

* **Format**: The type of format of the answer:
    * `Y/N/NA`: Yes or No format (with optional N/A when applicable)
    * `FREETEXT`: A field where participant can encode any text
    * `FREENUMERIC`: A field where participat can encode any number
    * `Dropdown list`: A list of choice. All the lists are stored in the ['listAnswers'](./listAnswers') folder
    * `Likert scale`: A likert scale is used. The type of likert scale is mentioned.

* **Mandatory**: If a answer need to be given by the participants before going further in the survey

* **Conditional**: If the question appears only under a specific question, the condition is explicitly stated in that field

* **Diff from original**: If the question as been `modified`/`added`/`removed` or remain the `same` comparatively to the first iteration of the survey

    There is three types of modifications that is possible to do:
    * **Adding/removing questions** to take into account the specificity of the country or situation that were not taken into account. In that case, it could be situations that are not encounter else where or that a similar situation is shared among countries. In that case the questions and the answers have to be made from scratch. This can be also applied for omission in the UK survey. Therefore it is a possibility to enhance the original survey

    * **Adapting the answers to the country** - Some answers are not valid in other countries. The most obvious example is the list of university. In that case a new set of answers has to be created that is independent to the others versions
    * **Creating correspondances between countries** - This last type of modification is the most difficult but essential. It is to create correspondence between countries. The straight forward example is with salary. We need to create scales of salary. We have to build different salary scales that can be easily compared in the future.

For every questions that imply a fixed list of answers, a specific csv file can be found in the ['listAnswers']('./listAnswers/'). Any adapted and newly created list of answers need to follow the same format to make the adaptation and reuse easier.

* **Source of information**: When applicable, the source of the information itself

* **Change for each country?**: If the answer to the question need to be adapted to the country

* **Comment**: Various comment about the question


## Technical solution

We decided to use the open source [limesurvey](http://www.limesurvey.org) service to create the survey. This solution present advantage in term of price and variety of hosting solutions. Also it is easier to share survey template that can be later modified by each organisation/countries. The template is in [template/](./templates').

To distribute the survey, a docker container is going to be provided with the associated templates.

The collaboration will be done on this repository to ensure access to the information for every one and respect the principle of transparency. However, on early stage, the repository is going to be set up on *private mode* until everyone agrees on going on *public*.


## Question mandatory

The first iteration of the survey did not set up the question as *mandatory*. During the analysis we realised that was a mistake. It is impossible to distinguish the NA to other type of answer. It is then strongly recommended to set up all question to mandatory, execpt for sensible question such as gender - salary.


# Details on questions

This section lists different identified issues or concerns about specifics sections in the survey.

## Reasons to leave previous position

With that section we intended to know why the respondents would have leave their previous work in private sector. We build the items based on several lists of the most shared reasons to leave the jobs


## Work indicators

In the RSE survey we used

Note that in the template the questions are in order to make it easier to work with them. However they need to be randomised.


## RSE definition issue

This section is essential to tailor the answer to the population of interest only. However, the definition of RSE is difficult because it is a relatively new role and there is no consensus on it yet.

For the previous study, we named the population **Research Software Engineer (RSEs)** because it is the term adopted in UK. We know that this term is not possible in Canada. Therefore this needs to be adopted to the most common used term in the respective country/organisation.

The questions we used to define RSE come from the [UKRSE website](http://www.rse.ac.uk/who.html). However, we removed items they were obviously biased toward a negative definition of the role as well as the one created on the assumption that RSE are post-doc. Despite the terminology a work on the definition should be done to include more possible variety of RSE around organisations.
There should also have a way to distinguishes RSE among themselves, which type of coding, work and assistance they provide. The first step toward such distinctions should be done by asking open questions on and analyse it later to see if tendencies are emerging.


## Contribution to papers

We added four questions to know in which extend the RSE are recognised for their paper contribution. This section should have more items about other types of contribution. It would be interesting to know in which extend their code is cited in the papers and how it is done.

## Good practices

We included two questions to know more about the good practice

## Academia and private sector

We are aware that some RSEs can work in private sector and still contribute to research. We are not studying that aspect in UK because our mission is about the RSEs working in academy. As consequence, the questions are not adapted for the private sector but a discussion on that aspect is needed.


## Gender

This question is quite difficult to create in order to capture the different genders that exists. However, the population will not be necessarily big and the study is not gender centred so we decided to only keep *woman* *man* *other* *prefer not to say*. The category *other* will capture all the potential diversity without creating too much different categories that would have to be grouped together for the analysis. However, it may still be a good option to include all categories or at least a blank field. In that case, adding the option *Trans* and *FREE TEXT*, should be enough. In the present template we left as we did for our own survey.

## Analysis

[LATER]



# REFERENCES

