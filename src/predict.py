import pandas as pd
import joblib


def main():
    test_path = "data/raw/test.csv"
    sample_path = "data/raw/sample_submission.csv"
    model_path = "models/random_forest.pkl"
    output_path = "data/submissions/submission_random_forest.csv"

    test = pd.read_csv(test_path)
    sample = pd.read_csv(sample_path)

    print("Test columns:", test.columns.tolist())
    print("Submission columns:", sample.columns.tolist())

    model = joblib.load(model_path)

    X_test = test.drop(columns=["id"], errors="ignore")
    pred = model.predict(X_test)

    target_col = sample.columns[-1]
    sample[target_col] = pred

    sample.to_csv(output_path, index=False)
    print(f"Submission saved to {output_path}")


if __name__ == "__main__":
    main()
