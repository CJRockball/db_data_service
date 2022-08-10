import pandas as pd

def import_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = pd.read_csv(url)
    
    
    df.to_csv('./data/tips.csv')
    return df 

if __name__ == "__main__":
    df = import_data()
    print(df.head())
    