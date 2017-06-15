#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__: 'Olivier PHILIPPE'
__licence__: 'BSD3-clause'

"""
Scrip to programatically generate notebook for exploratory analysis
Use the code from: https://gist.github.com/fperez/9716279
"""

import nbformat as nbf

from data_process.uk_2017 import cleaning as uk_2017_cleaning
from data_process.uk_2017 import action_file as uk_2017_action
print(uk_2017_cleaning)


def example_generate_notebook():
    """
    Scrip to programatically generate notebook for exploratory analysis
    Use the code from: https://gist.github.com/fperez/9716279
    """
    nb = nbf.v4.new_notebook()

    text = """\
                # My first automatic Jupyter Notebook
                  This is an auto-generated notebook.\
           """

    code = """\
                %pylab inline
                hist(normal(size=2000), bins=50);"""

    nb['cells'] = [nbf.v4.new_markdown_cell(text),
                   nbf.v4.new_code_cell(code)]

    fname = './notebooks/test.ipynb'

    with open(fname, 'w') as f:
        nbf.write(nb, f)


def main():
    print(uk_2017_action.

if __name__ == "__main__":
    main()
