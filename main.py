from src.data_loader import load_data
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate

df = load_data("data/student-mat.csv")

df = preprocess(df)

target = "G3"

X = df.drop(target, axis=1)
y = df[target]

model = train_model(X, y)

rmse, mse = evaluate(model, X, y)

print("Final MSE:", mse)
print("RSME: ", rmse)
