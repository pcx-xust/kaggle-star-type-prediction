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
├─ data/
│  ├─ raw/
│  ├─ processed/
│  └─ submissions/
├─ src/
│  ├─ download_data.py
│  ├─ train.py
│  └─ predict.py
├─ models/
├─ reports/
│  ├─ figures/
│  └─ model_report.md
├─ README.md
├─ requirements.txt
└─ .gitignore
