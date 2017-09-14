"""
Config file specific to uk to create automated survey
"""


class config:

    # To modify, just add the keys of the dictionary
    header_to_modify = [{'class': 'S', 'name': 'sid', 'text': '421498'},
                        {'class': 'S', 'name': 'admin_email', 'text': 'olivier.philippe@soton.ac.uk'},
                        {'class': 'S', 'name': 'allowprev', 'text': 'Y'}]
    # Add header and description. Tuple of a dictionary + the position where it is supposed
    # to be inserted
    header_to_add = [({'class': 'S', 'name': 'additional_languages', 'text': 'de'}, 12)]

    # Same as header_to_modify
    description_to_modify = []
    description_to_add = []
    languages_to_add = 'de'

    # The index positions starts at 0
    # Adding the survey title to the global description. The index position is at 0 and the structure of the dictionary is as follow:
    # {'class': 'SL', 'name': 'surveyls_title', 'text': 'DEMO -- RSE Survey -- 2017 -- EN', 'language': 'en'}
    survey_title = {'en': 'RSE study for Germany',
                    'de': 'RSE study for Germany'}

    sections_txt = {0: {'en': {'name': 'Questions about you', 'text': ''},
                        'de': {'name': 'Question about you', 'text': ''}},
                    1: {'en': {'name': 'Your current employment', 'text': ''},
                        'de': {'name': 'Your current employment', 'text': ''}},
                    2: {'en': {'name': 'Your employment history', 'text': ''},
                        'de': {'name': 'Your employment history', 'text': ''}},
                    3: {'en': {'name': 'Your working practices', 'text': ''},
                        'de': {'name': 'Your working practices', 'text': ''}},
                    4: {'en': {'name': 'Your perception of your current position', 'text': ''},
                        'de': {'name': 'Your perception of your current position', 'text': ''}},
                    5: {'en': {'name': 'Demographic questions', 'text': ''},
                        'de': {'name': 'Demographic questions', 'text': ''}},
                    6: {'en': {'name': 'Final question about you', 'text': ''},
                        'de': {'name': 'Final question about you', 'text': ''}}}
