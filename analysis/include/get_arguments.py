#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt

"""
Short script to parse
the argments from the command line
"""


def get_arguments(argv):
    """
    """
    country = None
    year = None
    try:
        opts, args = getopt.getopt(argv, 'hc:y:', ['country=', 'year='])
    except getopt.GetoptError:
        print('run.py -c <country> -y <year>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('run.py -c <country> -y <year>')
            sys.exit()
        elif opt in ('-c', '--country'):
            country = arg
        elif opt in ('-y', '--year'):
            year = arg
    if country and year:
        # folder_path = os.path.join(year, country)
        return year, country
    elif int(year) >= 2018:
        return 2018, None
    else:
        print('Need a country and a year. Please use the following command:\n' +
              '\trun.py -c <country> -y <year>')
        sys.exit(2)
