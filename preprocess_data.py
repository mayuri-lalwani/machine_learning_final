import pandas as pd

def one_hot_encoding_labels(df, _feature):
    df = pd.concat([df,pd.get_dummies(df[_feature], prefix=_feature)],axis=1)
    return df