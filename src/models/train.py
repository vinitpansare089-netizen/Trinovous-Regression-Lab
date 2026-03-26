# from sklearn.linear_model import LinearRegression

# def train_model(X, y):
#     print("training model...")
#     model = LinearRegression()
#     model.fit(X, y)
#     print("Model Trained")
#     return model

from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model