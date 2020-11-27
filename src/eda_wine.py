#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

"""Generate EDA plot images and tables for the wine quality analysis. This is based on the data at: https://archive.ics.uci.edu/ml/datasets/Wine+Quality.
Usage: eda_wine.py --datafile=<datafile> --out=<output-directory>

Options:
--datafile=<datafile>          path to data file
--out=<output_directory>    directory for saving plots
"""

from docopt import docopt
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

opt = docopt(__doc__)

def main(datafile, out):
    # Load the train data
    train_df = pd.read_csv(data)

    # Target plot
    target_plot = draw_target_plot(train_df)
    save_plot(target_plot, out)

    # Numeric columns plot
    num_plot = draw_numeric_plot(train_df)
    save_plot(num_plot, out)

    # Binary column plot
    bin_plot = draw_binary_plot(train_df)
    save_plot(bin_plot, out)

    # Correlation plot
    corr_plot = draw_corr_plot(train_df)
    save_plot(corr_plot, out)
    

def draw_numeric_plot(train_df):
    """draw numeric plot

    Args:
        train_df (pd.DataFrame): train data split as a pandas dataframe

    Returns:
        alt.Chart: plot object of numeric plot
    """
    num_cols = list(train_df.select_dtypes(include=np.number).iloc[:,1:].columns)

    num_plot = alt.Chart(train_df).mark_area(
        opacity=0.5,
        interpolate='monotone'
    ).encode(
        alt.X(alt.repeat("repeat"), type='quantitative', scale=alt.Scale(zero=False), bin=alt.Bin(maxbins=100)),
        alt.Y('count()', stack=None),
        fill='good_wine'
    ).properties(
        height=200,
        width=200
    ).repeat(
        repeat=num_cols,
        columns = 4
    ).configure_axis(labels=False)

    return num_plot

def draw_binary_plot(train_df):
    """draw binary plot

    Args:
        train_df (pd.DataFrame): train data split as a pandas dataframe

    Returns:
        alt.Chart: plot object of binary plot
    """
    bin_plot = alt.Chart(train_df).mark_bar().encode(
        x='good_wine',
        y='count()',
        color='good_wine',
        column='type')

    return bin_plot


def draw_corr_plot(train_df):
    """draw correlation plot

    Args:
        train_df (pd.DataFrame): train data split as a pandas dataframe

    Returns:
        alt.Chart: plot object of correlation plot
    """
    corr_df = train_df[num_cols].corr(method='spearman').stack().reset_index(name='corr')

    corr_plot = alt.Chart(corr_df).mark_rect().encode(
        alt.X('level_0', title=''),
        alt.Y('level_1', title=''),
        color=alt.Color('corr', scale=alt.Scale(domain=(-1, 1), scheme='purpleorange')),
        tooltip='corr'
    ).properties(
        height=400,
        width=400
    )

    return corr_plot



if __name__ == '__main__':
    main(opt['--data'], opt['--out'])
