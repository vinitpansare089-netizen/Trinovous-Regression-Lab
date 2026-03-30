import joblib
import pandas as pd

def predict_new(data_dict):
    
    print(" Making prediction...")

    # Load artifacts
    model = joblib.load("models/vinit_model.pkl")
    scaler = joblib.load("models/vinit_scalar.pkl")
    columns = joblib.load("models/columns.pkl")

    # Convert input to DataFrame
    df = pd.DataFrame([data_dict])

    # Encode
    df = pd.get_dummies(df)

    # Align columns (VERY IMPORTANT)
    df = df.reindex(columns=columns, fill_value=0)

    # Scale
    df = scaler.transform(df)

    # Predict
    prediction = model.predict(df)

    return prediction[0]