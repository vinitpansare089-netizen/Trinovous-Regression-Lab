from src.data.data_loader import load_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model
from src.evaluation.evaluate import evaluate_model
from src.prediction.predict import predict_new
import json
import os
from src.logger import get_logger


df = load_data("data/raw/student-mat.csv")
# print(type(df))

#preprocess using function
X_train, X_test, y_train, y_test = preprocess_data(df)


model, params = train_model(X_train, y_train, model_type='rf')


print(f"Best Params: {params}")
print(f"Model Type: {type(model)}")


#evaluation
mse, rmse, mae, r2 = evaluate_model(model, X_test, y_test)

train_mse, train_rmse, train_mae, train_r2 = evaluate_model(model, X_train, y_train)
test_mse, test_rmse, test_mae, test_r2 = evaluate_model(model, X_test, y_test)

print("Train RMSE:", train_rmse)
print("Test RMSE:", test_rmse)
print("Test R2:", test_r2)
print("Test Mae: ", mae)

print("Final MSE:", mse)
print("RSME: ", rmse)
print("R2: ", r2)
print("Test Mae: ", mae)


studytime = int(input("Enter studytime: "))
failures = int(input("Enter failures: "))
absences = int(input("Enter absences(1-5): "))
# school = (input("Enter school: "))
# sex = int(input("Enter sex: "))

sample = {
    "studytime": studytime,
    "failures": failures,
    "absences": absences,
    "school": "GP",
    "sex": "M"
}

result = predict_new(sample)

print("Predicted G3:", result)

os.makedirs("artifacts", exist_ok=True)

results = {
    "train_rmse": train_rmse,
    "test_rmse": test_rmse,
    "mse": mse,
    "best_params": params
}

with open("artifacts/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Results saved to artifacts/results.json")

logger = get_logger()

logger.info("Pipeline started")
logger.info(f"Best Params: {params}")
logger.info(f"Train RMSE: {train_rmse}")
logger.info(f"Test RMSE: {test_rmse}")

