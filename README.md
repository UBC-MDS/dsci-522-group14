## Wine Quality Prediction
* contributors: Jianru Deng, Yuyan Guo, Vignesh Lakshmi Rajakumar, Cameron Harris 

Using machine learning to predict wine quality based on various physical and chemical properties of wine. 

### About

This analysis attempts to build a classification model using a publicly available [dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) containing physicochemical testing results of nearly 5000 wines and their wine quality as a score from 0-10. The goal of the project was to answer the following research question:

> Can we predict if a wine is "good" (6 out of 10) or "bad" ($\leq$ 5 out of 10) based on its physicochemical properties alone?

This prediction problem could have been framed as either a multi-class classification, binary classification or regression problem. During exploratory data analysis (EDA) the team found two observations that led us to simplify the problem into a binary classification one (i.e. good vs. bad wine). The first observation, which came from a distribution of the training target values, was that not all classes were well represented for the target values. The second observation was that the majority of wine quality scores were between 4-6. From this information, we decided that a multi-class classification approach would yield poor prediction results and provide little in value in identifying important features for determining wine quality. Whereas with a binary classification, we could better predict which types of chemical and physical characteristics can be attributed to good wines.

Next, we determined the point at which to split whether a wine is considered good or bad. This was done with the goal of minimizing the amount of class imbalance in the test data. A split at 5.5 (i.e. 6 or higher is good, 5 or lower is bad) was determined to be the best option and led to a 60/40 class split of good/bad wines respectively. 

Feature-target relationships were also plotted during EDA to see if any features stood out as good indicators of wine quality. The most prevelant feature at indicating quality appeared to be alcohol content. Further discussion of the EDA can be found [here](https://github.com/UBC-MDS/dsci-522-group14/blob/main/src/wine_quality_eda.ipynb). 

The data is presented as separate tables for red and white wine, we elected to combine the data into one dataset and see if the type of wine influences the rating. The resulting table contains 12 features (11 numeric and 1 binary categorical). For modelling, the numeric features will be scaled using sci-kit-learn's StandardScalar() transformer. While the categorical feature will be transformed to a binary one using OneHotEncoding(). Given the nature of the classification problem, the following models will be evaluated and scored to determine their appropriateness in prediction:
- DummyClassifier
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

How to run script to download data (Yuyan to update)

### Dependencies

(Yuyan to update)
- Python 3.8.5 and Python packages:
    - docopt=0.6.2
    - requests=2.22.0
    - pandas=0.25.1R
    - feather-format=0.4.0
    - etc. 

## References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.


