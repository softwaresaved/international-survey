README
======
How to distribute the survey in Germany?
----------------------------------------

  - de-RSE mailing list
  - wiss-software@listserv
  - via Allianzinitiative?
  - AG open science
  - orcid mailingliste?
  - contacts within research organisations
    - HGF, Martin
    - MPG, Stephan
    
People doing work here
----------------------

  * katrinleinweber
  * mrtnhmtz
  * StephanJanosch



to do - missing
---------------

Overall
- Remove files not used
- When translation is finished and survey is set-up for testing ask others to conduct a test with a dry run participation

[de_17.csv](de_17.csv)
- Check question list of other national RSE groups to reuse missing questions
- Prioritize and add additional, Germany related, questions
- Double-check translations
- ~~Double-check dropping of socio5, disa1, ukrse1~~ done
- What's the difference between affRec2-4?
  - These are idoms. We should try to find good translations that match the meaning of the idioms.
  - If no better translation is found we keep them as is.
- ~~Is addiing question rse4de okay?~~ Done , is okay
- Clarify use of "RSE" in questions, equivalent description and possibly information in the welcome text of the survey

[academic_field.csv](listAnswers/academic_field.csv)
- Clarify if classes are equivalent in Germany or need changes
- Double-check translation

[countries.csv](listAnswers/countries.csv)
- Translate; will do this afternoon. Stephan

[decision_job.csv](listAnswers/decision_job.csv)
- ~~Double-check translations~~ done
- Add or match related question in [de_17.csv](de_17.csv)

[funding.csv](listAnswers/funding.csv)
- Clarify, really we have to -> Wait for results from test run to check if it's really problematic

[salary.csv](listAnswers/salary.csv)
- ~~Define equivalent classes in EUR and translate, Try to keep equivalent classes~~ done
- The idea is to get information if RSEs are underpayed, so matching TVöD doesn't seem to be a good idea
- TVöD classes (Maybe hint for Entgeldgruppen) is difficult since since several steps in a group might make a huge difference
- Translate/Adapt the UK salaries in a clever way to german model (then use salary_de.csv) ?
- Consider adding 1-2 additional questions asking for the type of tariff and then (conditionally) ask for the tariff group ?
- ~~Delete salaries.csv~~ done

[work_researchers.csv](listAnswers/work_researchers.csv)
- No related question found in [de_17.csv](de_17.csv) - shall we drop the file?
- Translate


Stephan's notes from 2017-07-25
-------------------------------

The lists of institutions are fetched from wikidata. A Knime workflow creates the corresponding files. https://github.com/softwaresaved/international-survey/blob/master/survey_creation/de_17/de_17_resources.knwf
 
Stephan's notes from 2017-07-19
-------------------------------

I started translating. I did choose the german 'Du'. I used [https://github.com/jakob/TableTool] which quoted everything. Issue about this raised: [https://github.com/softwaresaved/international-survey/issues/59]

The welcome message stands still side by side for comparison. 

older notes
-----------


careful translation to include as much people as possible
  not put engineering part into foreground

add (or remove) questions if feasible

member of association

Record who has been contacted and when, when sending the invitation to fill the survey! It's important to understand the results finally.

Aim to release the German survey by mid or end of August and close it by end of September.
  - Consider time to set-up and test final LimeSurvey
  - Make use of RSE17 publicity to spread invitation for survey


neue Fragen
-----------

  - ~~SJ: Bist Du auf der de-RSE Mailingliste eingeschrieben? http://www.de-rse.org/de/join.html~~ done

  - ~~DOI yes: (conditional)~~
  --  ~~software directly or paper referencing~~
  --  ~~what infrastructure tools (librariers, Zenodo)~~
  		
  - ~~SJ: Hast du einen "ORCID identifier"~~ done
  - SJ: Wüsstest Du eine bessere Bezeichnung als RSE? Wenn ja, welche? (Bedenke die Spannbreite)
  - SJ: Wünschst du dir eine Konferenz in D zu dem Thema wissenschaftliche Softwareentwickling?
  	- if yes: ask for permissions to contact and ask for email in external google form
  - AL: Welche Metriken/Tools benutzt Du, um die "Beliebtheit" Deiner Software zu verfolgen? "Don't care", "I don't know" ,Downloads, Stars auf GitHub etc.?
  -  - think about the goal of the question
  - can_17: How many software developers typically work on your projects? (answer file: ?, get from canada notebook)

weitere mögliche Fragen
-----------------------

  - SJ: Arbeitest du allein oder im Team mit anderen RSEs?
  - Wie bist du vernetzt in deiner Institution?
  - DL: Ermöglicht es dir dein Arbeitgeber (finanziell) zu Fortbildungen zum Thema Softwareentwicklung/Programmierung zu reisen? 
  - DL: Hast du das bereits wahrgenommen?
  - KL: Gibt es vor Ort Fortbildungsangebote?
  - KL: Hast du diese bereits wahrgenommen?
  - DL: Bist du bei deinem Arbeitgeber mit anderen Softwareentwickler_innen / Programmierer_innen vernetzt? Wenn ja, wie?
  - DL: Steht dir vor Ort Infrastruktur zur Softwareentwicklung zur Verfügung (z.B. eigene Instanzen von Plattformen zur Kommunikation, zum Projektmanagement, zur Versionskontrolle, zum automatisierten Testing/Building, etc.)?
  - SJ: Kennst du den Begriff RSE?
  - SJ: Hast du schon etwas vom SSI gehört?
  - SJ: Welchen Organisationen/Gruppen stehst du im Bezug auf deine Arbeit nahe?
  - SJ: Gibt es Richtlinien wie mit Quellcode umgegangen werden soll?
  - SJ: Kann dein Chef programmieren?
 
 DL: David Laehnemann
 SJ: Stephan Janosch
 
 * Hast Du Software in Publikationen veröffentlicht? Wie, d.h. extra Softwarepublikation oder innerhalb einer größeren Pub?
* Veröffentlichst Du Software vor einer Publikation, z.B. ala GitHub/Zenodo?
* Welche Plattformen benutzt Du für Veröffentlichung?
* Wird Deine Software zitiert auch ohne Veröffentlichung? Wie registrierst Du dies?
* Trägt eine Softwarezitierung anstatt einer Publikationszitierung zu Deiner Karriere bei?

Viele Grüße,
Andreas Leimbach 
 
  
