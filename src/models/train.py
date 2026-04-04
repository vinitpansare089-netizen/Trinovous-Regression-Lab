# from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import joblib
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train, model_type='rf'):
    # print("training model with Tuning...")

### Random forest selection
    if model_type == 'rf':
        model = RandomForestRegressor(random_state=42)
        params = {
            "n_estimators" : [100],
            "max_depth" : [5, 10],
            "min_samples_split" : [5, 10]
        }

        grid = GridSearchCV(model, params, scoring='neg_mean_squared_error')
        grid.fit(X_train, y_train)

        best_model = grid.best_estimator_
        best_params = grid.best_params_

    elif model_type == 'lr':
        best_model = LinearRegression()
        best_model.fit(X_train, y_train)
        best_params = "no hyperparameters"

    elif model_type == 'dt':
        best_model = DecisionTreeRegressor()
        best_model.fit(X_train, y_train)
        best_params = "No need of tuning"

    else:
        raise ValueError("Invalid Model")
    
    joblib.dump(best_model, "models/vinit_models.pkl")
    
    return best_model , best_params


# /////////////////////////

    # model = RandomForestRegressor(random_state=42)

    # params = {
    #     "n_estimators": [50, 100],
    #     "max_depth": [5, 10, None],
    #     "min_samples_split": [2, 5]
    # }

    # grid = GridSearchCV(model, params, cv=5, scoring="neg_mean_squared_error")
    # grid.fit(X_train, y_train)

    # best_model = grid.best_estimator_
    # best_params = grid.best_params_
    
    
    # # Save the model in as a file
    # # print("Loading...model file")
    # joblib.dump(best_model, "models/vinit_model.pkl")
    # print("loaded.")

    # # print("Model Trained") vinit now check evaluation file
    # return best_model, best_params

