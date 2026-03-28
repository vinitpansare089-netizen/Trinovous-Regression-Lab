from src.data.data_loader import load_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model
from src.evaluation.evaluate import evaluate

df = load_data("data/raw/student-mat.csv")

#preprocess using function
df = preprocess_data(df)

#Target 
target = "G1"

X = df.drop(target, axis=1)
y = df[target]

model = train_model(X, y)

#evaluation
mse, rmse = evaluate(model, X, y)

print("Final MSE:", mse)
print("RSME: ", rmse)
