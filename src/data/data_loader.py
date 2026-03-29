### data loading function

import pandas as pd
import seaborn as sns

def load_data(path):
    # print("Loading data")
    df = pd.read_csv(path)
    # print("Data Loaded")
    return df