# Wine quality predictor data pipe
# author: Vignesh Rajakumar (group 14)
# date: 2020-12-1

all: doc/wine_quality_prediction_report.html

# download data
data/raw/winequality-red.csv data/raw/winequality-white.csv: src/download_data.py
	python src/download_data.py --url_1=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --url_2=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --out_file_1=data/raw/winequality-red.csv --out_file_2=data/raw/winequality-white.csv

# pre-process data
data/processed/test_set.csv data/processed/train_set.csv data/processed/wine_data.csv: src/wrangle.py data/raw/winequality-red.csv data/raw/winequality-white.csv
	python src/wrangle.py --input_r=data/raw/winequality-red.csv --input_w=data/raw/winequality-white.csv --out_dir=data/processed/

# create exploratory data analysis figure
results/eda_bin.png results/eda_corr.png results/eda_num.png results/eda_target.png: src/eda_wine.py data/processed/train_set.csv
	python src/eda_wine.py --datafile=data/processed/train_set.csv --out=results/

# tune and test model
results/hyperparameter_result.csv results/model_comparison.csv results/test_score.csv: src/ml_model.py data/processed/train_set.csv data/processed/test_set.csv
	python src/ml_model.py --path_1=data/processed/train_set.csv --path_2=data/processed/test_set.csv --out_dir=results/

# render final report
doc/wine_quality_prediction_report.html: doc/wine_quality_prediction_report.Rmd results/eda_target.png results/model_comparison.csv results/test_score.csv results/hyperparameter_result.csv
	Rscript -e "rmarkdown::render('doc/wine_quality_prediction_report.Rmd')"

clean:
	rm -rf data
	rm -rf results
	rm -rf doc/wine_quality_prediction_report.html