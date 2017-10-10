#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Script to preprocess the raw dataset prior to any analysis. This script is launched only on
the researchers computer as (s)he is the only one to have access to the raw dataset
"""

import os
import sys
import getopt
import pandas as pd
from include.preprocessing import CleaningData


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
        folder_path = os.path.join(year, country)
        return folder_path
    else:
        print('Need a country and a year. Please use the following command:\n' +
              '\trun.py -c <country> -y <year>')
        sys.exit(2)


def main():

    folder = get_arguments(sys.argv[1:])
    # load dataset
    df = pd.read_csv(raw_data)
    cleaning_process = CleaningData(df)
    df = cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()


if __name__ == "__main__":
    main()
