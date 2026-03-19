from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from xgboost import XGBClassifier
import pandas as pd
import joblib


def train_models(X, y):

   
    important_features = [
        'length_url',
        'length_hostname',
        'nb_dots',
        'nb_hyphens',
        'nb_at',
        'nb_qm',
        'nb_www',
        'https_token',
        'ratio_digits_url',
        'nb_subdomains',
        'prefix_suffix',
        'shortening_service'
    ]

    X = X[important_features]

    df = pd.concat([X, y], axis=1)

    print("\nBefore balancing:")
    print(df['status'].value_counts())

    df_majority = df[df['status'] == 0]
    df_minority = df[df['status'] == 1]

   
    df_minority_upsampled = resample(
        df_minority,
        replace=True,
        n_samples=len(df_majority),
        random_state=42
    )

    df_balanced = pd.concat([df_majority, df_minority_upsampled])
    df_balanced = df_balanced.sample(frac=1, random_state=42)


    X = df_balanced.drop('status', axis=1)
    y = df_balanced['status']


    joblib.dump(important_features, "models/features.pkl")


    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.1,
        eval_metric='logloss'
    )

    model.fit(X_train, y_train)


    joblib.dump(model, "models/model.pkl")

    return model, X_test, y_test