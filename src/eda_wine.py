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
import sys

from selenium import webdriver
from altair_saver import save
import chromedriver_binary

# Handle large data sets without embedding them in the notebook
alt.data_transformers.enable('data_server')

opt = docopt(__doc__)

def main(datafile, out):
    # Load the train data
    train_df = pd.read_csv(datafile)

    # Target plot
    target_plot = draw_target_plot(train_df)
    save_plot(target_plot, out, "target")

    # Numeric columns plot
    num_plot = draw_numeric_plot(train_df)
    save_plot(num_plot, out, "num")

    # Binary column plot
    bin_plot = draw_binary_plot(train_df)
    save_plot(bin_plot, out, "bin")

    # Correlation plot
    corr_plot = draw_corr_plot(train_df)
    save_plot(corr_plot, out, "corr")
    

def draw_numeric_plot(train_df):
    """draw numeric plot

    Args:
        train_df (pd.DataFrame): train data split as a pandas dataframe

    Returns:
        alt.RepeatChart: plot object of numeric plot, repeated for each numeric column
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
    bin_plot = alt.Chart(train_df, title='Target distribution for each wine type').mark_bar().encode(
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
    num_cols = list(train_df.select_dtypes(include=np.number).iloc[:,1:].columns)
    corr_df = train_df[num_cols].corr(method='spearman').stack().reset_index(name='corr')

    corr_plot = alt.Chart(corr_df, title='Correlation Matrix').mark_rect().encode(
        alt.X('level_0', title=''),
        alt.Y('level_1', title=''),
        color=alt.Color('corr', scale=alt.Scale(domain=(-1, 1), scheme='purpleorange')),
        tooltip='corr'
    ).properties(
        height=400,
        width=400
    )

    return corr_plot

def draw_target_plot(train_df):
    """draw bar chart for target distribution

    Args:
        train_df (pd.DataFrame): train data split as pandas dataframe

    Returns:
        alt.Chart: plot object of target plot
    """
    target_plot = alt.Chart(train_df, title='Target distribution').mark_bar().encode(
        x='good_wine',
        y='count()'
    )

    return target_plot

def save_plot(plot, out, plot_name):
    """save the plot object

    Args:
        plot (alt.Chart): plot bject to save
        out (string): output directory
        plot_name (string): name of the plot to be inlcluded in the filename
    """
    file_name = f'{out}/eda_{plot_name}.png'
    driver = webdriver.Chrome()
    save(plot, file_name, method='selenium', webdriver=driver)

# Tests
assert_df = pd.DataFrame(
    {'fixed acidity': [8.4], 
    'volatile acidity': [0.18], 
    'citric acid': [0.42], 
    'residual sugar': [5.1], 
    'chlorides': [0.036000000000000004], 
    'free sulfur dioxide': [7.0], 
    'total sulfur dioxide': [77.0], 
    'density': [0.9939], 
    'pH': [3.16], 
    'sulphates': [0.52], 
    'alcohol': [11.7], 
    'type': ['white'], 
    'good_wine': [False]}
)

assert isinstance(draw_numeric_plot(assert_df), alt.RepeatChart)
assert isinstance(draw_binary_plot(assert_df), alt.Chart)
assert isinstance(draw_corr_plot(assert_df), alt.Chart)
assert isinstance(draw_target_plot(assert_df), alt.Chart)

if __name__ == '__main__':
    main(opt['--datafile'], opt['--out'])
