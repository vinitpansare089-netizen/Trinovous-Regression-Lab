## preprocessing done through this module
import pandas as pd
def preprocess(df):
    print("Preprossing data")

    #drop null values
    df = df.dropna()

    #convert categorical columns to numeric
    df = pd.get_dummies(df, drop_first=True)
    
    print("preprossing done")
    return df


    