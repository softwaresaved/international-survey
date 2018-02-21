# International survey

Last year, the Software Sustainability Institute conducted a survey on Research Software Developers to understand who they are and their work conditions. This knowledge is essential to tailor any policy for this specific group, whose importance has increased in these past years but may still lack official recognition.
This year, several additional countries participated by adapting the survey to their own country:
* Germany: Stephan Janosch and Martin Hammitzsch.
* The Netherlands: Ben van Werkhoven and Tom Bakker.
* South Africa: Anelda van der Walt.
* The United States of America: Sandra Gesing and Daniel Katz

## Diffusion

We reached a total of 1377 participants and after selecting only the participants from specifics countries, we analysed 841 responses.
Here is a table with the number of participants per country.

**Countries** |**Total participants\***|**Partial participants\*\***|**Participants who finished the survey**|**Number of participants actually analysed**
:-----:|:-----:|:-----:|:-----:|:-----:
**Germany**|574|296|278|325
**Netherlands**|100|28|72|77
**United Kingdom**|232|88|144|164
**United States of America**|432|143|289|253
**South Africa**|39|22|17|22
**TOTAL**|1377|577|800|841

<sub> \* The *Total participants* are the number of people that opened the survey no matter how far they went through.</sub>

<sub> \*\* The *Partial participants* are the number of participants that did not finished the survey but may have only skipped the last question.</sub>

## Composition of the survey

The survey itself had ten major sections covering various aspects.
The different sections may not appear in all surveys as each country tailored each survey. For a report of which questions are present in which survey, please follow this [link](https://github.com/softwaresaved/international-survey/blob/master/survey_creation/2017/summary_questions.csv). Here is a brief description of each section and its associated goals:

1. **Demographics**: In this section, we were interested in the traditional social and economical aspect of the participants. Gender, age, salary and education are among the investigated dimensions and adapted to the specificities of each countries.
2. **Coding**: Obviously, RSEs are coding, but how often, for how long and for whom.
3. **Employment**: Which type of organisation they work for and in which disciplines.
4. **Current contract**: What type of contract and funding they have. This helps to assess the working stability of the participants.
5. **Previous employment**: Where they were previously working and the reasons they chose to be an RSE.
6. **Collaboration and training**: RSEs works for other researchers. We investigated this aspect here by asking questions not only about with whom they work and for which projects, but also if they train their fellow researchers.
7. **Publications**: Publications are an important aspect of academic work. However, as RSEs have hybrid roles, it may not be easy for them to benefit from this form of recognition. Additionally, some specific rules apply to the publication and dissemination of software. This section tries to understand these practices.
8. **Sustainability**: Some practices should be put in place to ensure quality of code but also the sustainability of the developed softwares.
9. **Job Satisfaction**: The aim of this section is to ask the participants about their job satisfaction to identify potential structural issues that are translated into individual perspectives.
10. **RSE Network**: Developing a network for RSEs is a long task and countries have different maturity levels on this regard. It is therefore essential to see how these efforts are accepted within the RSE population and measure awareness of such organisations.

## Quick insight of some results\*

Results differ from one country to another but exists some tendencies are shared among different places become clear and could be seen as common faith for RSEs around the world. Firstly, we can say RSEs are mainly male and are from 25 to 44 years old. They also hold, for the majority of them, a doctorate.

<sub>\*Disclaimer: These results only give an overview of some results. To find out the exact number for each country with more precision, go directly to the different notebook as linked in the [last section](#links). </sub>



**Countries**|**Gender**|**Age**|**Qualification**
:-----:|:-----:|:-----:|:-----:
**Germany**|Male (83%)|25 – 44 (84%)|Doctorate (48%)
**Netherlands**|Male (63%)|25 – 44 (84%)|Doctorate (56%)
**United Kingdom**|Male (84%)|25 – 44 (75%)|Doctorate (67%)
**United States of America**|Male (82%)|25 – 44 (69%)|Doctorate (60%)
**South Africa**|Male (92%)|25 – 44 (76%)|Doctorate (68%)

Secondly, where they get their diploma. It is clear that 3 disciplines are constantly represented, *Computer sciences*, *Physics and Astronomy* and *Biology*.


|||
:-----:|:-----:|:-----:|:-----:
**Germany**|Physics and astronomy (26%)|Computer sciences (17%)|Biology (11%)
**Netherlands**|Computer sciences (20%)|Physics and astronomy (18%)|Biology (12%)
**United Kingdom**|Computer sciences (27%)|Physics and astronomy (27%)|Biology (8%)
**United States of America**|Computer sciences (25%)|Physics and astronomy (15%)|Biology (15%)
**South Africa**|Physics and astronomy (55%)|Other (9%)|Electrical & Electronic Engineering (5%)



RSEs are coming from the same disciplines and it looks like they also work in the same ones. When we asked them for which disciplines they work, similar results come up, *Computer sciences*, *Biology* and *Physics and Astronomy* are over represented.


|||
:-----:|:-----:|:-----:|:-----:
**Germany**|Computer science (18%)|Physics and astronomy (14%) |Biology (14%)
**Netherlands**|Computer science (20%)|Biology (10%)|Physics and astronomy (10%)
**United Kingdom**|Computer science (15%)|Biology (11%)|Physics and astronomy (10%)
**United States of America**|Computer science (21%)|Biology (12%)|Physics and astronomy (9%)
**South Africa**|Physics and astronomy (29%)|CS (12%)|Mathematics (10%)


However, if we take a closer look at the results, it is possible to see a more interdisciplanry perspective in their work. In the following [notebook](https://github.com/softwaresaved/survey_additional_analysis/blob/master/interdisciplinary_aspects_of_research_software_engineers_in_uk.ipynb) data about United Kingdom is analysed. It appears that up to 63% of UK participants are working in more than one discipline.


Among other results that are shared accross countries, we can talk about the reasons why RSEs chose their job. It is clear that interest in research is the main motivation to become an RSE—it is a position they wanted to have and are happy with. However, even if it seems that they are enjoying their job, they do not see much possibility of progression or promotion with their current job. This is a problem already highlighted in 2016 in United Kingdom and the situation did not change in 2017.

We also investigated their publications, both in traditional academic fashion and more on software practices. They are still showing a major contribution to paper publication through software development but they are not always cited in the paper.

**Country**|**Software used for publication**|**Cited in the paper**
:-----:|:-----:|:-----:
**Germany**|83%|71%
**Netherlands**|95%|77%
**United Kingdom**|91%|78%
**United States of America**|90%|71%
**South Africa**|74%|42%


This year we asked them about the use of Open Source licence and if they use a Digital Object Identifier (DOI). On the one hand, the former is most extensively used, and among the users, they are often used. On the other hand, the use of DOI has a lower penetration rate and even among those who use it, they do not tend to frequently associate a DOI. Therefore, Open source seems more spread and as soon it is used, it becomes natural to associate an open source licence to the software, while the DOI does not share the same enthusiasm.

**Country**|**Use of open source licence**|**Frequency of open source use**|**Use of DOI**|**Percent of time for doi**
:-----:|:-----:|:-----:|:-----:|:-----:
**Germany**|62%|42% all the time|18%|variable
**Netherlands**|85%|44% all the time|31%|variable
**United Kingdom**|68%|48% all the time|22%|Sometime (30%)
**United States of America**|81%|40% all the time|32%|Sometime (26%)
**South Africa**|44%|variable|11%|Not often

Sustainability is an important aspect we advocate here at the Software Sustainability Institute. So it is normal we try to study this aspect too. To find out if RSEs are developing appropriate practices to ensure their software will outlive them, we asked if they are developing appropriate testing as well as the bus factor of their biggest project and the presence or not of a technical plan.


**Country**|**Testing**|**Bus factor**|**Technical handover**
:-----:|:-----:|:-----:|:-----:
**Germany**|15% not implementing anything|1 (57%)|Yes (19%)
**Netherlands**|13% not implementing anything|1 (45%)|Yes (21%)
**United Kingdom**|10% No testing|1 (42%)|Yes (26%)
**United States of America**|7% No testing|1 (39%)|Yes (18%)
**South Africa**|24% no testing|1 (78%)|Yes (11%)


The percentage of RSEs not implementing any form of testing could be seen as rather low. However, understanding the importance of their work in producing and publishing results, 10% should be seen as high. A similar problem is found with the bus factor. Often, only one person is responsible for the software writing. This could be explained by the low number of software developers dedicated to a project, though the low number of technical plan creates a problematic situation (even more when we perform an analysis of the result about future promotion).


**Country**|**Testing**|**Bus factor**|**Technical handover**
:-----:|:-----:|:-----:|:-----:
**Germany**|15% not implementing anything|1 (57%)|Yes (19%)
**Netherlands**|13% not implementing anything|1 (45%)|Yes (21%)
**United Kingdom**|10% No testing|1 (42%)|Yes (26%)
**United States of America**|7% No testing|1 (39%)|Yes (18%)
**South Africa**|24% no testing|1 (78%)|Yes (11%)


Lastly, a short overview of the three top languages per countries is presented here. As we can see, there are some differences but Python is clearly the dominant language among RSEs.


||||
:-----:|:-----:|:-----:|:-----:|:-----:
**Germany**| |Python (18%)|C++ (10%)|Javascript (9%)
**Netherlands**| |N/A|N/A|N/A
**United Kingdom**| |Python (15%)|Unix Shell Script (11%)|Markup language (9%)
**United States of America**| |Python (18%)|C (11%)|C++ (10%)
**South Africa**| |Python (22%)|SQL (10%)|R (10%)


## Links to the results<a name="links"></a>

This quick overview only scratches the surface of the data collected. To get complete access to the available information, you can peruse the [Github repository](https://github.com/softwaresaved/international-survey).
Direct access to any of the specific surveys is also available:

* [Germany](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_de_2017_narrative.ipynb)
* [Netherlands](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_nl_2017_narrative.ipynb)
* [United Kingdom](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_uk_2017_narrative.ipynb)
* [United States of America](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_us_2017_narrative.ipynb)
* [South Africa](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_zaf_2017_narrative.ipynba)

This is another repository that contains extra analysis and will contain more in the near future: [extra analysis](https://github.com/softwaresaved/survey_additional_analysis)

We are currently working on creating the survey for 2018 and hope to run it in July. To participate, read all information available at [here]()
