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
from include.config import CleaningConfig
from include.get_arguments import get_arguments


def main():
    year, country = get_arguments(sys.argv[1:])
    # load dataset

    cleaning_config = CleaningConfig(year, country)
    df = pd.read_csv(cleaning_config.raw_data)
    cleaning_process = CleaningData(df)
    df = cleaning_process.cleaning()
    cleaning_process.write_df()
    cleaning_process.write_config_file()


if __name__ == "__main__":
    main()
