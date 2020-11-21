# author: Yuyan Guo in Group 14
# date: 2020-11-20

"""Downloads two csv data files using ";" as demiliters from the web to the same local directory.

Usage: src/download_data.py --url_1=<url_1> --url_2=<url_2> --out_file_1=<out_file_1> --out_file_2=<out_file_2>
 
Options:
--url_1=<url_1>             URL from where to download the first csv dataset (must be in standard csv format)
--url_2=<url_2>             URL from where to download the second csv dataset (must be in standard csv format)
--out_file_1=<out_file_1>   Path (including filename and must be the same directory as another path) of where to locally write the file corresonding to url_1
--out_file_2=<out_file_2>   Path (including filename and must be the same directory as another path) of where to locally write the file corresonding to url_2
"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

def main(url_1, url_2, out_file_1, out_file_2):
    data_1 = pd.read_csv(url_1, delimiter=";")
    data_2 = pd.read_csv(url_2, delimiter=";")
    try:
        data_1.to_csv(out_file_1, index=False)
        data_2.to_csv(out_file_2, index=False)
    except:
        os.makedirs(os.path.dirname(out_file_1))
        data_1.to_csv(out_file_1, index=False)
        data_2.to_csv(out_file_2, index=False)



if __name__ == "__main__":
    main(opt["--url_1"], opt["--url_2"], opt["--out_file_1"], opt["--out_file_2"])
