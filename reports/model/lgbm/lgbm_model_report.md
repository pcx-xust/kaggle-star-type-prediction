# LightGBM Model Report

## Model Setting

This notebook trains a LightGBM classifier using the original photometric features and additional color index features.

## Feature Set

Base features:

['u', 'g', 'r', 'i', 'z', 'redshift', 'alpha', 'delta']

Color index features:

['u_g', 'g_r', 'r_i', 'i_z']

Final feature set:

['u', 'g', 'r', 'i', 'z', 'redshift', 'alpha', 'delta', 'u_g', 'g_r', 'r_i', 'i_z']

## Validation Results

| Model | Accuracy | Balanced Accuracy | Macro F1 | Best Iteration |
|---|---:|---:|---:|---:|
| LightGBM + color features | 0.967515 | 0.954901 | 0.956350 | 2000 |

## Output Files

- `tables/lgbm_metrics.csv`
- `tables/lgbm_classification_report.csv`
- `tables/lgbm_feature_importance.csv`
- `figures/lgbm_confusion_matrix.png`
- `figures/lgbm_feature_importance.png`

## Notes

The Kaggle score should be recorded separately after submitting the generated submission file.
