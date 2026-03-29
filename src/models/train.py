from sklearn.tree import DecisionTreeRegressor
import joblib

def train_model(X_train, y_train):
    print("training model...")

    model = DecisionTreeRegressor(max_depth=5, min_samples_split=10)
    model.fit(X_train, y_train)
    
    #Save the model in as a file
    print("Loading...model file")
    joblib.dump(model, "models/vinit_model.pkl")
    print("loaded.")

    print("Model Trained")
    return model

