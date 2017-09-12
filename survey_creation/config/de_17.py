"""
Config file specific to uk to create automated survey
"""


class config:

    # To modify, just add the keys of the dictionary
    header_to_modify = [{'class': 'S', 'name': 'sid', 'text': '421498'},
                        {'class': 'S', 'name': 'admin_email', 'text': 'olivier.philippe@soton.ac.uk'}]
    # Same as header_to_modify
    description_to_modify = []

    # Add header and description. Tuple of a dictionary + the position where it is supposed
    # to be inserted
    header_to_add = [({'class': 'S', 'name': 'additional_languages', 'text': 'nl'}, 12)]
    # The index positions starts at 0
    description_to_add = []

    sections_txt = {0: {'en': {'name': 'Questions about you', 'text': ''},
                        'nl': {'name': 'Question about you', 'text': ''}},
                    1: {'en': {'name': 'Your current employment', 'text': ''},
                        'nl': {'name': 'Your current employment', 'text': ''}},
                    2: {'en': {'name': 'Your employment history', 'text': ''},
                        'nl': {'name': 'Your employment history', 'text': ''}},
                    3: {'en': {'name': 'Your working practices', 'text': ''},
                        'nl': {'name': 'Your working practices', 'text': ''}},
                    4: {'en': {'name': 'Your perception of your current position', 'text': ''},
                        'nl': {'name': 'Your perception of your current position', 'text': ''}},
                    5: {'en': {'name': 'Demographic questions', 'text': ''},
                        'nl': {'name': 'Demographic questions', 'text': ''}},
                    6: {'en': {'name': 'Final question about you', 'text': ''},
                        'nl': {'name': 'Final question about you', 'text': ''}}}
