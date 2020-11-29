# author: Jianru Deng 
# date: 2020-11-26


"""This script takes in 2 .csv files of red and white wines,
    cleans the data,
    merges two files into one,
    regroups the 'quality' to make as 'target',
    creates a new feature as 'type',
    and writes the cleaned full data, splited data into the specified directory


   Usage: src/wrangle.py --input_r=<input_r> --input_w=<input_w> --out_dir=<out_dir>
   
   
   Options:
    --input_r=<input_r>     Path to raw data of red wine, filename should be included
    --input_w=<input_w>     Path to raw data of white wine, filename should be included
    --out_dir=<out_dir>     Local file path to folder in which the processed data csvs will be written
"""

# example: 

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from docopt import docopt


opt = docopt(__doc__)

def main(input_r, input_w, out_dir):
    # Check the out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Read the data from the raw data
    red_df = pd.read_csv(input_r, sep = ',')
    white_df = pd.read_csv(input_w, sep = ',')
    
    # Merge the two datasets and add a feature as 'type' for wine type
    red_df['type'] = 'red'
    white_df['type'] = 'white'
    
    wine_df = pd.concat([red_df, white_df], ignore_index = True) 
    
    # Group the 'quality' feature into two and make it as a 'target' 
    wine_df['target'] = wine_df['quality']
    wine_df.loc[wine_df.quality >5, 'target'] = 'good'
    wine_df.loc[wine_df.quality <=5, 'target'] = 'bad'
    wine_df.drop(columns=['quality'], inplace=True)
    
    wine_df.to_csv(out_dir + '/wine_data.csv', index = False)
        
    # Split the data
    train, test = train_test_split(wine_df, test_size=0.2, random_state=2020)
    
    # Save the data
    train.to_csv(out_dir + "/train_set.csv", index=False)
    test.to_csv(out_dir + "/test_set.csv", index = False)


# Tests that the file paths exist
def check_paths():
  if (os.path.exists(opt["--input_r"])) and (os.path.exists(opt["--input_w"])):
    pass
  else:
    raise ValueError('At least one of the file you want to combine cannot be found')
  
check_paths()

# Test that the input files are csv type

def test_input(input1,input2, out_dir):
    assert input1.endswith(".csv"), "Hi please only give me .csv file only, yours is not."
    assert input2.endswith(".csv"), "Hi please only give me .csv file only, yours is not."
    
    
    
test_input(opt["--input_r"], opt["--input_w"], opt["--out_dir"])



if __name__ == "__main__":
    main(opt["--input_r"], opt["--input_w"], opt["--out_dir"])
