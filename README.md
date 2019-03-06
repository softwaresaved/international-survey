# International collaboration for survey

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1194668.svg)](https://doi.org/10.5281/zenodo.1194668) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)



***Collaboration tool to create surveys and analyse data about Research Software Engineers around the world***

This repository is used to create and analyse international surveys. It use csv files to store questions and answers that are later transformed into a limesurvey TSV file. The analysis are using python and are shared within jupyter notebooks.


In **2016** the Software Sustainability Institute ran the first survey of Research Software Engineers (RSEs) - the people who write code in academia. This produced the first insight into the demographics, job satisfaction, and practices of RSEs. To support and broaden this work, the Institute will run the UK survey every year and - it is hoped - will expand the survey so that insight and comparison can be made across different countries. Ultimately, we hope that these results, the anonymised version of which will all be open licensed, will act as a valuable resource to understand and improve the working conditions for RSEs.

In **2017** we also surveyed Canadian RSEs and we added four further countries, Germany, Netherlands, South Africa and USA. 
Our thanks to our partners: Scott Henwood (Canada), Stephan Janosch and Martin Hammitzsch (Germany), Ben van Werkhoven and Tom Bakker (Netherlands), Anelda van der Walt (South Africa) and Daniel Katz and Sandra Gesing (USA).

In **2018** we have worked differently and created a survey for all countries (rather than one survey for each ones). 



## Published results
We publish the results under the form of notebooks. All surveys have an attached 'public.csv' file. Theses files have been cleaned of all sensitive data. Therefore, the jupyter notebooks show some results that are not contained in the 'public.csv'.

<table>
    <thead>
      <tr>
            <th>Country</th>
            <th>2016</th>
            <th>2017</th>
            <th>2018</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Australia</td>
            <td>N/A</td>
            <td>N/A</td>
            <td rowspan=8><a href="https://github.com/softwaresaved/international-survey/tree/master/analysis/2018">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2018/data/public_data.csv">Public data</a></td>
        </tr>
        <tr>
            <td>Canada</td>
            <td>N/A</td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/results_can.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/can/data/public_data.csv">Public data</a></td>
        </tr>
        <tr>
            <td>Germany</td>
            <td>N/A</td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/results_de_narrative.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/de/data/public_data.csv">Public data</a></td>
        </tr>
        <tr>
            <td>Netherlands</td>
            <td>N/A</td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/results_nl_narrative.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/nl/data/public_data.csv">Public data</a></td>
        </tr>
        <tr>
            <td>New Zealand</td>
            <td>N/A</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>United Kingdom</td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2016/results_uk_narrative.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2016/uk/data/public_data.csv">Public data</a></td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/results_uk_narrative.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/uk/data/public_data.csv">Public data</a></td>
        </tr>
        <tr>
            <td>United States</td>
            <td>N/A</td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/results_us_narrative.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/us/data/public_data.csv">Public data</a></td>
        </tr>
        <tr>
            <td>South Africa</td>
            <td>N/A</td>
            <td><a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/results_zaf_narrative.ipynb">Analysis</a> / <a href="https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/zaf/data/public_data.csv">Public data</a></td>
        </tr>
    </tbody>
</table>

## Composition of the survey
The [base questions](https://github.com/softwaresaved/international-survey/blob/master/survey_creation/2018/questions.csv) for the survey were tailored to meet the requirements of each country. They covered ten subjects:
   1. **Demographics**: traditional social and economic questions, such as gender, age, salary and education.
   1. **Coding**: how much code do RSEs write, how often, and for whom.
   1. **Employment**: questions about where RSEs work and in which disciplines.
   1. **Current contract**: understanding stability of employment by questioning the type of employment contract RSEs receive.
   1. **Previous employment**: understanding routes into the profession the reasons for choosing it.
   1. **Collaboration and training**: who RSEs work with, how many people they work with, and the training they conduct.
   1. **Publications**: do RSEs contribute to publications and are they acknowledged?
   1. **Sustainability and tools**: testing, bus factor, technical handover. Also which tools they are using
   1. **Job satisfaction**: what do RSEs think about their job and their career?
   1. **Network**: how do RSEs meet and gain representation?
These subjects are not necessarily  investigated under this order, neither published with that order. 

## Contribution

### Contributing
If you wish to contribute and being involved in the survey creation please follow the [HOWTOCONTRIBUTE](https://github.com/softwaresaved/international-survey/blob/master/HOW%20TO%20CONTRIBUTE.md).
If you have discover an issue in the survey or wish to participate to the conversation we welcome any [issue submission](https://github.com/softwaresaved/international-survey/issues).

### Current contributors
Here is a list of contributors for the 2017/2018 version of the survey (alphabetic order). They are also mentioned in the [.zenodo.json](https://github.com/softwaresaved/international-survey/blob/master/.zenodo.json) to be automatically added to the DOI.
* Stephan Druskat
* Sandra Gesing
* Martin Hammitzsch
* Scott Henwood
* Simon Hettrick
* Stephan Janosch
* Katrin Leinweber
* Olivier Philippe
* Nooriyah P. Lohani
* Nicholas R. May
* Manodeep Sinha
* Daniel S. Katz
* Anelda van der Walt
* Ben van Werkhoven

## Licence 

This repository contains code and public data. We have different licence for each
* The code is released under [BSD 3-Clause License](https://github.com/softwaresaved/international-survey/blob/master/LICENSE.md).
* The data stored in this repository is under the [CC BY 2.5 SCOTLAND](https://github.com/softwaresaved/international-survey/blob/master/LICENSE_FOR_DATA).

The repository is also archived on zenodo: https://doi.org/10.5281/zenodo.1194668.
If you want to cite this work and need a citation in a specific format, you can use the citation service on the zenodo.

## Citations
The citation for the 2018 version is:
> Olivier Philippe, Martin Hammitzsch, Stephan Janosch, Anelda van der Walt, Ben van Werkhoven, Simon Hettrick, … Manodeep Sinha. (2019, March 6). softwaresaved/international-survey: Public release for 2018 results (Version 2018-v.1.0.2). Zenodo. http://doi.org/10.5281/zenodo.2585783

The citation for the 2017 version is:
> Olivier Philippe, Martin Hammitzsch, Stephan Janosch, Anelda van der Walt, Ben van Werkhoven, Simon Hettrick, … Scott Henwood. (2018, March 27). softwaresaved/international-survey: Public release for 2017 results (Version 2017-v1.2). Zenodo. http://doi.org/10.5281/zenodo.2574123

## Funders
The Software Sustainability Institute is supported by EPSRC grant EP/H043160/1 and EPSRC/ESRC/BBSRC grant EP/N006410/1, with additional project funding from Jisc and NERC. Collaboration between the universities of Edinburgh, Manchester, Oxford and Southampton.
