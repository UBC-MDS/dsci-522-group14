#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

"""Generate EDA plot images and tables for the wine quality analysis. This is based on the data at: https://archive.ics.uci.edu/ml/datasets/Wine+Quality.
Usage: eda_wine.py --data=<data-file> --out=<output-directory>

Options:
--data=<data-file>          path to data file
--out=<output_directory>    directory for saving plots
"""

from docopt import docopt

opt = docopt(__doc__)

def main(data, out):
    pass

if __name__ == '__main__':
    main(opt['--data'], opt['--out'])
    