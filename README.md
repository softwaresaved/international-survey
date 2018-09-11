# International collaboration for survey


[![DOI](https://zenodo.org/badge/63957124.svg)](https://zenodo.org/badge/latestdoi/63957124) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

***Collaboration tool to create surveys and analyse data about Research Software Engineers around the world***


In 2016 the Software Sustainability Institute ran the first survey of Research Software Engineers (RSEs) - the people who write code in academia. This produced the first insight into the demographics, job satisfaction, and practices of RSEs. To support and broaden this work, the Institute will run the UK survey every year and - it is hoped - will expand the survey so that insight and comparison can be made across different countries. Ultimately, we hope that these results, the anonymised version of which will all be open licensed, will act as a valuable resource to understand and improve the working conditions for RSEs.

In 2017 we also surveyed Canadian RSEs and we added four further countries, Germany, Netherlands, South Africa and USA. 
Our thanks to our partners: Scott Henwood (Canada), Stephan Janosch and Martin Hammitzsch (Germany), Ben van Werkhoven and Tom Bakker (Netherlands), Anelda van der Walt (South Africa) and Daniel Katz and Sandra Gesing (USA).

This repository is used to create and analyse international surveys. It use csv files to store questions and answers that are later transformed into a limesurvey TSV file. The analysis are using python and are shared within jupyter notebooks.


## Published results for the 2017 survey

We publish the results under the form of notebooks. All surveys have an attached 'public.csv' file. Theses files have been cleaned of all sensitive data. Therefore, the jupyter notebooks show some results that are not contained in the 'public.csv'.

|Country | Notebook | Dataset |
|  :-:       |  :-:   |  :-:  |
|Canada| 	[Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_can_2017_narrative.ipynb)| [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/can/data/public_data.csv)|
|Germany|  [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_de_2017_narrative.ipynb)| [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/de/data/public_data.csv)|
|Netherlands | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_nl_2017_narrative.ipynb)    | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/nl/data/public_data.csv)|
|South Africa | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_zaf_2017_narrative.ipynb)  	 | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/zaf/data/public_data.csv)|
|UK  | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_uk_2017_narrative.ipynb) | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/uk/data/public_data.csv)|
|USA | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_us_2017_narrative.ipynb)  | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/us/data/public_data.csv) |


## Contributing
If you wish to contribute and being involved in the survey creation please follow the [HOWTOCONTRIBUTE](https://github.com/softwaresaved/international-survey/blob/master/HOW%20TO%20CONTRIBUTE.md).
If you have discover an issue in the survey or wish to participate to the conversation we welcome any [issue submission](https://github.com/softwaresaved/international-survey/issues).


## Contributors
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

## Licence and citations

This repository contains code and public data. We have different licence for each
* The code is released under [BSD 3-Clause License](https://github.com/softwaresaved/international-survey/blob/master/LICENSE.md).
* The data stored in this repository is under the [CC BY 2.5 SCOTLAND](https://github.com/softwaresaved/international-survey/blob/master/LICENSE_FOR_DATA).

The repository is also archived on zenodo: https://doi.org/10.5281/zenodo.1194668.
If you want to cite this work and need a citation in a specific format, you can use the citation service on the zenodo.
The citation for the current archived version is:
> Olivier Philippe, Martin Hammitzsch, Stephan Janosch, Anelda van der Walt, Ben van Werkhoven, Simon Hettrick, … Scott Henwood. (2018, March 27). softwaresaved/international-survey: Public release for 2017 results (Version 2017-v1.1). Zenodo. http://doi.org/10.5281/zenodo.1406215


## Funders
The Software Sustainability Institute is supported by EPSRC grant EP/H043160/1 and EPSRC/ESRC/BBSRC grant EP/N006410/1, with additional project funding from Jisc and NERC. Collaboration between the universities of Edinburgh, Manchester, Oxford and Southampton.
