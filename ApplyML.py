import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
def apply_ML(ticker):
'''
process data for labels
'''
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    print(df["Symbol"].loc["AMD"])
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)
    for i in range(1,hm_days+1):
        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
    df.fillna(0, inplace=True)
    return tickers, df
apply_ML('MMM')#before this we need labels
def buy_sell_hold(*args):
    cols = [c for c in args]
    req = 0.02
    for col in cols:
        if col > req:
                return 1
        if col < -req:
                return -1
    return 0
#map it to pandas dataframe
def extract_features(ticker):
    tickers, df = apply_ML(ticker)
    df['{}_target'.format(tickers)] = list(map(buy_sell_hold,df['{}_1d'.format(ticker)],
                                               df['{}_2d'.format(ticker)],
                                               df['{}_3d'.format(ticker)],
                                               df['{}_4d'.format(ticker)],
                                               df['{}_5d'.format(ticker)],
                                               df['{}_6d'.format(ticker)],
                                               df['{}_7d'.format(ticker)] )) 
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
    return X, y, df      
'''
we will use k nearest neighbour method
'''

