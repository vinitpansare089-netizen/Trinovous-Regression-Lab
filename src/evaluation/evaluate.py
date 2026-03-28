##model evaluating done in this module
import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):
    print("Evaluating Model")
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    print("Evaluated Model")
    return mse, rmse
