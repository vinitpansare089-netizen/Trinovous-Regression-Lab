from sklearn.linear_model import LinearRegression
import joblib

def train_model(X, y):
    print("training model...")
    model = LinearRegression()
    model.fit(X, y)
    #Save the model in as a file
    print("Loading...model file")
    joblib.dump(model, "models/vinit_model.pkl")
    print("loaded.")

    print("Model Trained")
    return model

