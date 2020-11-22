## Wine Quality Prediction
* contributors: Jianru Deng, Yuyan Guo, Vignesh Lakshmi Rajakumar, Cameron Harris 

Using machine learning to predict wine quality based on various physical and chemical properties of wine. 

### About

This analysis attempts to build a classification model using a publicly available [dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) containing physicochemical testing results of nearly 5000 wines and their wine quality as a score from 0-10. The goal of the project was to answer the following research question:

> Can we predict if a wine is "good" (6 or higher out of 10) or "bad" (5 or lower out of 10) based on its physicochemical properties alone?

Based on the main purpose of this project, this prediction problem has been framed as a binary classification problem. During exploratory data analysis (EDA) the team found two observations that led us to prefer using the datasets to identify the quality of the wines as two groups(i.e. good vs. bad wine)instead of multiple groups. The first observation, which came from a distribution of the training target values, was that not all classes were well represented for the target values. The second observation was that the majority of wine quality scores were between 4-6. From this information, we decided that a multi-class classification problem might yield unnecessary poor prediction results and provide little in value in identifying important features for determining wine quality. Whereas with a binary classification, we might get better preditions and better predict which types of chemical and physical characteristics can be attributed to good wines in general.

Next, we determined the point at which to split whether a wine is considered good or bad. This was done with the goal of minimizing the amount of class imbalance in the dataset as well as considering the rating in reality. A split at 5.5 (i.e. 6 or higher is good, 5 or lower is bad) was determined to be the resonable option from both perspectives and led to a 60/40 class split of good/bad wines respectively. 

Feature-target relationships were also plotted during EDA to see if any features stood out as potentially good indicators of wine quality. The most prevelant feature at indicating quality appeared to be alcohol content. Further discussion of the EDA can be found [here](https://github.com/UBC-MDS/dsci-522-group14/blob/main/src/wine_quality_eda.ipynb). 

The data is presented as separate tables for red and white wine, we elected to combine the data into one dataset and see if the type of wine influences the rating. The resulting table contains 12 features (11 numeric and 1 binary categorical). For modelling, the numeric features will be scaled using sci-kit-learn's StandardScalar() transformer. While the categorical feature will be transformed to a binary one using OneHotEncoding(). Given the nature of the classification problem, the following models will be evaluated and scored to determine their appropriateness in prediction:
- DummyClassifier (baseline)
- SVM with RBF Kernel
- Naive Bayes
- kNN
- Logistic Regression
- Random Forest

The results of this analysis will be presented in a report outlining the prediction accuracy of various models (as a table) and discussion of which features are important for this prediction task (e.g. Logistic Regression coefficients). Stay tuned. 

This Data Set was created by P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009. It was sourced from the UCI Machine Learning Repository (Dua and Graff 2017). Due to privacy reasons, only the physicochemical properties have been included and information about the company, grape type, price, etc. are left out. 

### Exploratory Data Analysis (EDA)

The results of EDA can be found [here](https://github.com/UBC-MDS/dsci-522-group14/blob/main/src/wine_quality_eda.ipynb).

### Usage

To replicate the analysis, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
command at the command line/terminal from the root directory of this
project to download the data:

```
python src/download_data.py --url_1=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --url_2=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --out_file_1=data/winequality-red.csv --out_file_2=data/winequality-white.csv
```

### Dependencies

- Python 3.8.3 and Python packages:
    - docopt==0.6.2
    - requests==2.24.0
    - pandas==1.1.3
    - scikit-learn==0.23.2
    - altair==4.1.0
    - matplotlib==3.3.3
    - numpy==1.19.2
    - ipython==7.19.0
    - altair_saver==0.5.0
    - ipykernel==5.3.4
    
## License

The DSCI-522-Group-14 materials here are licensed under the MIT License Copyright (c) 2020 DSCI-522-Group-14. If re-using/re-mixing please provide attribution and link to this webpage.


## References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.


