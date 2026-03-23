from sklearn.linear_model import LinearRegression

def train(X, y):
    print("training model...")
    model = LinearRegression()
    model.fit(X, y)
    print("Model Trained")
    return model