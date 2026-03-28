from sklearn.linear_model import LinearRegression
import joblib

def train_model(X, y):
    print("training model...")
    model = LinearRegression()
    model.fit(X, y)
    #Save the model in as a file
    joblib.dump(model, "vinit_model.pkl")

    print("Model Trained")
    return model

