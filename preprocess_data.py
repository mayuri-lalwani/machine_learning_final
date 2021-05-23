import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def one_hot_encoding_labels(df, _feature):
    # creating instance of one-hot-encoder
    enc = OneHotEncoder(handle_unknown='ignore')
    # passing bridge-types-cat column (label encoded values of bridge_types)
    results = enc.fit_transform(df[[_feature]]).toarray()
    enc_df = pd.DataFrame(results)
    print(enc.categories_)
    # merge with main df bridge_df on key values
    df = df.join(enc_df)
    return df

def one_dummy_encoding_labels(df, _feature):
    df = pd.concat([df,pd.get_dummies(df[_feature], prefix=_feature)],axis=1)
    return df