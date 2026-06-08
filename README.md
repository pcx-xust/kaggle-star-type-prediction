# Kaggle Star Type Prediction

## Project Overview

This project is based on the Kaggle Playground Series competition `playground-series-s6e6`.

The goal is to build a reproducible machine learning pipeline for predicting star type classes from tabular data.

## Problem Type

This is a supervised multi-class classification task.

## Dataset

The dataset contains:

- `train.csv`: training data with labels
- `test.csv`: test data without labels
- `sample_submission.csv`: Kaggle submission template

Raw data is not included in this repository. Please download it from Kaggle using the official API.

## Project Structure

```text
kaggle-star-type-prediction/
├── data/
│   ├── raw/                    # Raw Kaggle data files, ignored by Git
│   └── processed/              # Processed data files, ignored by Git
│
├── notebook/
│   ├── 01_eda.ipynb
│   ├── 02_baseline_model.ipynb
│   ├── 03_color_feature_model.ipynb
│   ├── 04_model_selection.ipynb
│   ├── 05_submission.ipynb
│   ├── 06_lgbm_model.ipynb
│   └── 07_lgbm_cv_tuning.ipynb
│
├── reports/
│   ├── eda/                    # EDA reports, figures, and summary tables
│   └── model/
│       ├── baseline/           # Dummy, RandomForest, and ExtraTrees results
│       ├── color_features/     # Color feature engineering results
│       ├── lgbm/               # LightGBM validation results
│       ├── lgbm_cv_tuning/     # LightGBM cross-validation tuning results
│       └── final_selection/    # Final model selection report
│
├── src/
│   ├── download_data.py
│   ├── train.py
│   └── predict.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

Notes:

* Raw Kaggle data files are stored locally under `data/raw/` and are not uploaded to GitHub.
* Trained model binaries and Kaggle submission CSV files are generated locally and are excluded by `.gitignore`.
* The final selected model is LightGBM with color index features, achieving a Kaggle Public Score of `0.95719`.

