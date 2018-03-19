# Modifications from the 2017 survey

I modify the process of survey creation for this year into a single one surveys.

## Advantages

1. One survey launch for every countries meaning one address and one work of diffusion (even if each country still needs to reach its own audience)

2. A better collaborative approach as everyone work on the same questions

3. A easier analysis process with all the data being in the exact same dataset with the exact same title.

4. During the survey creation, working on a master file for all questions and answers will help to fix and update all the questions at the same time.

5. It is easier for everyone to see which questions the others countries are asking.

6. It is possible to offer a generic survey that people who are not necessarily from any of our country can still answer.

I also keep the benefits of the previous approach which are:

1. Each country can decide which questions is included or not

2. Adapting the answer to each specific countries (such as organisations, salaries, ...).


## Drawbacks

However there are some drawbacks that I can think of right now. Don't hesitate to add anything you can think of (here or as an issue on github). I duplicate them as issue on github but copy them here for completness.

1. We need to change some questions to make them more generic and avoid the specific mention of the country.

2. The translation will be available for each countries while it would only work for the country that did it (for instance the german). The only way I can see how we can workaround that it is to put a disclaimer at the beggining.

3. The introduction and ending text will also need to be more generic and will be shared accross all surveys.

4. The mention *Research Software Developer* is not allowed everywhere (such as Canada). We need at least an alternative term that will be presented alongside RSE. I can think of *Research Software Developer*. In practice a question would look like: *Is there any Research Software Engineer (RSE) / Research Software Developer (RSD) group in your country*. If you think of a better alternative, please raise a ticket on github.


## Modified questions from 2017.

- Removed:

- Merged:

- Answers reworked:

- Added: I did not add any questions, I think it is on lower priority now and should be done when we have a cleaner version of the current survey.


## Modifications on the file structure

Working with a common questions.csv file brings a slightly different approach on how to work.

1. Before you had a separated file for the questions. Now you decide in the appropriate column of your country which question you want or not (with 'Y' or 'N').

2. The answers's file is still indicated in the questions file. However, all the answers files are grouped in one folder [INSERT LINK] and we all have the same one. For the questions you need to adapt to your own country (such as salary or university list) you create a file in your respective folder with the same name as the answer file and populate it with your own answers. In this way, only divergent version of answers are created in separated folders.
