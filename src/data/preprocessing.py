

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(df):
    
    # Encode categorical
    df = pd.get_dummies(df, drop_first=True)

    
    df = df.drop(['G1', 'G2'], axis=1)
    # df = df.drop(['G1'], axis=1)

    # Feature engineering
    df["study_failures"] = df["studytime"] * (df["failures"] + 1)
    df["absence_level"] = df["absences"] / (df["studytime"] + 1)

    # Split features & target
    X = df.drop("G3", axis=1)
    y = df["G3"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scaling the columns (0-1)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # after encoding
    columns = X.columns

    joblib.dump(columns, "models/columns.pkl")


    # print("Loading.... scalar file")
    joblib.dump(scaler, "models/vinit_scalar.pkl")
    # print("Loaded")

    return X_train, X_test, y_train, y_test
    