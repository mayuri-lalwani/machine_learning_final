import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def one_hot_encoding_labels(bridge_df, _feature):
    # creating instance of one-hot-encoder
    enc = OneHotEncoder(handle_unknown='ignore')
    # passing bridge-types-cat column (label encoded values of bridge_types)
    results = enc.fit_transform(bridge_df[[_feature]]).toarray()
    enc_df = pd.DataFrame(results, columns=enc.categories_)
    print(enc.categories_)
    # merge with main df bridge_df on key values
    bridge_df = bridge_df.join(enc_df)
    return bridge_df