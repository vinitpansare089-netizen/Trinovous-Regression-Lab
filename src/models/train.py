from sklearn.tree import DecisionTreeRegressor
import joblib
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train):
    print("training model with Tuning...")

    model = DecisionTreeRegressor(random_state=42)

    params = {
        "max_depth" : [3,5,7,10],
        "min_samples_split" : [2, 5, 10]
    }

    grid = GridSearchCV(model, params, cv=5, scoring="neg_mean_squared_error")
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    print("Params:" , grid.best_params_)
    
    return best_model
    #Save the model in as a file
    # print("Loading...model file")
    # joblib.dump(model, "models/vinit_model.pkl")
    # print("loaded.")

    # print("Model Trained")
    # return model

