import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def visualize_data():
        df = pd.read_csv('sp500_joined_closes.csv')
        df_corr = df.corr()
        #print(df_corr.head())
        #get the coreletion of sp500 joined table
        df_corr.to_csv('cor_tab.csv')
        #make a heatmap and for that value of data needed
        data1 = df_corr.values
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
        fig1.colorbar(heatmap1)
        #setting ticks to identify companies
        ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
        ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
        #flip out y axis so to read easily
        ax1.invert_yaxis()
        ax1.xaxis.tick_top()
        #set column label and row label
        column_labels = df_corr.columns
        row_labels = df_corr.index
        ax1.set_xticklabels(column_labels)
        ax1.set_yticklabels(row_labels)
        plt.xticks(rotation=90)
        plt.savefig('corr_sp500.svg')
visualize_data()
