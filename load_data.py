import pandas as pd
import requests

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
    df['Verdict'] = df['Verdict'].str.lower()
    trans_dict ={
        'checked': 'mostly-true',
        'unproven': 'false',
        'incorrect': 'pants-fire',
        'misleading': 'barely-true',
        'mostly correct': 'mostly-true',
        'correct': 'true',
        'understated': 'half-true',
        'exaggerated': 'half-true',
        'downplayed': 'half-true',
        'mostly-correct': 'mostly-true',
        'verdict': 'true',
        'name-field-verdict': 'mostly-true',
        'not-rated': 'false'
    }
    df.replace({'Verdict': trans_dict}, inplace=True)
    _features =['Statement', 'Verdict']
    df = df[_features]
    return df

def load_augument_data():
    df = pd.read_csv('./dataset/augument_dataset.csv')
    print(df.Verdict.unique())
    return df

def scrape_data_from_newsapi():
    # BBC news api
    my_url = "https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=4aa01326eb3147a881ad8f93863c9663"
    my_open_bbc_page = requests.get(my_url).json()
    my_article = my_open_bbc_page["articles"]
    my_results = []
    for ar in my_article:
        my_results.append(ar["title"])
    df_news = pd.DataFrame(my_results, columns = ['Statement'])
    return df_news