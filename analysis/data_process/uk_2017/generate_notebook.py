#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__: 'Olivier PHILIPPE'
__licence__: 'BSD3-clause'

"""
Scrip to programatically generate notebook for exploratory analysis
Use the code from: https://gist.github.com/fperez/9716279
"""

import nbformat as nbf


class GenerateNotebook:
    """
    """
    def __init__(self, notebook_filename):
        """
        """
        self.outfilename = notebook_filename
        # Generate an empty notebook
        self.nb = nbf.v4.new_notebook()

    def add_text(self, text_to_add):
        """
        """
        formatting_text = nbf.v4.new_markdown_cell(text_to_add)
        self._append_notebook(formatting_text)

    def add_code(self, code_to_add):
        """
        """
        formatting_code = nbf.v4.new_markdown_cell(code_to_add)
        self._append_notebook(formatting_code)

    def _append_notebook(self, cell_to_add):
        """
        """
        self.nb['cell'].append(cell_to_add)

    def example_generate_notebook():
        """
        Scrip to programatically generate notebook for exploratory analysis
        Use the code from: https://gist.github.com/fperez/9716279
        """

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

    def save_notebook(self):
        """
        Save the notebook on the hard drive
        """
        with open(self.outfilename, 'w') as f:
            nbf.write(nb, f)


def main():
    pass


if __name__ == "__main__":
    main()
