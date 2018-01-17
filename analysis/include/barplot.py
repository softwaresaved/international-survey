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

try:
    from include.abstract_plot import abstractPlot
except ModuleNotFoundError:
    from abstract_plot import abstractPlot


class barPlot(abstractPlot):
    """
    Output a barplot with specific configuration
    """
    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)


    def create_plot(self):
        """
        """
        print(self.df)
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
