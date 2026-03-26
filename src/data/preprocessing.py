# ## preprocessing done through this module
# import pandas as pd
# def preprocess(df):
#     print("Preprossing data")

#     #drop null values
#     df = df.dropna()

#     #convert categorical columns to numeric
#     df = pd.get_dummies(df, drop_first=True)
    
#     print("preprossing done")
#     return df


    # Encode categorical
    df = pd.get_dummies(df, drop_first=True)
    
    # Split features & target
    X = df.drop("G3", axis=1)
    y = df["G3"]
    