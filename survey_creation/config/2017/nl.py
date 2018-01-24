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
    header_to_add = []

    # Same as header_to_modify
    settings_to_modify = []
    settings_to_add = []

    # The index positions starts at 0
    # Adding the survey title to the global description. The index position is at 0 and the structure of the dictionary is as follow:
    survey_title = {'en': 'Survey: Research Software Engineering in the Netherlands'}

    sections_txt = {0: {'en': {'name': 'Questions about you', 'text': ''}},
                    1: {'en': {'name': 'Your current employment', 'text': ''}},
                    2: {'en': {'name': 'Your employment history', 'text': ''}},
                    3: {'en': {'name': 'Your working practices', 'text': ''}},
                    4: {'en': {'name': 'Your perception of your current position', 'text': ''}},
                    5: {'en': {'name': 'Demographic questions', 'text': ''}},
                    6: {'en': {'name': 'Final questions about you', 'text': ''}}}

    private_data = {'en': 'IMPORTANT: This information will not be made publicly available'}
