#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
from config import NotebookConfig

__author__: 'Olivier PHILIPPE'
__licence__: 'BSD3-clause'

"""
Scrip to programatically generate notebook for exploratory analysis
Use the code from: https://gist.github.com/fperez/9716279
"""


class GenerateNotebook(NotebookConfig):
    """
    """
    def __init__(self, notebook_filename):
        """
        """
        self.outfilename = notebook_filename
        # Generate an empty notebook
        self.nb = nbf.v4.new_notebook()
        self._import()
        self._setup_display()
        self._setup_matplotlib()
        self._load_dataset()
        # Processor to run the notebook
        self.processor = ExecutePreprocessor(timeout=600,
                                             kernel_name='python3',
                                             allow_errors=self.allow_errors)

    def _import(self):
        """
        Import all the needed library
        """
        self.add_section('Importing modules')
        import_code = '\n'.join(self.to_import)
        self._add_code(import_code)

    def _setup_display(self):
        """
        Extending the limit of rows and columns
        displayed
        """
        rows = """pd.set_option('display.max_rows', 1000)"""
        columns = """pd.set_option('display.max_columns', 1000) """
        self._add_code('\n'.join([rows, columns]))

    def _setup_matplotlib(self):
        """
        Set up matplotlib for Jupyter
        """
        magic_inline = """get_ipython().magic('matplotlib inline')  # Activate that line to use in Jupyter """
        size_figures = """matplotlib.rcParams['figure.figsize'] = (15.0, 8.0)"""
        self._add_code('\n'.join([magic_inline, size_figures]))

    def _load_dataset(self):
        """
        """
        self._add_text('# Loading dataset')
        loading = """df =  pd.read_csv('{}')""".format(self.cleaned_df_location)
        self._add_code(loading)

    def add_section(self, text):
        """
        """
        self._add_text('# Section: {}'.format(text))

    def add_group(self, text):
        """
        """
        self._add_text('## Group of question: {}'.format(text))

    def add_question_title(self, text):
        """
        """
        self._add_text('### {}'.format(text))

    def add_count(self, *args):
        """
        """
        count_count = """v_to_count = get_count(df, {},
                                                "{}",
                                                "{}")""".format(*args)
        self._add_code(count_count)

    def add_display(self):
        """
        """
        display = """display(v_to_count) """
        self._add_code(display)

    def add_plot(self, *args):
        """
        """
        plot = """_ = get_plot(v_to_count, "{}")""".format(*args)
        self._add_code(plot)

    def _add_text(self, text_to_add):
        """
        """
        formatting_text = nbf.v4.new_markdown_cell(text_to_add)
        self._append_notebook(formatting_text)

    def _add_code(self, code_to_add):
        """
        """
        formatting_code = nbf.v4.new_code_cell(code_to_add)
        self._append_notebook(formatting_code)

    def _append_notebook(self, cell_to_add):
        """
        """
        self.nb.setdefault('cells', []).append(cell_to_add)

    def run_notebook(self):
        """
        Run the notebook before saving it
        Source of information:
            http://nbconvert.readthedocs.io/en/latest/execute_api.html
        """
        self.processor.preprocess(self.nb, self.processing_options)

    def save_notebook(self):
        """
        Save the notebook on the hard drive
        """
        with open(self.outfilename, 'w') as f:
            nbf.write(self.nb, f)


def main():

    pass


if __name__ == "__main__":
    main()
