# Importing modules

# Loading dataset
To find the total number of participants, we took all submissions and then removed those from people who were outside the country (see question 1) and those from people who had not completed the first ten questions (i.e. those people who did not complete the first page of the survey).


# Section 1. Social demographics
In this section, we determine some information about the demographics of the respondents: country of work, gender, age, salary, educational level.


## Country of work
The data was cleaned to remove all participants that were not working in United States of America

### In which country do you work?

## Gender
Their is a clear gender imbalance in the RSE community in Germany. It is predominately *male* (82%). Only 14% of the participants describe their gender as *female*, while 4% *prefer not to say*.

### Please select your gender

## Age
The majority of RSEs fall within the *25 to 34 years* (53%), and the next more important age range is *35 to 44 years* (31%). The representation of older or younger range is marginal compared to these two groups (16% in total, split in three age ranges).

### Please select your age

## Ethnic origin
The RSEs are in majority *White* (77%) compared to the other ethnic origins. The second largest group is the *Asian* (11%), followed by *Hispanic, Latino, or Spanish origin* (6%)


### How would you describe your ethnic origin? This refers to people who share the same cultural background and identity, not country of birth or nationality.

## Salary
We asked the participants to give us the range of salary they are paid. The most common salary in USA for the participants is *from $70,000 to $89,999* (28%) and *from $90,000 to $109,999* (29%). On the extremes, 4 RSEs earn less than $30,000 while 10 earn more than $150,000

### Please select the range of your salary

## Disability
To ensure equality, it is important to gather information about disability. In this regard, 3% of the participants declare having a condition as defined by the Americans with Disabilities Act (ADA)

### Do you have a condition that is defined as a disability by the Americans with Disabilities Act (ADA)?

## Qualifications
A majority of RSEs hold a *doctorate* (60%) followed by *master degree* (25%) and *undergraduate degree* (12%). The rest of the degree are marginal. This show a necessity for RSEs to be embedded in a research process before becoming software developer in research. 

For the type of background, some cleansing were done to transform specific fields into more generic ones as used [here](https://www.thecompleteuniversityguide.co.uk/courses). Most RSEs come from a background in *Computer Science* (25%) followed by *Biological Sciences* and *Physics and Astronomy* (both represent 15%).
There is a significant reduction in proportion for the next backgrounds but overall the origin is quite diverse with a total of 23 different fields (including the field *Other*).

When we asked the RSEs if they hold any professional qualifications, 23 of them answered to it but when we take a closer looks to the results, it appears that only a small number get some certificates in machine learning, bioinformatic or in GIS. 

### What is the highest degree/qualification you have obtained?
### In which subject is your highest academic degree/qualification?
## Professional qualifications
### Do you hold any other professional degrees/qualifications? (Please enter each of them separated by a semicolon)


# Section 2: Questions about coding

In this section we investigate the relationship between RSEs and the code they develop.

As expected, the vast majority of RSEs (96%) write code. They are, in vast majority, writing code for other people. Only 7% of them write code for themselves. A high proportion even writes code for 5 or more people (26%).

However, despite the majority of them writing code, only 61% consider themselves as professional software developer. This is a low number when we consider the average time of developing software (14 years) and that they are mainly developing software for others.

Unsurprisingly, RSEs spend the majority of their time coding. The second activity that seems to take their time is "research". So it would appear that their job title accurately describes their work. "Teaching" is the aspect of work with the least call on RSEs time: 45% of RSEs reported that they spent no time in teaching at all.



### Do you write code as part of your job?
### Who uses the code that you write?
### Do you consider yourself a professional software developer?
### How many years of Software development experience do you have?
### In an average month, how much time do you spend on software development (Please rate your answer between 1 to 10. 1 Being none at all and 10 being All your time.); In an average month, how much time do you spend on Research; In an average month, how much time do you spend on Management; In an average month, how much time do you spend on Teaching; In an average month, how much time do you spend on Other activities


# Section 3. Questions about employment

75% of RSEs work within a university and 11% in National laboratory and it seems that University of Illinois and Princeton University have the highest concentration of the participants (7% each) but overall the participants seems widely spread in a number of different Universities. 

A list of different organisations, when RSEs were not working for any university is also given below, as well as a job title. About the job title, 44 participants mention that their official job title differs from the one they are actually using.

At the question about the field where they work, the participants mainly answered *Computer Science*, followed by *Physics and Astronomy* and *Biological Sciences* (both 14%). These is the three main disciplines found in the question about education.



### What type of organization do you work for?
### Which University?
### Which organization do you work for?
### What is your official job title?
### Are you known by a different job title? If so, please enter the job title you use
### In which disciplines do you work (select as many as apply)


# Section 4. Questions about the type of contract

Type of contracts and funding are important to understand the situation of RSEs and if they have stable position in academia.
A vast majority of participants have a full time job (96%) and with a permanent position (42% as long as the funding are available and 40% with core funding). The average length of contract duration is more or less 6 years for the participants that does not have a permanent position.

For the source of funding, 90% of the participants know the origin of them. The majority of the project for which the participants work are funded through Grants (51%), followed by funding from institutions (29%). The rest of funding are marginal.
The second question about the funding was about the previous project. This helps to see if the source of funding changes over time for the participants. The answer is no, the sources of funding were exactly the same with only a slight variation in percentages, the grants account for 50% while the funding from institutions accounts for 29%. 

A question also asked about the funding about their effort as an RSE/equivalent. Here again the two tops sources of funding remains the same, 44% for Grants and 33% for institution. However, for their effort as RSE, 10% of the participants declared to volunteer their time.
It is important to note that these percentages are not mutually exclusives as the participants had the option to choose several sources of funding for each question.


### Do you work full time or part time
### What type of employment do you have?
### What is the total duration of your current employment (in years)?
### Do you know the source of the funding used to support you and your current, largest project?
### Which of the following sources are used to pay for your effort as an RSE/equivalent?
### Which of the following sources are used to fund your current, largest project?
### Which of the following sources were used to fund your current, largest project three years ago?


# Section 5. Questions about previous employment

Several questions were about the participants previous job. The idea is to collect insights of their career and understand what are their motivations to be an RSE.

Almost half of the participants worked in a university prior to their current position (48%) but an interesting big number comes from Private companies (23%) showing a different path of career. For the last significative portion of RSEs, it is their first job (17%).

We asked the participants to rank the reasons why they chose their actual position among 8 different ones:
* Desire to work in a research environment
* Freedom to choose own working practices
* Desire to advance research
* I want to learn new skills
* Opportunity to develop software
* Flexible working hours
* Ability to work across disciplines
* Opportunity for career advancement
* The salary

It appears that the desire to advance research, the desire to work in a research environment and the Freedom to choose own working practices and the  are more often ranked as the first reasons than any others one. On the contraries, the Opportunity for career advancement and the salary are the least common reasons for choosing a position as RSE.

### Where was your previous job based?
### Rank the following factors dependent on how strongly they influenced your decision to accept your current position


# Section 6. Collaboration and training

RSEs do not work for themselves, their role involves writing code that is used by others (as seen in section 2). This is why we asked if they are embedded in a stable structure and whom the participants work with. 43% of them are within a Research Software Group which leave the majority of them without appropriate institutional support.

On the side of collaboration, we wanted to know if they were working within a stable group of researcher software. Usually, they seems to work with different researchers 57% while slight minority work constantly for the same people (43%). 

Working for researchers or working within a research software group is different than working on the same project with other developers. On average they work on a bit more than 3 different projects at the same time.

RSEs have programming skills that is not necessarily shared within their field. Therefore, they can train other researchers to develop some best practices or learn how to program more efficiently. 78% of them participate to such training. They are not teaching directly to students (as seen in section 2) but transferring skills is an important aspect of their job. In average, they do training twice a year. In average, they do training six times a year (by removing any participants who claimed to do more than 52 trainings per year). These trainings are more often done under the form of workshop or with Software Carpentry than traditional teaching. A type of training probably more adapted to teach computing skills.


## Collaboration
### Do you work for a Research Software Group?
### How many software projects are you currently involved in?

## Training
### Have you ever trained researchers in computational techniques?
### On average, how many times a year do you take part in providing training?
### What training programs are you involved with (comma separated list) (For example, Software Carpentry, local university training, etc.)


# Section 7. Publications

RSEs is an hybrid role between a researcher and a software developer. We investigated both of these aspects concerning publication and dissemination of their work, one on the traditional aspect of it (publications and conference) and on the more software aspect (open source and DOI).
One essential aspect of career in academia is the publications and the conferences to gain recognition. However, the role of RSE being less about writing articles than creating the infrastructure and the software for the article to exist, there is some fear that they will fail to have recognition through the papers and conferences.
Our results support this idea, while for 90% of the participants, their software is used in published researches they are only 71% (among them) who are acknowledged in the publication.

Among these participants that are acknowledged in the paper, only 29% are generally named as main author for the paper. Among the 71% of those who are not main author, 80% are at least mentioned as co-authors. And among these RSEs that are not mentioned as co-author or main author, 54% are at least generally acknowledged in the main text of the paper.
On conference, the number of RSEs that present their work in conference is rather small, only 65% of RSEs present their work in conferences or workshops.


One important development practice is how the code is distributed and if the RSEs are releasing their work under open licence.
We asked the participants if they have ever released their work under open source licence and 81% of them replied by the affirmative. 
it is seems that the vast majority of them doing it all the time (40%). Therefore, as soon as the step to open source is done, it seems that RSEs seems a constant interest in it. However, they rarely use a Digital Object Identifier (DOI) to help to identify their software, only 32% of them are doing it. And the frequency of use of the DOI among them is much more variable than for the open licence meaning they are less convince by the utility of it compared to open licence.


## Academic publications
### Has your software contributed to research that has been published in a journal or at a conference?; In general, when your software contributes to a paper, are you acknowledged in that paper?; Are you generally named as the main author of the paper?; Are you generally named as a co-author of the paper?; Are you generally acknowledged in the main text of the paper?
### Have you ever presented your software work at a conference or workshop?
### Which conference(s)/workshop(s) (comma separated list with FULLNAME (ACRONYM))

## Open Source
### Have you ever released your software under an open-source license?
### How often do you release the software projects you've worked on under an open-source license?
### Have you ever used a Digital Object Identifier (DOI) to identify your software?
### How often do you associate your software with a Digital Object Identifier (DOI)?


# Section 8. Sustainability and technical details

This section comprises two subsections that focus on the technical and development aspects of the RSEs' work. They aim to understand good practices in developing software and which tools are important for RSEs.

Developing software requires a set of good practices to ensure the quality of the subsequent analysis as well as the robustness of the developed software, to name a few of important aspects. We wanted to see if the implementation of some simple but essential good practices were a reality. Three measures were created, the implementation of testing, the bus factor and the technical hand over plan.
These metrics allows to see the importance of the RSEs role in their team but also if they are themselves implementing some practices that are used widely in industry but less in academic research.

We asked the participants to choose any of the following testing methods:
* Test engineers conduct testing
* Developers conduct testing
* Users conduct testing
* No formal testing

Obviously, the *test engineers conduct testing* is the most potential testing method but may not be possible in number of small projects while, no formal testing should not occur in any ideal scenario, regardless of the size of the project. Only 7% of the participants confessed they were not implementing any testing at all. When they are conducting testing, the RSEs seems to prefer (or only able to implement) *developer testing* (52% of them) or letting the users conduct the testing (35%), while the use of test engineers is marginal (6%).

We chose two broad measures to provide an insight into sustainability: the bus factor and technical hand over planning. The bus factor is a measure of the number of developers who understand a specific software project and could, with only a cursory review of the project, maintain or extend the code. A project with a bus factor of 1 is completely reliant on only one developer. If this developer finds new employment, becomes ill or is hit by the titular bus, then the project will fail. A high bus factor provides some confidence that the project can be sustained even if a developer leaves. A technical hand over plan is used to introduce a new developer to a software project. These plans cover basic information, such as the licence and location of the software, a repository, a description of the software architecture, a summary of development plans and any other information that a new developer would need to understand the software. A project that has written (and maintained) a technical hand over plan can withstand the departure of a developer, even a key developer, significantly better than one without such a plan.

On majority of the RSEs' projects the bus factor is low, 39% of the project have a bus factor of 1 followed by a bus factor of 2 (27%). Higher bus factor is only marginal with only 13% of the projects having a bus factor of 3, 5% of a bus factor of 4 and 7% a bus factor equal or higher than 5.
The presence of a technical plan, which can mitigate the low bus factor in the different projects is really low (18%) and presents a risk of project failures.


On technical details we wanted to know which of the programming languages are mostly used by the RSEs. We give them a multi-choice list inspired by the [results](https://insights.stackoverflow.com/survey/2017#most-popular-technologies) published by Stackoverflow. Python is the most used language (18%) followed by C, C++ and R (10% each). The rests of the languages that are higher than 5% are Fortran (8%), SQL (7%), Matlab (7%) and JavaScript (7%).
About which Operating System used by RSEs, a majority are using GNU/Linux (54%) followed by OS X (35%) and Windows (10%).


## Good practices
### In general, what sort of testing do you conduct on your software? (check all that apply)
### What is the bus factor of your most important software project? (the bus factor is the number of team members who, if run over by a bus, would put the project in jeopardy, so 1 means the project is dependent on a single person)
### Is there a technical hand-over plan for your most important software project?

## Technical details
### What programming languages do you use at work? (Select as many as apply)
### What Operating System do you prefer to use at work?


# Section 9. Job satisfaction

The job satisfaction is an essential pulse to take about the community. It helps to track the evolution and the current state of the RSEs within their role and to catch any sign of structural or organisational dysfunction that are translated into well-being. There are a lot of different metrics to measure the quality of a job on a personal and psychological level [4]. Several models exist to understand the link between different factors of job satisfaction and turnover intention [5]–[9]. Turnover intention is an important measure that is highly associated with the risk of employees leaving the organisation [7]. Job satisfaction is important in retaining RSEs. Perceived employability provides information on how workers values their own skills in regard of the market. To measure the different attitudes toward the RSE role, we used scales that have been created in [5], [6], [8], [9]. These are Likert scale [10], which are 5 point ordinal scales graduated from Strongly disagree to Strongly agree. Each scale is composed of several so called items (i.e. questions) that each measure one attitude.

Beside these specific concepts we asked more general question about their satisfaction in their current position and their satisfaction with their career in general with a range of answers from *0 - Not at all satisfied* to *10 - Completely satisfied*, 80% of the participants answered more than 5 to the scale (which can be considered as a neutral position) to the question about their satisfaction about their current position. For the question about their satisfaction with their career in general (and using the same scale), 84% of the participants answered more than 5 to the scale.

The specific questions about their job satisfaction reflect, in general, the same opinion as the two more generic questions. However, the granularity helps to identify a couple of issues that would not appears with generic questions:

* *The feedback about the performance*: These questions ask if the RSEs feel that they receive enough information about their work and their performance. While they seems to have enough information about the purpose of their work and having access to sufficient data and information, they are less assertive about the feedback they receive from their colleagues and their supervisors.

* *The turnover intention*: These questions aim to measure the desire to quit their current position. Overall, the participants are not willing to leave their position and are not necessarily searching for other job, even if the potential job would offer the same compensations.

* *The perceived employability*: This concept is linked to the previous one. People may not have the intention to leave their jobs, not because they like it, but because they fear they are not employable. This is not the case here, the participants consider themselves more often employable than not.

* *The affective recognition*: This concept try to see if the participants receive positive feedback from their supervisors. Overall, again the participants report a positive relation with their supervisors. It means they are not systematic issues with direct management.

* *Affective satisfaction*: Here, the concept measures how much the participants enjoy and like their job. The answers were positive and again, reflect the answers given at the more generic questions.

* *The possibility of progression*: This question aims to study the possibility of evolution for the RSEs, if information is available and if they see a possibility of evolution within their current career. This is the only questions that clearly received negative answers. To summarise, even if the RSEs have planned to be in this position, as a part of their career plan, the majority of them think they cannot be promoted in their current group, neither the information for such progression is easily accessible.


## General satisfaction

## Feedback about performance
### Do you receive sufficient information on the results of your work?; Does your work give you the opportunity to check on how well you are doing your work?; In your work, do you have access to sufficient data and information?; Do you receive sufficient information on the purpose of your work?; Does your work provide you with direct feedback on how well you are doing your work?; Does your supervisor/line manager inform you about how well you are doing your work?; Do your colleagues inform you about how well you are doing your work?

## Turnover intention

### How often do you feel frustrated when not given the opportunity to achieve your personal work-related goals?; How often do you look forward to another day at work?; How often do you consider leaving your job?; How often do dream about getting another job that will better suit your needs?
### My current job satisfies my personal needs; I would accept another job at the same compensation level if I was offered it

## Perceived Employability
### It would not be very difficult for me to get an equivalent job in a different organization; I can think of a number of organizations that would probably offer me a job; My experience is in demand on the labor market; Given my qualifications and experience, getting a new job would not be very hard at all

## Affective recognition

### I am satisfied with my supervisor/line manager's confidence in me; I am satisfied with a word of thanks from my supervisor/line manager; I am satisfied with the recognition I receive from my supervisor/line manager for doing my job; I am satisfied with the compliments from my supervisor/line manager concerning my work; I am satisfied with the encouragement from my supervisor/line manager while doing my job


## Affective satisfaction

### I find real enjoyment in my job; Most days I am enthusiastic about my job; I feel fairly well satisfied with my job; I like my job better than the average person

## Possibility of progression

### It is likely that I will gain a promotion within my current group; The process I have to complete to gain a promotion is clear and understandable; There are many opportunities within my chosen career plan; My current position is an integral part of my career plan; It is likely that my next position will be an RSE role


# Section 10. Research Software Engineer

This last section regroups different questions about RSEs in general, the specific skills for them, where they meet other RSEs and if they are part of the UK RSE Association. 

About the skills we asked them what type of skills are important to become a RSE and how they did learn them. Both questions are displayed as wordcloud and the list of the different answers. 

The last section was about the RSE network, specific to USA. It appears that the network is not really efficient yet. First, to the question where they meet other RSE, only 20% of them chose between the different propositions, with a higher number in local RSE group (18%) which is normal knowing that only 6% are members of the UK RSE Association. 

## Skills

### What three skills would you like to acquire or improve to help your work as a Research Software Engineer? The skills can be technical and non-technical.
### How did you learn the skills you need to become an RSE?

## RSE Network

### Are you a member of the UK RSE Association? (Members are people who have signed up to the UK RSE mailing list)
### How do you meet other RSEs?

