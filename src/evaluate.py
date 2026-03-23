##model evaluating done in this module

from sklearn.metrics import mean_squared_error

def evaluate(model, X, y):
    print("Evaluating Model")
    predictions = model.predict
    mse = mean_squared_error(y, predictions)
    print("Evaluated Model")
    return mse