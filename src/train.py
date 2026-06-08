import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


def main():
    train_path = "data/raw/train.csv"
    model_path = "models/random_forest.pkl"

    df = pd.read_csv(train_path)

    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)

    # TODO: Replace with the actual target column name after checking train.csv
    target_col = "class"

    X = df.drop(columns=["id", target_col], errors="ignore")
    y = df[target_col]

    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    valid_pred = model.predict(X_valid)
    acc = accuracy_score(y_valid, valid_pred)

    print(f"Validation Accuracy: {acc:.5f}")

    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    main()
