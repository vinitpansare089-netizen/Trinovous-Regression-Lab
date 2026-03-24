from src.data_loader import load_data
from src.preprocessing import preprocess
from student_mat.src.models.train import train_model
from student_mat.src.evaluation.evaluate import evaluate

df = load_data("data/raw/student-mat.csv")

df = preprocess(df)

target = "G3"

X = df.drop(target, axis=1)
y = df[target]

model = train_model(X, y)

mse, rmse = evaluate(model, X, y)

print("Final MSE:", mse)
print("RSME: ", rmse)
