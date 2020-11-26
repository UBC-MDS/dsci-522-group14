# author: Jianru Deng 
# date: 2020-11-26


"""Cleans, splits and pre-processes (scales) 
   Usage: src/pre_process.py --input=<input> --out_dir=<out_dir>
   Options:
    --input=<input>       Path to raw data, filename should be included
    --out_dir=<out_dir>   Local file path to folder in which the processed data csvs will be written
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import QuantileTransformer, OneHotEncoder
from sklearn.compose import ColumnTransformer
import os
from docopt import docopt

opt = docopt(__doc__)

def main(input_data, out_dir):
    # Check the out_dir
    if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Read the data from the raw data
raw_data = pd.read_csv(input_data)

# Split the data
training, test = train_test_split(raw_data, test_size=0.2, random_state=522)

# Save the data
training.to_csv(out_dir + "/training_for_eda.csv", index=False)



def test_input(input):
    assert input.endswith(".csv"), "Input should be .csv file, please check your input!"

test_input(opt["--input"])

if __name__ == "__main__":
    main(opt["--input"], opt["--out_dir"])