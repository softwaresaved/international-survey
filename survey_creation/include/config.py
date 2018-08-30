"""
Config file for survey creation
"""


class config:

    # To modify, just add the keys of the dictionary
    header_to_modify = [{'class': 'S', 'name': 'sid', 'text': '421498'},
                        {'class': 'S', 'name': 'admin_email', 'text': 'olivier.philippe@soton.ac.uk'},
                        {'class': 'S', 'name': 'allowprev', 'text': 'Y'}]
    # Add header and description. Tuple of a dictionary + the position where it is supposed
    # to be inserted
    header_to_add = [({'class': 'S', 'name': 'additional_languages', 'text': '"fr de-informal"'}, 12)]
    # header_to_add = [({'class': 'S', 'name': 'additional_languages', 'text': 'de-informal'}, 12)]

    # Same as header_to_modify
    settings_to_modify = []
    settings_to_add = []
    languages_to_add = ['de-informal', 'fr']
    # languages_to_add = ['de-informal']

    # The index positions starts at 0
    # Adding the survey title to the global description. The index position is at 0 and the structure of the dictionary is as follow:
    survey_title = {'en': 'Study about people writing research software',
                    'de-informal': 'STUDY TEST',
                    'fr': 'Etude sur les personnes écrivant des programmes informatiques scientifiques'}

    sections_txt = {0: {'en': {'name': 'Questions about you', 'text': ''},
                        'de-informal': {'name': 'Fragen zu Deiner Person', 'text': ''},
                        'fr': {'name': 'Questions à propos de vous', 'text': ''}},
                    1: {'en': {'name': 'Your current employment', 'text': ''},
                        'de-informal': {'name': 'Fragen zu Deiner jetzigen Anstellung', 'text': ''},
                        'fr': {'name': 'Votre position actuelle', 'text': ''}},
                    2: {'en': {'name': 'Your employment history', 'text': ''},
                        'de-informal': {'name': 'Fragen zu Deinen bisherigen Anstellung(en)', 'text': ''},
                        'fr': {'name': 'Votre passé professionel', 'text': ''}},
                    3: {'en': {'name': 'Your working practices', 'text': ''},
                        'de-informal': {'name': 'Fragen zu Deinen Arbeitsgewohnheiten', 'text': ''},
                        'fr': {'name': 'Vos pratiques profesionnelles', 'text': ''}},
                    4: {'en': {'name': 'Your perception of your current position', 'text': ''},
                        'de-informal': {'name': 'Deine Wahrnehmung Deiner aktuellen Position', 'text': ''},
                        'fr': {'name': 'Votre perception sur votre position actuelle', 'text': ''}},
                    5: {'en': {'name': 'Demographic questions', 'text': ''},
                        'de-informal': {'name': 'Demographische Fragen', 'text': ''},
                        'fr': {'name': 'Questions démographiques', 'text': ''}},
                    6: {'en': {'name': 'Final questions about you', 'text': ''},
                        'de-informal': {'name': 'Die letzen Fragen über Dich', 'text': ''},
                        'fr': {'name': 'Dernières questions à propos de vous', 'text': ''}}}

    private_data = {'en': 'IMPORTANT: This information will not be made publicly available',
                    'de-informal': 'IMPORTANT: This information will not be made publicly available [DE-INFORMAL]',
                    'fr': 'IMPORTANT: Cette information ne sera pas rendue publique [FR]'}
