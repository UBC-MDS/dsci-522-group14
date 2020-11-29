## Wine Quality Prediction
* contributors: Jianru Deng, Yuyan Guo, Vignesh Lakshmi Rajakumar, Cameron Harris 

Using machine learning to predict wine quality based on various physical and chemical properties of wine. 

### About

This analysis attempts to build a classification model using a publicly available [dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) containing physicochemical testing results of nearly 5000 wines and their wine quality as a score from 0-10. The wine quality scores were determined by human wine taste preference (median of at least 3 evaluations made by wine experts). Each expert graded the wine quality between 0 (very bad) and 10 (very excellent). The features (physicochemical properties) were determined by analytical tests. A list of the features with a simple description of each is shown below:

1. **fixed acidity:** Sometimes referred to as titratable acidity, a measurement of the total concentration of titratable acids and free hydrogen ions present in wine. Import for the balance, colour and taste of wines.  
2. **volatile acidity:** Acids that are not measurable through titration (requires a steaming process) and generally created during the fermentation process. The most common volatile acids are acedic and lactic, further information on acidity can be found [here](http://winemakersacademy.com/understanding-wine-acidity/). 
3. **citric acid:** Common addition to wines to boost acidity levels, especially used in commerically produced wines following the fermentation process. 
4. **residual sugar:** Amount of sugar remaining after fermentation, which impacts the sweetness (or dryness) of the wine. 
5. **chlorides:** Measure of the amount of salt in a wine, which has a direct impact on taste.
6. **free sulfur dioxide (SO2):** SO2 is commonly added to wines to prevent bacterial growth and slow the oxidation process. The free SO2 is the portion that is not bound to other molecules.  
7. **total sulfur dioxide:** Total SO2 in wine (free + bound).
8. **density:** Density of wine measured as specific gravity. 
9. **pH:** Acidity level of the wine measured on the pH scale (lower = more acidic).
10. **sulphates:** Salt form of SO2 added to wines to prevent bacterial growth and slow the oxidation process. 
11. **alcohol:** Percentage of alcohol in wine measured by percent volume. 
12. **type:** Type of wine, for this data set red or white.

The goal of the project was to answer the following research question:

> Can we predict if a wine is "good" (6 or higher out of 10) or "bad" (5 or lower out of 10) based on its physicochemical properties alone?

* It is important to note that the labels "good" and "bad" are purely for classification and were selected by the relative wine quality scores determined by wine experts and the quality boundary identified during the exploratory data analysis (EDA). 

This prediction problem could have been framed as either a multi-class classification, binary classification or regression problem. During EDA, the team found two observations that led us to simplify the problem into a binary classification one (i.e. good vs. bad wine). The first observation, which came from a distribution of the training target values, was that not all classes were well represented for the target values. The second observation was that the majority of wine quality scores were between 4-6. From this information, we decided that a multi-class classification approach would yield poor prediction results and provide little in value in identifying important features for determining wine quality. Whereas with a binary classification, we could better predict which types of chemical and physical characteristics can be attributed to good wines.

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

``` bash
# download data
python src/download_data.py --url_1=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --url_2=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --out_file_1=data/raw/winequality-red.csv --out_file_2=data/raw/winequality-white.csv

# pre-process data
python src/pre_process.py --input_r=data/raw/winequality-red.csv --input_w=data/raw/winequality-white.csv --out_dir=data/processed/

# create exploratory data analysis figure
python src/eda_wine.py --datafile=data/processed/train_set.csv --out=results/

# tune and test model
python src/ml_model --path_1=data/processed/train_set.csv --path_2=data/processed/test_set.csv --out_dir=results/

# render final report
Rscript -e "rmarkdown::render('src/winequality_prediction_report.Rmd', output_format='github_document')"
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
    - selenium==3.141.0
    - python-chromedriver-binary==87.0.4280.20.0
    
## License

The DSCI-522-Group-14 materials here are licensed under the MIT License Copyright (c) 2020 DSCI-522-Group-14. If re-using/re-mixing please provide attribution and link to this webpage.


## References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.


