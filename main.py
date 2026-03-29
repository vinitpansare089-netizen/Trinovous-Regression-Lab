from src.data.data_loader import load_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model
from src.evaluation.evaluate import evaluate_model

df = load_data("data/raw/student-mat.csv")
print(type(df))

#preprocess using function
X_train, X_test, y_train, y_test = preprocess_data(df)


model = train_model(X_train, y_train)


#evaluation
mse, rmse = evaluate_model(model, X_test, y_test)

train_mse, train_rmse = evaluate_model(model, X_train, y_train)
test_mse, test_rmse = evaluate_model(model, X_test, y_test)

print("Train RMSE:", train_rmse)
print("Test RMSE:", test_rmse)

print("Final MSE:", mse)
print("RSME: ", rmse)
