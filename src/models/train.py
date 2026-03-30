# from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train):
    # print("training model with Tuning...")
    

    model = RandomForestRegressor(random_state=42)

    params = {
        "n_estimators": [50, 100],
        "max_depth": [5, 10, None],
        "min_samples_split": [2, 5]
    }

    grid = GridSearchCV(model, params, cv=5, scoring="neg_mean_squared_error")
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    best_params = grid.best_params_
    
    
    # Save the model in as a file
    # print("Loading...model file")
    joblib.dump(best_model, "models/vinit_model.pkl")
    print("loaded.")

    # print("Model Trained")
    return best_model, best_params

