##model evaluating done in this module
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_model(best_model, X_test, y_test):
    # print("Evaluating Model")
    predictions = best_model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    #evaluation of R2 for regression models
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # print("Evaluated Model")
    return mse, rmse, mae, r2
