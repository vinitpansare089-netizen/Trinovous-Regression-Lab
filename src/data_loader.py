### data loading function

import pandas as pd

def load_data(path):
    print("Loading data")
    df = pd.read_csv(path)
    print("Data Loaded")
    return df