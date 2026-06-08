
# LightGBM CV Tuning Report

## Objective

This notebook performs cross-validation and small-range hyperparameter tuning for the LightGBM model with color index features.

## Feature Set

Base features:

['u', 'g', 'r', 'i', 'z', 'redshift', 'alpha', 'delta']

Color index features:

['u_g', 'g_r', 'r_i', 'i_z']

Final feature set:

['u', 'g', 'r', 'i', 'z', 'redshift', 'alpha', 'delta', 'u_g', 'g_r', 'r_i', 'i_z']

## Cross-Validation Setting

- Validation method: 5-fold StratifiedKFold
- Selection metric: OOF Macro F1
- Random state: 42

## Tuning Summary

The tuning summary is saved in:

`reports/model/lgbm_cv_tuning/tables/lgbm_cv_tuning_summary.csv`

## Best Parameter Setting

Best parameter name:

`lr003_leaves63`

Best parameters:

{
    "name": "lr003_leaves63",
    "learning_rate": 0.03,
    "num_leaves": 63,
    "min_child_samples": 30,
    "reg_alpha": 0.1,
    "reg_lambda": 1.0,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "n_estimators": 3000
}

## Best OOF Results

| Model | OOF Accuracy | OOF Balanced Accuracy | OOF Macro F1 | Mean Best Iteration |
|---|---:|---:|---:|---:|
| LightGBM CV Tuned | 0.968234 | 0.956756 | 0.957276 | 1259 |

## Submission File

The generated submission file is:

`submissions/lgbm_cv_tuned_submission.csv`

Kaggle Public Score:

待Kaggle提交后填写

## Comparison with Previous Models

| Model | Validation/CV Metric | Kaggle Public Score |
|---|---:|---:|
| RandomForest + color features | 0.944721 | 0.94506 |
| LightGBM + color features | 0.956350 | 0.95719 |
| LightGBM CV tuned | 0.957276 | 待提交后填写 |

## Conclusion

The best cross-validation parameter setting is `lr003_leaves63`.
It achieved an OOF Macro F1 of 0.957276, which is slightly higher than the previous single-split LightGBM validation result.
The generated submission file should be submitted to Kaggle and compared with the current best public score of 0.95719.
