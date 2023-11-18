import pandas as pd

if __name__ == '__main__':
    fname = 'Quan-REU_Research-2023.csv'
    df = pd.read_csv(fname)
    df = df.fillna({col: '' for col in df.columns}) # fill nan with empty str
    df.to_markdown('README.md')