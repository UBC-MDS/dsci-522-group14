# author: Yuyan Guo in Group 14
# date: 2020-11-28

"""Carrying out the machine learning analysis pipeline.

Usage: src/download_data.py --path_1=<path_1> --path_2=<path_2> --out_dir=<out_dir>
 
Options:
--path_1=<path_1>           Path of the training set
--path_2=<path_2>           Path of the test set
--out_dir=<out_dir>         Path of the directory (including "/" at the end") to save the results
"""

# Import libraries
import os
from docopt import docopt
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    cross_validate,
    train_test_split,
)

opt = docopt(__doc__)

def main(path_1, path_2, out_dir):
  # Read the data and split the data
  train_df = pd.read_csv(path_1)
  test_df = pd.read_csv(path_2)
  X_train, y_train = train_df.drop(["target"], axis=1), train_df["target"]
  X_test, y_test = test_df.drop(["target"], axis=1), test_df["target"]

  # Indentify feature types and define the transformations
  numeric_features = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", 
                    "density", "pH", "sulphates", "alcohol"]
  binary_features = ["type"]
  numeric_transformer = make_pipeline(StandardScaler())
  binary_transformer = make_pipeline(OneHotEncoder(drop='if_binary', dtype=int))
  preprocessor = ColumnTransformer(
      transformers=[
          ("num", numeric_transformer, numeric_features),      
          ("binary", binary_transformer, binary_features),
      ])
      
  # Use DummyClassifier as baseline and store the results
  results_dict = {}
  dummy = DummyClassifier(strategy = "most_frequent")
  dummy_score = cross_validate(dummy, X_train, y_train, return_train_score=True)
  store_cross_val_results("DummyClassifier", dummy_score, results_dict)
  
  # Comparing different classifiers and store the results
  models = {
      "Decision Tree": DecisionTreeClassifier(random_state=123),
      "RBF SVM": SVC(random_state=123),
      "Logistic Regression": LogisticRegression(max_iter=2000, random_state=123),
      "Random Forest": RandomForestClassifier(random_state=123)
  }

  for model, classifier in models.items():
      pip = make_pipeline(preprocessor, classifier)
      scores = cross_validate(pip, X_train, y_train, n_jobs=-1, return_train_score=True)
      store_cross_val_results(model, scores, results_dict)
  model_comparison = pd.DataFrame(results_dict).T
    
  # Pick the Random Forest as our model and carry out the hyperparameter optimization using RandomizedSearchCV
  rf_pipeline = make_pipeline(
      preprocessor, RandomForestClassifier(random_state=123)
  )

  param_dist = {
      "randomforestclassifier__n_estimators": list(range(50,200)),
      "randomforestclassifier__max_depth": list(range(2,20)),
  }

  random_search = RandomizedSearchCV(rf_pipeline, param_distributions=param_dist, n_jobs=-1, n_iter=30, random_state=123)
  random_search.fit(X_train, y_train)
  hyperpara_result = pd.DataFrame(random_search.cv_results_).sort_values('rank_test_score').head()[["param_randomforestclassifier__max_depth", 
                                                                                    "param_randomforestclassifier__n_estimators",
                                                                                    "mean_test_score",
                                                                                    "std_test_score", 
                                                                                    "rank_test_score"]]
                                                                                    
  # Based on the result of RandomizedSearchCV, using the model with best hyperparamters on test set
  best_n = random_search.best_params_['randomforestclassifier__n_estimators']
  best_depth = random_search.best_params_['randomforestclassifier__max_depth']

  rf_pipeline = make_pipeline(
      preprocessor, RandomForestClassifier(random_state=123, n_estimators=best_n, 
                                         max_depth=best_depth))
  rf_pipeline.fit(X_train, y_train)
  test_score = rf_pipeline.score(X_test, y_test)

  summary = {"Test score": [test_score]}
  test_score = pd.DataFrame(data = summary)
  
  # Export the test results as csv files
  model_comparison.to_csv(out_dir + "model_comparison.csv", index=False)
  hyperpara_result.to_csv(out_dir + "hyperparameter_result.csv", index=False)
  test_score.to_csv(out_dir + "test_score.csv", index=False)
  
# Define the helper function to store the cross-validation results for the model
def store_cross_val_results(model_name, scores, results_dict):
    """
    Stores mean scores from cross_validate in results_dict for
    the given model model_name.

    Parameters
    ----------
    model_name :
        scikit-learn classification model
    scores : dict
        object return by `cross_validate`
    results_dict: dict
        dictionary to store results

    Returns
    ----------
        None

    """
    results_dict[model_name] = {
        "mean_train_accuracy": "{:0.4f}".format(np.mean(scores["train_score"])),
        "mean_valid_accuracy": "{:0.4f}".format(np.mean(scores["test_score"])),
        "mean_fit_time (s)": "{:0.4f}".format(np.mean(scores["fit_time"])),
        "mean_score_time (s)": "{:0.4f}".format(np.mean(scores["score_time"])),
        "std_train_score": "{:0.4f}".format(scores["train_score"].std()),
        "std_valid_score": "{:0.4f}".format(scores["test_score"].std()),
    }
    
if __name__ == "__main__":
    main(opt["--path_1"], opt["--path_2"], opt["--out_dir"])
