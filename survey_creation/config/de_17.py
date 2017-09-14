"""
Config file specific to de_17 to create automated survey
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
    survey_title = {'en': 'Study about people writing scientic software for Germany',
                    'de': 'Umfrage zur Softwareentwicklung in der deutschen Wissenschaft'}

    sections_txt = {0: {'en': {'name': 'Questions about you', 'text': ''},
                        'de': {'name': 'Fragen zu Deiner Person', 'text': ''}},
                    1: {'en': {'name': 'Your current employment', 'text': ''},
                        'de': {'name': 'Fragen zu Deiner jetzigen Anstellung', 'text': ''}},
                    2: {'en': {'name': 'Your employment history', 'text': ''},
                        'de': {'name': 'Fragen zu Deinen bisherigen Anstellung(en)', 'text': ''}},
                    3: {'en': {'name': 'Your working practices', 'text': ''},
                        'de': {'name': 'Fragen zu Deinen Arbeitsgewohnheiten', 'text': ''}},
                    4: {'en': {'name': 'Your perception of your current position', 'text': ''},
                        'de': {'name': 'Deine Wahrnehmung Deiner aktuellen Position', 'text': ''}},
                    5: {'en': {'name': 'Demographic questions', 'text': ''},
                        'de': {'name': 'Demographische Fragen', 'text': ''}},
                    6: {'en': {'name': 'Final questions about you', 'text': ''},
                        'de': {'name': 'Die letzen Fragen über Dich', 'text': ''}}}
