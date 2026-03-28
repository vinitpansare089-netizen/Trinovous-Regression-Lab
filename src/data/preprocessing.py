## preprocessing done through this module
# import pandas as pd
# def preprocess(df):
#     print("Preprossing data")

#     #drop null values
#     df = df.dropna()

#     #convert categorical columns to numeric
#     df = pd.get_dummies(df, drop_first=True)
    
#     print("preprossing done")
#     return df

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(df):
    
    # Encode categorical
    df = pd.get_dummies(df, drop_first=True)
    
    # Split features & target
    X = df.drop("G3", axis=1)
    y = df["G3"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Loading.... scalar file")
    joblib.dump(scaler, "models/vinit_scalar.pkl")
    print("Loaded")

    return X_train, X_test, y_train, y_test
    