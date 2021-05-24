import pandas as pd

def load_potitifact_data():
    df = pd.read_csv('./dataset/politifact_dataset.csv')
    return df

def remove_invalid_verdict(df):
    df = df[df.Verdict != 'half-flip']
    df = df[df.Verdict != 'full-flop']
    df = df[df.Verdict != 'no-flip']
    print(df.Verdict.unique())
    return df

def load_africacheck_data():
    df = pd.read_csv('./dataset/africa_check_dataset.csv')
    return df

def load_augument_data():
    df1 = load_potitifact_data()
    df2 = load_africacheck_data()
    _features =['Statement', 'Verdict']
    df1 = df1[_features]
    df2 = df2[_features]
    df = df1.merge(df2, how='left', on=_features)
    return df