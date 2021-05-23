import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def one_hot_encoding_labels(bridge_df, _featurre):
    # creating instance of one-hot-encoder
    enc = OneHotEncoder(handle_unknown='ignore')
    # passing bridge-types-cat column (label encoded values of bridge_types)
    enc_df = pd.DataFrame(enc.fit_transform(bridge_df[[_featurre]]).toarray())
    # merge with main df bridge_df on key values
    bridge_df = bridge_df.join(enc_df)
    return bridge_df