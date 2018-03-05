# International survey

Last year, the Software Sustainability Institute conducted a survey on Research Software Developers to understand who they are and their work conditions. This knowledge is essential to tailor any policy for this specific group, whose importance has increased in these past years but may still lack official recognition.
This year, several additional countries participated by adapting the survey to their own country:
* Germany: Stephan Janosch and Martin Hammitzsch.
* The Netherlands: Ben van Werkhoven and Tom Bakker.
* South Africa: Anelda van der Walt.
* United States of America: Daniel S. Katz and Sandra Gesing 

## Diffusion

We reached a total of 1377 participants and after selecting only the participants from the specific country being surveyed, we analysed 841 responses.

**Countries** |**Number of analysed responses**|**Link to analysis**|**Link to data**|
:-----:|:-----:|:-----:|:-----:|:-----:
**Germany**|325|[jupyter notebook](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_de_2017_narrative.ipynb)||
**Netherlands**|77|[jupyter notebook](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_nl_2017_narrative.ipynb)||
**United Kingdom**|164|[jupyter notebook](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_uk_2017_narrative.ipynb)||
**United States of America**|253|[jupyter notebook](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_us_2017_narrative.ipynb)||
**South Africa**|22|[jupyter notebook](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_zaf_2017_narrative.ipynba)||

## Composition of the survey

The surveys are composed of 10 sections that each investigated a specific aspect of the RSEs. These questions were mainly focused on the individual level.
The different sections may not appear in all surveys, as each country tailored each survey. For a report of which questions are present in which survey, please follow this [link](https://github.com/softwaresaved/international-survey/blob/master/survey_creation/2017/summary_questions.csv). Here is a brief description of each section and its associated goals:

1. **Demographics**: In this section, we were interested in the traditional social and economical aspect of the participants. Gender, age, salary and education are among the investigated dimensions and adapted to the specificities of each countries.
2. **Coding**: Obviously, RSEs are coding, but how often, for how long and for whom.
3. **Employment**: Which type of organisation they work for and in which disciplines.
4. **Current contract**: What type of contract and funding they have. This helps to assess the working stability of the participants.
5. **Previous employment**: Where they were previously working and the reasons they chose to be an RSE.
6. **Collaboration and training**: RSEs works for other researchers. We investigated this aspect here by asking questions not only about with whom they work and for which projects, but also if they train their fellow researchers.
7. **Publications**: Publications are an important aspect of academic work. However, as RSEs have hybrid roles, it may not be easy for them to benefit from this form of recognition. Additionally, some specific rules apply to the publication and dissemination of software. This section tries to understand these practices.
8. **Sustainability**: Some practices should be put in place to ensure quality of code but also the sustainability of the developed software.
9. **Job Satisfaction**: The aim of this section is to ask the participants about their job satisfaction to identify potential structural issues that are translated into individual perspectives.
10. **RSE Network**: Developing a network for RSEs is a long task and countries have different maturity levels on this regard. It is therefore essential to see how these efforts are accepted within the RSE population and measure awareness of such organisations.

## Quick insight of some results\*

Results differ from one country to another but some tendencies are shared among different places and could be seen as common for RSEs around the world. Firstly, we can say RSEs are mainly male and are from 25 to 44 years old. The majority of them hold a doctorate.

<sub>\*Disclaimer: This is only an overview of the results. To find out the exact numbers for each country, go directly to the different notebooks as linked in the [last section](#links). </sub>


We asked the participants which qualification they obtained, which is reported below.

**Countries**|**Gender**|**Age**|**Qualification**
:-----:|:-----:|:-----:|:-----:
**Germany**|Male (83%)|25 – 44 (84%)|Doctorate (48%)
**Netherlands**|Male (63%)|25 – 44 (84%)|Doctorate (56%)
**United Kingdom**|Male (84%)|25 – 44 (75%)|Doctorate (67%)
**United States of America**|Male (82%)|25 – 44 (69%)|Doctorate (60%)
**South Africa**|Male (92%)|25 – 44 (76%)|Doctorate (68%)

When we asked them in which field they obtained they qualification, there are three 3 disciplines that are clearly most common: *Computer sciences*, *Physics and Astronomy* and *Biology*.


|Country| First discipline| Second discipline | Third discipline |
|:-----:|:-----:|:-----:|:-----:|
|**Germany**|Physics and astronomy (26%)|Computer sciences (17%)|Biology (11%)|
|**Netherlands**|Computer sciences (20%)|Physics and astronomy (18%)|Biology (12%)|
|**United Kingdom**|Computer sciences (27%)|Physics and astronomy (27%)|Biology (8%)|
|**United States of America**|Computer sciences (25%)|Physics and astronomy (15%)|Biology (15%)|
|**South Africa**|Physics and astronomy (55%)|Other (9%)|Electrical & Electronic Engineering (5%)|



RSEs come from the same disciplines and it looks like they also work in the same ones. When we asked them for which disciplines they work, similar results came up, *Computer sciences*, *Biology* and *Physics and Astronomy* are over represented.


|Country| First discipline | Second discipline | Third discipline |
|:-----:|:-----:|:-----:|:-----:|
|**Germany**|Computer science (18%)|Physics and astronomy (14%) |Biology (14%)|
|**Netherlands**|Computer science (20%)|Biology (10%)|Physics and astronomy (10%)
|**United Kingdom**|Computer science (15%)|Biology (11%)|Physics and astronomy (10%)|
|**United States of America**|Computer science (21%)|Biology (12%)|Physics and astronomy (9%)|
|**South Africa**|Physics and astronomy (29%)|CS (12%)|Mathematics (10%)|


However, if we take a closer look at the results, it is possible to see a more interdisciplanry perspective in their work. In the following [notebook](https://github.com/softwaresaved/survey_additional_analysis/blob/master/interdisciplinary_aspects_of_research_software_engineers_in_uk.ipynb) data about United Kingdom is analysed. It appears that up to 63% of UK participants are working in more than one discipline.


Another specific aspect of the RSEs is what drives them to choose this work. We have seen that the majority hold a Doctorate, meaning a real interest and knowledge of a science field. This interest is clearly translated into the reasons for choosing this job. We asked them to rank the following propositions for the reasons they chose their position:

* Desire to work in a research environment
* Freedom to choose own working practices
* Desire to advance research
* I want to learn new skills
* Opportunity to develop software
* Flexible working hours
* Ability to work across disciplines
* Opportunity for career advancement
* The salary


|Country| First reason | Second reason | Third reason |
|:-----:|:-----:|:-----:|:-----:|
|**Germany**|Desire to work in a research environment|Freedom to choose own working practices|Desire to advance research|
|**Netherlands**|N/A|N/A|N/A|
|**United Kingdom**|Desire to work in a research environment|Desire to advance research|Opportunity to develop software|
|**United States of America**|Desire to advance research|Desire to work in a research environment|Freedom to choose own working practices|
|**South Africa**|Desire to work in a research environment|Flexible working hours|Ability to work accross disciplines|

We can see that is the research environment that mainly attracts RSEs and they are dedicated people that, as results also report, love their work and are really satisfied with it.
However, even if it seems that they are enjoying their job, they do not see much possibility of progression or promotion with their current job. This problem was previously highlighted in 2016 in the United Kingdom, and the situation did not change in 2017.

We also investigated their publications, both in traditional academic fashion and more on software practices. RSEs show a major contribution to paper publication through software development, but they are not always cited in the paper.

**Country**|**Software used for publication**|**Cited in the paper**
:-----:|:-----:|:-----:
**Germany**|83%|71%
**Netherlands**|95%|77%
**United Kingdom**|91%|78%
**United States of America**|90%|71%
**South Africa**|74%|42%


This year we asked them about the use of Open Source licence and if they use a Digital Object Identifier (DOI). On the one hand, an open source licence is extensively used, and on the other hand, DOIs for software have a lower penetration rate.

**Country**|**Use of open source licence**|**Frequency of open source use**|**Use of DOI**|**Percent of time for doi**
:-----:|:-----:|:-----:|:-----:|:-----:
**Germany**|62%|42% all the time|18%|variable
**Netherlands**|85%|44% all the time|31%|variable
**United Kingdom**|68%|48% all the time|22%|Sometime (30%)
**United States of America**|81%|40% all the time|32%|Sometime (26%)
**South Africa**|44%|variable|11%|Not often

Sustainability is an important aspect we advocate here at the Software Sustainability Institute. So it is normal for us to try to study this. To find out if RSEs are developing appropriate practices to ensure their software will outlive them, we asked if they are developing appropriate testing as well as the bus factor of their biggest project and the presence or not of a technical plan.


**Country**|**Testing**|**Bus factor**|**Technical handover**
:-----:|:-----:|:-----:|:-----:
**Germany**|15% not implementing anything|1 (57%)|Yes (19%)
**Netherlands**|13% not implementing anything|1 (45%)|Yes (21%)
**United Kingdom**|10% No testing|1 (42%)|Yes (26%)
**United States of America**|7% No testing|1 (39%)|Yes (18%)
**South Africa**|24% no testing|1 (78%)|Yes (11%)


The percentage of RSEs not implementing any form of testing could be seen as rather low. However, understanding the importance of their work in producing and publishing results, 10% should be seen as high. A similar problem is found with the bus factor. Often, only one person is responsible for developing the software. This could be explained by the low number of software developers dedicated to a project, though the low number of technical handover plans creates a problematic situation (even more when we perform an analysis of the result about future promotion).

Lastly, a short overview of the three top languages per countries is presented here. As we can see, there are some differences but Python is clearly the dominant language among RSEs.


|Country| First language| Second language| Third language |
|:-----:|:-----:|:-----:|:-----:|
|**Germany**|Python (18%)|C++ (10%)|Javascript (9%)|
|**Netherlands**|N/A|N/A|N/A|
|**United Kingdom**|Python (15%)|Unix Shell Script (11%)|Markup language (9%)|
|**United States of America**|Python (18%)|C (11%)|C++ (10%)|
|**South Africa**|Python (22%)|SQL (10%)|R (10%)|


## Links to the results<a name="links"></a>

This quick overview only scratches the surface of the data collected. To get complete access to the available information, you can peruse the [Github repository](https://github.com/softwaresaved/international-survey).

This is another repository that contains extra analysis and will contain more in the near future: [extra analysis](https://github.com/softwaresaved/survey_additional_analysis)

We are currently working on creating the survey for 2018 and hope to run it in July. To participate, read all information available at [here](https://github.com/softwaresaved/international-survey/blob/master/HOW%20TO%20CONTRIBUTE.md)
