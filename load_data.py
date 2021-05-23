import pandas as pd

def load_potitifact_data():
    df = pd.read_csv('./dataset/politifact_dataset.csv')
    return df