### data loading function

import pandas as pd
# import seaborn as sns

def load_data(path):
    try:
        print("loading data...")
        df = pd.read_csv(path)
        print("data loaded")
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Invalid file: {e}')








def load_data(path):
    #print("Loading data")
    df = pd.read_csv(path)
    # print("Data Loaded")
    return df