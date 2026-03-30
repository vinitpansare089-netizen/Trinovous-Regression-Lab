import joblib
import pandas as pd

def predict_new(data_dict):
    
    model = joblib.load("models/model.pkl")
    scaler = joblib.load("models/vinit_scaler.pkl")
    
    df = pd.DataFrame([data_dict])
    
    df = pd.get_dummies(df)
    
    # ⚠️ align columns (important later)
    # skip for now
    
    df = scaler.transform(df)
    
    prediction = model.predict(df)
    
    return prediction[0]