from src.preprocessing import load_data, preprocess_data
from src.train_model import train_models
from src.evaluate import evaluate_models


def main():
    print(" Starting Phishing Website Detection Project...")

    print("\n Loading dataset...")
    df = load_data(r"D:\phishingdetection\data\phishing.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    print("Dataset Loaded Successfully!")
    print("Columns:", df.columns.tolist())

    print("\n Preprocessing data...")
    X, y = preprocess_data(df)

    print(f" Data Ready: {X.shape[0]} samples, {X.shape[1]} features")

    print("\n Label distribution:")
    print(y.value_counts())

    print("\n Training model...")
    model, X_test, y_test = train_models(X, y)

    print(" Model trained and saved in models/model.pkl")
    print(" Feature list saved in models/features.pkl")


    print("\n Evaluating model...")
    evaluate_models({"Random Forest": model}, X_test, y_test)

    print("\n Project completed successfully!")


if __name__ == "__main__":
    main()