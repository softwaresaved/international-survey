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

international-survey/survey_creation/de_17/de_17.csv
- Check question list of other national RSE groups to reuse missing questions
- Prioritize and add additional, Germany related, questions
- Double-check translations

international-survey/survey_creation/de_17/listAnswers/academic_field.csv
- Clarify if classes are equivalent in Germany or need changes
- Translate

international-survey/survey_creation/de_17/listAnswers/countries.csv
- Translate

international-survey/survey_creation/de_17/listAnswers/decision_job.csv
- Double-check translations
- Not used, ignore?

international-survey/survey_creation/de_17/listAnswers/education.csv
- Needs clarification

international-survey/survey_creation/de_17/listAnswers/ethnicity.csv
- Clarify if this question make sense for German survey
- Clarify if translation makes sense or if equivalent or different classes for German survey should be used
- Translate

international-survey/survey_creation/de_17/listAnswers/funding.csv
- Clarify, really we have to ;-)

international-survey/survey_creation/de_17/listAnswers/previous_job.csv
- Clarify

international-survey/survey_creation/de_17/listAnswers/reasons_leave_job.csv
- Double-check translations

international-survey/survey_creation/de_17/listAnswers/salaries.csv
- Define equivalent classes in EUR and add the in EN in DE
- Add examples, e.g. TVöD classes ...
- Translate (translate the UK salaries in a clever way to german model. Maybe hint for Entgeldgruppen.)
- or is it salary.csv

international-survey/survey_creation/de_17/listAnswers/testing.csv
- Double-check translations

international-survey/survey_creation/de_17/listAnswers/type_contract.csv
- Add "(Student) Research Assistant";"Wissenschaftliche/Studentische Hilfskraft" ?
- Devide "Fixed term";"Befristeter Vertrag" into "Haushaltmittel" and "Drittmittel"?
- Add other types of contract?

international-survey/survey_creation/de_17/listAnswers/type_organisation.csv
- Needs clarification for "Government" and "Private Company"

international-survey/survey_creation/de_17/listAnswers/ukrse.csv
- Double-check addition of new option "DE-RSE Community";"DE-RSE Community"
- Double-check if URLs for RSE communities are useful
- Clarify if additional text field makes sense for option "Local RSE group/network";"Andere RSE Gruppen und RSE ähnliche Netzwerke"

international-survey/survey_creation/de_17/listAnswers/work_researchers.csv
- Not used, ignore?


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

  - SJ: Bist Du auf der de-RSE Mailingliste eingeschrieben? (http://www.de-rse.org/de/join.html) (replaces q for uk rse ml)
  - SJ: Kollaborierst du mit Deiner Bibliothek beim Veröffentlichen/Archivieren von Software?
  - SJ: Hast du einen "ORCID identifier"
  - SJ: Wüsstest Du eine bessere Bezeichnung als RSE? Wenn ja, welche? (Bedenke die Spannbreite)
  - SJ: Arbeitest du allein oder im Team mit anderen RSEs?
  - SJ: Wünschst du dir eine Konferenz in D zu dem Thema wissenschaftliche Softwareentwickling?
  - AL: Welche Metriken/Tools benutzt Du, um die "Beliebtheit" Deiner Software zu verfolgen? Downloads, Stars auf GitHub etc.?


weitere mögliche Fragen
-----------------------

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
 
  
