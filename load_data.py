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
