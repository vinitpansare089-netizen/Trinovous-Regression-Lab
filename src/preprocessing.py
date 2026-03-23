def preprocess(df):
    print("Preprossing data")
    df = df.dropna()
    print("preprossing done")
    return df