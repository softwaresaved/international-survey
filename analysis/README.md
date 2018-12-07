# README

This folder contains all the necessary files to analyse the data collected in the survey.
It comprises of python scripts to generate a clean dataset (and merging years togethers), as well as Jupyter notebooks to analyse and sharing the results.

# Folder structure

* [./include](./include): Contains several python scripts used during the analysis (regardless of the year)
* [./2016/](./2016/): Folder containing the analysis for the 2016 survey. It contains the data from United Kingdom and Canada
* [./2017/](./2017/): Folder containing the analysis for the 2017 survey. It has separated folders for each countries that participate to the creation of the survey as well as two jupyter notebooks. One, being created automatically by the script [generate_2017_results.py](./generate_2017_results.py), and a second files that contains descriptions of the results.
* [./2018/](./2018/): folder containing the analysis for the 2018 survey
    * [./data](./2018/data)
    * Jupyter notebooks:
        * [0. Imports and functions.ipynb](./2018/0. Imports and functions.ipynb): Notebook containing all the imports and specific functions written for the 2018 analysis
        * [1. Overview and sampling.ipynb](./2018/1. Overview and sampling.ipynb): Loading the dataset and applying rule of subsetting, as well as displaying some informations about the location of the participants
        * [a. Education and previous formation.ipynb](./2018/a. Education and previous formation.ipynb): All analysis about the education of the participants
        * [b. Current employment.ipynb](./2018/b. Current employment.ipynb): All analysis about the current job of the participants, such as contract, salary, ...
        * [c. Professional developer.ipynb](./2018/c. Professional developer.ipynb): Analysis about the self-reported level of profesionalisation and the experience as developer
        * [d. How time is spent.ipynb](./2018/d. How time is spent.ipynb): Likert scales on how the participants spend their time at work and how they would want to do
        * [e. Previous employement.ipynb](./2018/e. Previous employement.ipynb): information about the previous employment and the reasons that the participants chose their current job
        * [f. Collaboration and training.ipynb](./2018/f. Collaboration and training.ipynb): Different analysis on the collaboration with other developers and researchers and participation to training
        * [g. Publications and citations.ipynb](./2018/g. Publications and citations.ipynb): Questions regarding the citations of the RSE and their participation to conferences/workshops
        * [h. Good practices, open source and tools.ipynb](./2018/h. Good practices, open source and tools.ipynb): Analysi of their practice in developing code and maintaining it, as well as which tools or OS the participants use.
        * [i. Job satisfaction.ipynb](./2018/i. Job satisfaction.ipynb): Self-reporting job satisfaction, turnover intention, perceived employability,...
        * [j. Socio demography.ipynb](./2018/j. Socio demography.ipynb): Questions about gender, ethnicity, age
        * [k. Research Software Engineer.ipynb](./2018/k. Research Software Engineer.ipynb): Several questions specific to the Research Software Engineers organisation
        * [x. All data.ipynb](./2018/x. All data.ipynb): All the sections above in one single file. It is here temporarily and going to be deleted when the 2018-survey branch is pushed into master

* [cleaning.py](./cleaning.py): Script to run on the raw dataset to output a cleaned data set and an public one, in csv format. Only the main researcher can run that script as (s)he is the only one to have the raw data
* [generating_2017_results.py](./generating_2017_results.py): Script to generate the analysis notebooks for the 2017 survey. Kept for archive reason.
* [merging.years.py](./merging_years.py): Script to run after the 'cleaning.py'. It parse the 2017 cleaned and public data and merge them into the 2018 dataset (alongside doing some last minute cleaning).

