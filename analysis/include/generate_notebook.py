#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
from include.config import NotebookConfig

__author__: "Olivier PHILIPPE"
__licence__: "BSD3-clause"

"""
Scrip to programatically generate notebook for exploratory analysis
Use the code from: https://gist.github.com/fperez/9716279
"""


class GenerateNotebook(NotebookConfig):
    """
    """

    def __init__(self, year, country, notebook_filename):
        """
        """
        super().__init__(year, country)
        self.outfilename = "results_{}".format(notebook_filename)
        # Generate an empty notebook
        self.nb = nbf.v4.new_notebook()
        # Get all the import from NotebookConfig
        self._import()
        # Set up some display options for pandas to extend
        # the limit of the row and columns that are displayed
        self._setup_display()
        # Hide the code when export in html
        self._hide_code_for_html()
        # Setup matplotlib magic and size of figures
        self._setup_matplotlib()
        # Load the dataset
        self._load_dataset()
        # Processor to run the notebook
        self.processor = ExecutePreprocessor(
            timeout=600, kernel_name="python3", allow_errors=self.allow_errors
        )

    def _import(self):
        """
        Import all the needed library
        """
        self.add_section("Importing modules")
        import_code = "\n".join(self.to_import)
        self._add_code(import_code)

    def _hide_code_for_html(self):
        """
        Hide the code cell when convert the notebook in
        html
        source:https://gist.github.com/masnick/d6a1af14812c0c4b3314
        """
        self._add_text("This text is used to hide the code cell when exported in html")
        code = """di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)"""
        self._add_code(code)

    def _setup_display(self):
        """
        Extending the limit of rows and columns
        displayed
        """
        rows = """pd.set_option('display.max_rows', 1000)"""
        columns = """pd.set_option('display.max_columns', 1000) """
        tables = """InteractiveShell.ast_node_interactivity = "all" """
        self._add_code("\n".join([rows, columns, tables]))

    def _setup_matplotlib(self):
        """
        Set up matplotlib for Jupyter
        """
        magic_inline = """get_ipython().magic('matplotlib inline')  # Activate that line to use in Jupyter """
        # svg_output = """%config InlineBackend.figure_format = 'svg'"""
        # Dependency of size of figure in the textCleaning.py. Carefull if changing these value
        # it will impact the quality of the wordcloud generated in textCleaning.py (need to change the width and height)
        size_figures = """matplotlib.rcParams['figure.figsize'] = (15.0, 8.0)"""
        self._add_code("\n".join([magic_inline, size_figures]))

    def _load_dataset(self):
        """
        """
        self._add_text("# Loading dataset")
        loading = """df =  pd.read_csv('{}')""".format(self.cleaned_df_location)
        self._add_code(loading)

    def output_total_participants(self):
        """
        Show the number of participant that have been filtered out
        """
        self._add_text(
            "The total of participant after cleaning the dataset. Remove all participants that have not completed the survey passed the first pages and all participants who are not from the country"
        )
        self._add_code("""len(df)""")

    def add_section(self, text):
        """
        """
        self._add_text("# Section: {}".format(text))

    def add_group(self, text):
        """
        """
        self._add_text("## Group of question: {}".format(text))

    def add_question_title(self, text):
        """
        """
        self._add_text("### {}".format(text))

    def add_count(self, *args):
        """
        """
        self.count = True
        count_count = """v_to_count, filename = get_count(df, {}, "{}", "{}", "{}", "{}")""".format(
            *args
        )
        # count_count = """v_to_count, filename = get_count(df, "{}")""".format(','.join(*args))
        self._add_code(count_count)

    def add_percentage(self):
        """
        """
        self.percent = True
        percentage_count = """perc_to_count = get_percentage(v_to_count, filename)"""
        self._add_code(percentage_count)

    def add_display_percentage(self):
        """
        """
        display = """display_side_by_side(perc_to_count, multiple=False) """
        self.percent = True
        self._add_code(display)

    def add_display_count(self):
        """
        """
        display = """display_side_by_side(v_to_count, multiple=False) """
        self.count = False
        self._add_code(display)

    def add_display_all(self):
        """
        """
        args = list()
        args_na = list()
        if self.count is True:
            args.append("v_to_count")
            args_na.append("v_na")
        if self.percent is True:
            args.append("perc_to_count")
            args_na.append("perc_na")
        self.percent, self.count = False, False
        display = """display_side_by_side({})""".format(",".join(args))
        # display_na = """display_side_by_side({})""".format(','.join(args_na))
        self._add_code(display)
        # self._add_code(display_na)

    def add_plot(self, *args):
        """
        """
        if (
            self.show_percent is True
            and args[0] != "likert"
            and args[0] != "freenumeric"
        ):
            plot = """_ = get_plot(perc_to_count, "{}")""".format(",".join(args))
        # elif args[0] == 'freetext':
        #     plot = """_ = get_plot(wc, "{}")""".format(','.join(args))
        else:
            plot = """_ = get_plot(v_to_count, "{}")""".format(",".join(args))
        self._add_code(plot)

    def add_wordcloud(self, column):
        """
        """
        word_cloud = """ wc = wordcloud(df, {})""".format(column)
        self._add_code(word_cloud)
        # plot = """_ = get_plot(v_to_count, "{}")""".format(','.join(args))
        plot = """ plt.imshow(wc, interpolation='bilinear')\n plt.axis("off")"""
        self._add_code(plot)

    def _add_text(self, *args):
        """
        """
        for text_to_add in args:
            formatting_text = nbf.v4.new_markdown_cell(text_to_add)
            self._append_notebook(formatting_text)

    def _add_code(self, *args):
        """
        """
        for code_to_add in args:
            formatting_code = nbf.v4.new_code_cell(code_to_add)
            self._append_notebook(formatting_code)

    def _append_notebook(self, cell_to_add):
        """
        """
        self.nb.setdefault("cells", []).append(cell_to_add)

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
        with open(self.outfilename, "w") as f:
            nbf.write(self.nb, f)


def main():

    pass


if __name__ == "__main__":
    main()
