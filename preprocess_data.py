import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def one_hot_encoding_labels(df, _feature):
    # creating instance of one-hot-encoder
    enc = OneHotEncoder(handle_unknown='error')
    # passing bridge-types-cat column (label encoded values of bridge_types)
    results = enc.fit_transform(df[[_feature]]).toarray()
    enc_df = pd.DataFrame(results)
    print(enc.categories_)
    # merge with main df bridge_df on key values
    df = df.join(enc_df)
    df = df.dropna()
    return df

def one_dummy_encoding_labels(df, _feature):
    df = pd.concat([df,pd.get_dummies(df[_feature], prefix=_feature)],axis=1)
    return df

def get_numerical_labels(df, _feature):
    df[_feature].replace(['false', 'pants-fire', 'barely-true', 'half-true', 'mostly-true', 'true'],[0,1,2,3,4,5], inplace=True)
    return df

def split_train_test_data(df, _source, _target, tain_percent=0.7):
    X, y = df[_source], df[_target]
    train_pct_index = int(tain_percent * len(X))
    print('%s out of %s will be trained' % (train_pct_index, len(X)))
    X_train, X_test = X[:train_pct_index], X[train_pct_index:]
    y_train, y_test = y[:train_pct_index], y[train_pct_index:]
    return X_train, X_test, y_train, y_test