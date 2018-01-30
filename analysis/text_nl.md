# Load dataset
To find the total number of participants, we took all submissions and then removed those from people who were outside the country (see question 1) and those from people who had not completed the first ten questions (i.e. those people who did not complete the first page of the survey).


# Section 1. Social demographics
In this section, we determine some information about the demographics of the respondents: country of work, gender, salary, educational level, age.


## Country of work
The data was cleaned to remove all participants that were not working in the Netherlands


## Gender
Their is a clear gender imbalance in the RSE community in the Netherlands. It is predominately *male* (89%). Only 7% of the participants describe their gender as *female*, while 4% *prefer not to say*.


## Age
The majority of RSEs fall within two ranges of ages the *25 to 34 years* and the *35 to 44 years* (both 42%). The representation of older or younger range is almost inexistant. 

## Salary
We asked the participants to give us the range of salary they are paid. 17% of the participants prefered not to say. However, the most common salary in The Netherlands for the participants is between 44.000 and 49.999 euros (19%) with a concentration of the other salaries around this range. However, 4% earn less than 27.499 euros and 15% more than 55.000 euros.


## Qualifications
The highest proportion of RSEs holds a PhD (56%) add 39% a master degree. The remaining participants have a Bachelor. 

Most RSEs derive from a background in *Computer Science* (26%) or *Physics and Astronomy* (23%). The third most often field is *Biological Sciences* (12%). There is a significant reduction in numbers in the next most popular background *Chemistry* (9%).


# Section 2: Questions about coding
In this section we investigate the relationship between RSEs and the code they develop.

As expected, the vast majority of RSEs (97%) write code. They are, in vast majority, writing code for other people. Only 6% of them write code for themselves, and 84% for 2 or more people

However, despite the majority of them writing code, only 65% consider themselves as *professional software developer*. This is a low number when we consider the average time of developing software (12 years) and that they are mainly developing software for others.

Unsurprisingly, RSEs spend the majority of their time coding. They are almost exclusively doing that. 



# Section 3. Questions about employment

48% of RSEs work within a university and 38% for a Research Institute. They are only 8% to work for Private company or other type of organisation. When we ask them from which university they work, the Leiden University has the most answers (20%), followed by Radboudumc, Radboud Universitair Medisch Centrum (14%) and by Utrecht University (11%). 
The same question applied for organisation they work for has a majority of "Netherlands eScience Center" (52%) and a variety of marginal organisation (in terms of answers). 

About the job title, 26 participants mention that their official job title differs from the one they are actually using. Both lists, the official and the job title they use, are available below. 


At the question about the field where they work, the participants mainly answered *Computer Science* (20%), followed by *Biological Sciences* (10%)  and *Physics and Astronomy* (10%). This top three remain the same as for their education. However, the lower percent for each of them is explained by a much larger variety of disciplines where they currently work, underlying the interdisciplinary aspect of RSEs. 



# Section 4. Questions about the type of contract

Type of contracts and funding are important to understand the situation of RSEs and if they have stable position in academia.
A vast majority of participants have a full time job (74%) and half of them have a permanent position. The average length of contract duration is more or less 2 years for the participants that does not have a permanent position.

# Section 5. Collaboration and training
RSEs do not work for themselves, their role involves writing code that is used by others (as seen in section 2), but the collaboration can take other forms. 
On average they work on 4 different projects at the same time.

RSEs have programming skills that is not necessarily shared within their field. Therefore, they can train other researchers to develop some best practices or learn how to program more efficiently. 59% of them participate to such training. They are not teaching directly to students (as seen in section 2) but transferring skills is an important aspect of their job. In average, they do training twice a year. These trainings are more often done under the form of workshop than traditional teaching. A type of training probably more adapted to teach computing skills.


# Section 6. Publications

RSEs is an hybrid role between a researcher and a software developer. We investigated both of these aspects concerning publication and dissemination of their work, one on the traditional aspect of it (publications and conference) and on the more software aspect (open source and DOI).
One essential aspect of career in academia is the publications and the conferences to gain recognition. However, the role of RSE being less about writing articles than creating the infrastructure and the software for the article to exist, there is some fear that they will fail to have recognition through the papers and conferences.
Our results support this idea, while for 95% of the participants, their software is used in published researches they are only 77% (among them) who are acknowledged in the publication.

Among these participants that are acknowledged in the paper, only 33% are generally named as main author for the paper. Among the 67% of those who are not main author, 78% are at least mentioned as co-authors. And among these last 22% of RSEs that are not mentioned as co-author or main author, 90% are at least generally acknowledged in the main text of the paper.
On conference, the number of RSEs that present their work in conference is also high. 79% of these RSEs have presented in conference or workshop. 

One important development practice is how the code is distributed and if the RSEs are releasing their work under open licence.
We asked the participants if they have ever released their work under open source licence and 85% of them replied by the affirmative. It is seems that they mainly doing it all the time (44%), followed by the score 9 on the 10 item scale (16%). Therefore, as soon as the step to open source is done, it seems that RSEs seems a constant interest in it. However, they rarely use a Digital Object Identifier (DOI) to help to identify their software, only 31% of them are doing it. And the frequency of use of the DOI among them is much more variable than for the open licence.


# Section 7. Sustainability and technical details

This section comprises two subsections that focus on the technical and development aspects of the RSEs' work. They aim to understand good practices in developing software and which tools are important for RSEs.

Developing software requires a set of good practices to ensure the quality of the subsequent analysis as well as the robustness of the developed software, to name a few of important aspects. We wanted to see if the implementation of some simple but essential good practices were a reality. Three measures were created, the implementation of testing, the bus factor and the technical hand over plan.
These metrics allows to see the importance of the RSEs role in their team but also if they are themselves implementing some practices that are used widely in industry but less in academic research.

We asked the participants to choose any of the following testing methods:
* Test engineers conduct testing
* Developers conduct testing
* Users conduct testing
* No formal testing

Obviously, the *test engineers conduct testing* is the most potential testing method but may not be possible in number of small projects while, no formal testing should not occur in any ideal scenario, regardless of the size of the project. Surprisingly, 13% of the participants confessed they were not implementing any testing at all. It may seems a low number but we think it is still a high percentage considering the specific work of this population. When they are conducting testing, the RSEs seems to prefer (or only able to implement) *developer testing* (49% of them) or letting the users conduct the testing (32%), while the use of test engineers is marginal (6%).

We chose two broad measures to provide an insight into sustainability: the bus factor and technical hand over planning. The bus factor is a measure of the number of developers who understand a specific software project and could, with only a cursory review of the project, maintain or extend the code. A project with a bus factor of 1 is completely reliant on only one developer. If this developer finds new employment, becomes ill or is hit by the titular bus, then the project will fail. A high bus factor provides some confidence that the project can be sustained even if a developer leaves. A technical hand over plan is used to introduce a new developer to a software project. These plans cover basic information, such as the licence and location of the software, a repository, a description of the software architecture, a summary of development plans and any other information that a new developer would need to understand the software. A project that has written (and maintained) a technical hand over plan can withstand the departure of a developer, even a key developer, significantly better than one without such a plan.

On majority of the RSEs' projects the bus factor is 1 (45%), followed by a bus factor of 2 (27%). Higher bus factors are marginal with only 19% of the projects having a bus factor of 3, 3% of a bus factor of 4 and 7 % a bus factor equal or higher than 5. However, the presence of a technical plan, which can mitigate the low bus factor in the different projects is really low (21%) and presents a risk of project failures.


# Section 8. Job satisfaction

The job satisfaction is an essential pulse to take about the community. It helps to track the evolution and the current state of the RSEs within their role and to catch any sign of structural or organisational dysfunction that are translated into well-being. There are a lot of different metrics to measure the quality of a job on a personal and psychological level [4]. Several models exist to understand the link between different factors of job satisfaction and turnover intention [5]–[9]. Turnover intention is an important measure that is highly associated with the risk of employees leaving the organisation [7]. Job satisfaction is important in retaining RSEs. Perceived employability provides information on how workers values their own skills in regard of the market. To measure the different attitudes toward the RSE role, we used scales that have been created in [5], [6], [8], [9]. These are Likert scale [10], which are 5 point ordinal scales graduated from Strongly disagree to Strongly agree. Each scale is composed of several so called items (i.e. questions) that each measure one attitude.

Beside these specific concepts we asked more general question about their satisfaction in their current position and their satisfaction with their career in general with a range of answers from *0 - Not at all satisfied* to *10 - Completely satisfied*, 79% of the participants answered more than 5 to the scale (which can be considered as a neutral position) to the question about their satisfaction about their current position. For the question about their satisfaction with their career in general (and using the same scale), 71% of the participants answered more than 5 to the scale.

The specific questions about their job satisfaction reflect, in general, the same opinion as the two more generic questions. However, the granularity helps to identify a couple of issues that would not appears with generic questions:

* *The feedback about the performance*: These questions ask if the RSEs feel that they receive enough information about their work and their performance. While they seems to have enough information about the purpose of their work and having access to sufficient data and information, they are less assertive about the feedback they receive from their colleagues and their supervisors.

* *The turnover intention*: These questions aim to measure the desire to quit their current position. Overall, the participants are not willing to leave their position and are not necessarily searching for other job, even if the potential job would offer the same compensations.

* *The perceived employability*: This concept is linked to the previous one. People may not have the intention to leave their jobs, not because they like it, but because they fear they are not employable. This is not the case here, the participants consider themselves more often employable than not.

* *The affective recognition*: This concept try to see if the participants receive positive feedback from their supervisors. Overall, again the participants report a positive relation with their supervisors. It means they are not systematic issues with direct management.

* *Affective satisfaction*: Here, the concept measures how much the participants enjoy and like their job. The answers were positive and again, reflect the answers given at the more generic questions.

* *The possibility of progression*: This question aims to study the possibility of evolution for the RSEs, if information is available and if they see a possibility of evolution within their current career. This is the only questions that clearly received negative answers. To summarise, even if the RSEs have planned to be in this position, as a part of their career plan, the majority of them think they cannot be promoted in their current group, neither the information for such progression is easily accessible. Moreover, they do not think that in their career plan there is a lot of opportunities. 

# Section 9. Research Software Engineer

The last section was about the RSE network. It appears that the network is not really efficient yet. First, to the question where they meet other RSE. They mainly meet within local group/network (56%). Only a few do it through the NL-RSE Association (5%) or at the UK RSE Association/ Conference (4%). However, they are almost half of them (47%) member of the NL-RSE Association










