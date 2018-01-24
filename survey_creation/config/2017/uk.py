"""
Config file specific to uk to create automated survey
"""

class config:

    additional_language = 'nl'
    # To modify, just add the keys of the dictionary
    header_to_modify = [{'class': 'S', 'name': 'sid', 'text': '421498'},
                        {'class': 'S', 'name': 'admin_email', 'text': 'olivier.philippe@soton.ac.uk'}]
    # Same as header_to_modify
    description_to_modify = []

    # Add header and description. Tuple of a dictionary + the position where it is supposed
    # to be inserted
    header_to_add = []
    description_to_add = [({'class': 'S', 'name': 'additional_languages', 'text': 'nl'}, 12)] # The index positions starts at 0
