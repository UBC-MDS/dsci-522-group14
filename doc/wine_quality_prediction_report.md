Predicting Wine Quality Using Physicochemical Properties
================
Contributors: Jianru Deng, Yuyan Guo, Vignesh Lakshmi Rajakumar, Cameron
Harris

  - [Acknowledgements](#acknowledgements)
  - [Data Summary](#data-summary)
  - [Preprocessing of Features](#preprocessing-of-features)
  - [Modelling and Cross Validation
    Scores](#modelling-and-cross-validation-scores)
  - [Hyperparameter Optimization](#hyperparameter-optimization)
  - [Test Data Scores and
    Conclusions](#test-data-scores-and-conclusions)
  - [References](#references)

## Acknowledgements

The data set was produced by P. Cortez, A. Cerdeira, F. Almeida, T.
Matos and J. Reis. Modeling wine preferences by data mining from
physicochemical properties. In Decision Support Systems, Elsevier,
47(4):547-553, 2009. It was sourced from Dua, D. and Graff, C. (2019).
UCI Machine Learning Repository \[<http://archive.ics.uci.edu/ml>\].
Irvine, CA: University of California, School of Information and Computer
Science.

All machine learning processing and analysis was done using Sci-kit
Learn (Pedregosa et al. (2011)). Tables and figures in this report were
created with the help of the Knitr (Xie (2014)) package. File paths were
managed using the Here (Müller (2020)) package.

## Data Summary

The [dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) used
for this prediction task contains physicochemical properties (features)
of nearly 5000 wines and their wine quality as a score from 0-10
(targets). The wine quality scores were determined by human wine taste
preference (median of at least 3 evaluations made by wine experts). Each
expert graded the wine quality between 0 (very bad) and 10 (very
excellent). The features (physicochemical properties) were determined by
analytic tests. Overall there were eleven numeric features and one
categorical feature (see
[README.md](https://github.com/UBC-MDS/dsci-522-group14/blob/main/README.md)
file for more details on features).

The goal of the project was to answer the following research question:

> Can we predict if a wine is “good” (6 or higher out of 10) or “bad” (5
> or lower out of 10) based on its physicochemical properties alone?

It is important to note that the labels “good” and “bad” are purely for
classification and were selected by the relative wine quality scores
determined by wine experts and the quality boundary identified during
the exploratory data analysis (EDA).

This prediction problem could have been framed as either a multi-class
classification, binary classification or regression problem. During EDA,
the team found two observations that led us to simplify the problem into
a binary classification one (i.e. good vs. bad wine). The first
observation, which came from a distribution of the training target
values, was that not all classes were well represented for the target
values. The second observation was that the majority of wine quality
scores were between 4-6. From this information, we decided that a
multi-class classification approach would yield poor prediction results
and provide little in value in identifying important features for
determining wine quality. Whereas with a binary classification, we could
better predict which types of chemical and physical characteristics can
be attributed to good wines.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 1. Sample of processed data used for wine quality prediction

</caption>

<thead>

<tr>

<th style="text-align:right;">

fixed acidity

</th>

<th style="text-align:right;">

volatile acidity

</th>

<th style="text-align:right;">

citric acid

</th>

<th style="text-align:right;">

residual sugar

</th>

<th style="text-align:right;">

chlorides

</th>

<th style="text-align:right;">

free sulfur dioxide

</th>

<th style="text-align:right;">

total sulfur dioxide

</th>

<th style="text-align:right;">

density

</th>

<th style="text-align:right;">

pH

</th>

<th style="text-align:right;">

sulphates

</th>

<th style="text-align:right;">

alcohol

</th>

<th style="text-align:left;">

type

</th>

<th style="text-align:left;">

target

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:right;">

7.4

</td>

<td style="text-align:right;">

0.70

</td>

<td style="text-align:right;">

0.00

</td>

<td style="text-align:right;">

1.9

</td>

<td style="text-align:right;">

0.076

</td>

<td style="text-align:right;">

11

</td>

<td style="text-align:right;">

34

</td>

<td style="text-align:right;">

0.9978

</td>

<td style="text-align:right;">

3.51

</td>

<td style="text-align:right;">

0.56

</td>

<td style="text-align:right;">

9.4

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

<tr>

<td style="text-align:right;">

7.8

</td>

<td style="text-align:right;">

0.88

</td>

<td style="text-align:right;">

0.00

</td>

<td style="text-align:right;">

2.6

</td>

<td style="text-align:right;">

0.098

</td>

<td style="text-align:right;">

25

</td>

<td style="text-align:right;">

67

</td>

<td style="text-align:right;">

0.9968

</td>

<td style="text-align:right;">

3.20

</td>

<td style="text-align:right;">

0.68

</td>

<td style="text-align:right;">

9.8

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

<tr>

<td style="text-align:right;">

7.8

</td>

<td style="text-align:right;">

0.76

</td>

<td style="text-align:right;">

0.04

</td>

<td style="text-align:right;">

2.3

</td>

<td style="text-align:right;">

0.092

</td>

<td style="text-align:right;">

15

</td>

<td style="text-align:right;">

54

</td>

<td style="text-align:right;">

0.9970

</td>

<td style="text-align:right;">

3.26

</td>

<td style="text-align:right;">

0.65

</td>

<td style="text-align:right;">

9.8

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

<tr>

<td style="text-align:right;">

11.2

</td>

<td style="text-align:right;">

0.28

</td>

<td style="text-align:right;">

0.56

</td>

<td style="text-align:right;">

1.9

</td>

<td style="text-align:right;">

0.075

</td>

<td style="text-align:right;">

17

</td>

<td style="text-align:right;">

60

</td>

<td style="text-align:right;">

0.9980

</td>

<td style="text-align:right;">

3.16

</td>

<td style="text-align:right;">

0.58

</td>

<td style="text-align:right;">

9.8

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

good

</td>

</tr>

<tr>

<td style="text-align:right;">

7.4

</td>

<td style="text-align:right;">

0.70

</td>

<td style="text-align:right;">

0.00

</td>

<td style="text-align:right;">

1.9

</td>

<td style="text-align:right;">

0.076

</td>

<td style="text-align:right;">

11

</td>

<td style="text-align:right;">

34

</td>

<td style="text-align:right;">

0.9978

</td>

<td style="text-align:right;">

3.51

</td>

<td style="text-align:right;">

0.56

</td>

<td style="text-align:right;">

9.4

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

<tr>

<td style="text-align:right;">

7.4

</td>

<td style="text-align:right;">

0.66

</td>

<td style="text-align:right;">

0.00

</td>

<td style="text-align:right;">

1.8

</td>

<td style="text-align:right;">

0.075

</td>

<td style="text-align:right;">

13

</td>

<td style="text-align:right;">

40

</td>

<td style="text-align:right;">

0.9978

</td>

<td style="text-align:right;">

3.51

</td>

<td style="text-align:right;">

0.56

</td>

<td style="text-align:right;">

9.4

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

<tr>

<td style="text-align:right;">

7.9

</td>

<td style="text-align:right;">

0.60

</td>

<td style="text-align:right;">

0.06

</td>

<td style="text-align:right;">

1.6

</td>

<td style="text-align:right;">

0.069

</td>

<td style="text-align:right;">

15

</td>

<td style="text-align:right;">

59

</td>

<td style="text-align:right;">

0.9964

</td>

<td style="text-align:right;">

3.30

</td>

<td style="text-align:right;">

0.46

</td>

<td style="text-align:right;">

9.4

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

<tr>

<td style="text-align:right;">

7.3

</td>

<td style="text-align:right;">

0.65

</td>

<td style="text-align:right;">

0.00

</td>

<td style="text-align:right;">

1.2

</td>

<td style="text-align:right;">

0.065

</td>

<td style="text-align:right;">

15

</td>

<td style="text-align:right;">

21

</td>

<td style="text-align:right;">

0.9946

</td>

<td style="text-align:right;">

3.39

</td>

<td style="text-align:right;">

0.47

</td>

<td style="text-align:right;">

10.0

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

good

</td>

</tr>

<tr>

<td style="text-align:right;">

7.8

</td>

<td style="text-align:right;">

0.58

</td>

<td style="text-align:right;">

0.02

</td>

<td style="text-align:right;">

2.0

</td>

<td style="text-align:right;">

0.073

</td>

<td style="text-align:right;">

9

</td>

<td style="text-align:right;">

18

</td>

<td style="text-align:right;">

0.9968

</td>

<td style="text-align:right;">

3.36

</td>

<td style="text-align:right;">

0.57

</td>

<td style="text-align:right;">

9.5

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

good

</td>

</tr>

<tr>

<td style="text-align:right;">

7.5

</td>

<td style="text-align:right;">

0.50

</td>

<td style="text-align:right;">

0.36

</td>

<td style="text-align:right;">

6.1

</td>

<td style="text-align:right;">

0.071

</td>

<td style="text-align:right;">

17

</td>

<td style="text-align:right;">

102

</td>

<td style="text-align:right;">

0.9978

</td>

<td style="text-align:right;">

3.35

</td>

<td style="text-align:right;">

0.80

</td>

<td style="text-align:right;">

10.5

</td>

<td style="text-align:left;">

red

</td>

<td style="text-align:left;">

bad

</td>

</tr>

</tbody>

</table>

Next we analyze the target classes for this data set in the figure
below.

<div class="figure" style="text-align: center">

<img src="C:/Users/vignesh/career/dsci-522-group14/results/eda_target.png" alt="Figure 1. Target Class Distribution" width="15%" />

<p class="caption">

Figure 1. Target Class Distribution

</p>

</div>

For this classification problem we determined that we could ignore class
imbalance related intricacies and could begin splitting the data into
train and test sets. For this task, an 80/20 train/test split was used.

## Preprocessing of Features

As mentioned, there were eleven numeric features and one categorical
feature. For this analysis, the eleven numeric features were scaled
using a standard scalar, which involves removing the mean and scaling to
unit variance (Pedregosa et al. (2011)). The categorical feature, wine
type, only contained two values (red and white) so it was treated as a
binary feature.

## Modelling and Cross Validation Scores

All models were evaluated through five-fold cross validation on the
training data set. Accuracy was used as the primary metric to evaluate
model performance. For this classification problem, there is low
consequence to a false negative or false positive classifications,
therefore recall and precision are of low importance to us. Accuracy
provides a simple, clear way to compare model performance.

\[ \text{Accuracy} = \frac{\text{Number of correct predictions}}{\text{Number of examples}} \]
The following models were evaluated to predict the wine quality label:

  - Dummy classifier
  - Decision tree
  - RBF SVM: SVC
  - Logistic Regression
  - Random Forest

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 2. Cross validation scores for models using training dataset

</caption>

<thead>

<tr>

<th style="text-align:left;">

model

</th>

<th style="text-align:right;">

mean\_train\_accuracy

</th>

<th style="text-align:right;">

mean\_valid\_accuracy

</th>

<th style="text-align:right;">

mean\_fit\_time (s)

</th>

<th style="text-align:right;">

mean\_score\_time (s)

</th>

<th style="text-align:right;">

std\_train\_score

</th>

<th style="text-align:right;">

std\_valid\_score

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

DummyClassifier

</td>

<td style="text-align:right;">

0.6336

</td>

<td style="text-align:right;">

0.6336

</td>

<td style="text-align:right;">

0.0034

</td>

<td style="text-align:right;">

0.0014

</td>

<td style="text-align:right;">

0.0001

</td>

<td style="text-align:right;">

0.0004

</td>

</tr>

<tr>

<td style="text-align:left;">

Decision Tree

</td>

<td style="text-align:right;">

1.0000

</td>

<td style="text-align:right;">

0.7535

</td>

<td style="text-align:right;">

0.0606

</td>

<td style="text-align:right;">

0.0088

</td>

<td style="text-align:right;">

0.0000

</td>

<td style="text-align:right;">

0.0268

</td>

</tr>

<tr>

<td style="text-align:left;">

RBF SVM

</td>

<td style="text-align:right;">

0.7943

</td>

<td style="text-align:right;">

0.7687

</td>

<td style="text-align:right;">

0.7542

</td>

<td style="text-align:right;">

0.0760

</td>

<td style="text-align:right;">

0.0048

</td>

<td style="text-align:right;">

0.0126

</td>

</tr>

<tr>

<td style="text-align:left;">

Logistic Regression

</td>

<td style="text-align:right;">

0.7360

</td>

<td style="text-align:right;">

0.7339

</td>

<td style="text-align:right;">

0.0396

</td>

<td style="text-align:right;">

0.0084

</td>

<td style="text-align:right;">

0.0029

</td>

<td style="text-align:right;">

0.0072

</td>

</tr>

<tr>

<td style="text-align:left;">

Random Forest

</td>

<td style="text-align:right;">

1.0000

</td>

<td style="text-align:right;">

0.8197

</td>

<td style="text-align:right;">

0.8782

</td>

<td style="text-align:right;">

0.0382

</td>

<td style="text-align:right;">

0.0000

</td>

<td style="text-align:right;">

0.0104

</td>

</tr>

</tbody>

</table>

The results in Table 2 show that the Random Forest classified the wine
quality with the highest accuracy on the training data with a validation
score of 0.82. This was not surprising to our team as Random Forest is
one of the most widely used and powerful model for classification
problems.

The SVC with RBF SVM model performed the next best with a validation
score of 0.769.

## Hyperparameter Optimization

Given the cross validation results above, hyperparameter optimization
was carried out on our Random Forest model on the number of trees and
maximum tree depth parameters.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 3. Hyperparameter optimization results

</caption>

<thead>

<tr>

<th style="text-align:right;">

param\_randomforestclassifier\_\_max\_depth

</th>

<th style="text-align:right;">

param\_randomforestclassifier\_\_n\_estimators

</th>

<th style="text-align:right;">

mean\_test\_score

</th>

<th style="text-align:right;">

std\_test\_score

</th>

<th style="text-align:right;">

rank\_test\_score

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:right;">

17

</td>

<td style="text-align:right;">

173

</td>

<td style="text-align:right;">

0.8220093

</td>

<td style="text-align:right;">

0.0131897

</td>

<td style="text-align:right;">

1

</td>

</tr>

<tr>

<td style="text-align:right;">

17

</td>

<td style="text-align:right;">

156

</td>

<td style="text-align:right;">

0.8218170

</td>

<td style="text-align:right;">

0.0124447

</td>

<td style="text-align:right;">

2

</td>

</tr>

<tr>

<td style="text-align:right;">

15

</td>

<td style="text-align:right;">

115

</td>

<td style="text-align:right;">

0.8208538

</td>

<td style="text-align:right;">

0.0106696

</td>

<td style="text-align:right;">

3

</td>

</tr>

<tr>

<td style="text-align:right;">

19

</td>

<td style="text-align:right;">

121

</td>

<td style="text-align:right;">

0.8204707

</td>

<td style="text-align:right;">

0.0104500

</td>

<td style="text-align:right;">

4

</td>

</tr>

<tr>

<td style="text-align:right;">

16

</td>

<td style="text-align:right;">

89

</td>

<td style="text-align:right;">

0.8197000

</td>

<td style="text-align:right;">

0.0121985

</td>

<td style="text-align:right;">

5

</td>

</tr>

</tbody>

</table>

The results of optimization two key hyperparameters resulted in slightly
improved validation results (note that in Table 3, “test score” is
comparable to “valid score” from Table 2).

## Test Data Scores and Conclusions

Finally, with a Random Forest model containing optimized
hyperparameters, we were able to test the accuracy of our model on the
test data set.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 4. Random Forest scores on test data set

</caption>

<thead>

<tr>

<th style="text-align:right;">

test\_score

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:right;">

0.8476923

</td>

</tr>

</tbody>

</table>

With an optimized, Random Forest model, we were able to achieve an
accuracy of 0.848 on the test data set. This is slightly higher than the
validation scores using the training data, which tells us that we may
have got a bit lucky on the test data set. But overall, the model is
doing a decent job at predicting the wine label of “good” or “bad” given
the physicochemical properties as features.

If we recall the main research question:

> Can we predict if a wine is “good” (6 or higher out of 10) or “bad” (5
> or lower out of 10) based on its physicochemical properties alone?

The results show that with about 85% accuracy, it is possible to predict
whether a wine may be considered “good” (6/10 or higher) or “bad” (5/10
or lower).

Some further work that may result in higher prediction accuracy could
include feature selection optimization. For example, some of the
features seem like they could be correlated (e.g. free sulphur dioxide,
total sulphur dioxide, sulphates).

The original data-set has an quantitative output metric: a rating
between 0-10. This problem could be a candidate for a regression model.
It would be interesting to compare the effectiveness and usefulness of
this consideration and could be explored in a future iteration.

Another point of interest in problem is the subjectivity of wine
quality. The current data set uses a median rating from multiple
tastings from multiple wine experts as an estimation of quality. While
we feel that this estimate is a good enough proxy, it is something to be
aware of when using this model.

## References

<div id="refs" class="references">

<div id="ref-here">

Müller, Kirill. 2020. *Here: A Simpler Way to Find Your Files*.
<https://CRAN.R-project.org/package=here>.

</div>

<div id="ref-sk-learn">

Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O.
Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in
Python.” *Journal of Machine Learning Research* 12: 2825–30.

</div>

<div id="ref-knitr">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

</div>
