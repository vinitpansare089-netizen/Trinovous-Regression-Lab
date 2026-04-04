import joblib
from fastapi import FastAPI
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

#app banana hai
app = FastAPI()

##ML model ko load krenge
model = joblib.load("models/vinit_models.pkl")
scaler = joblib.load("models/vinit_scalar.pkl")
columns = joblib.load("models/columns.pkl")

@app.get("/")
def Home():
    return {'message' : "working Vinit...."}

@app.post("/predict")
def predict(data: dict):
    print("incoming request: ", data)

    #convert karega data frame me kyuki dict ke form me aa raha hai
    df = pd.DataFrame([data])

    #convert categorical columns to numerical columns...
    df = pd.get_dummies(df)

    #reindexing karne ke liye according to what we except
    df = df.reindex(columns=columns, fill_value=0)

    df = scaler.transform(df)

    prediction = model.predict(df)[0]

    return {f'Predictions' : float(prediction)}




