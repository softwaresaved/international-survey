#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Generate barplot
"""

import pandas as pd
import matplotlib.pyplot as plt
try:
    from include.likertScalePlot import get_colors
except ModuleNotFoundError:
    from likertScalePlot import get_colors
try:
    import include.common_plot
except ModuleNotFoundError:
    import common_plot


class barPlot:
    """
    Output a barplot with specific configuration
    """

    def __init__(self, *args, **kwargs):
        """
        """
        # get the data
        self.df = args[0]
        # set the k,v as attribute to the class
        self.__dict__.update(kwargs)
        self._create_figure()
        print(self.df)

    def _create_figure(self):
        """
        Create the matplotlib figure
        """
        self.fig, self.ax = plt.subplots()

    def create_plot(self):
        """
        """
        return self.fig, self.ax


def main():
    """
    """
    df = pd.read_csv('./../2017/uk/data/cleaned_data.csv')
    test_df = df['edu1. What is the highest qualification you have obtained?']
    barplot = barPlot(test_df)
    fig, ax = barplot.create_plot()

if __name__ == "__main__":
    main()
