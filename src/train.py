from sklearn.linear_model import LinearRegression

def train_model(X, y):
    print("training model...")
    model = LinearRegression()
    model.fit(X, y)
    print("Model Trained")
    return model