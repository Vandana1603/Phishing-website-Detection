
import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding='latin1')
    return df
def preprocess_data(df):
    df = df.drop(columns=["url"])

    y = df["status"]

   
    y = y.replace({
        "legitimate": 0,
        "phishing": 1
    })

    X = df.drop(columns=["status"])

    return X, y
