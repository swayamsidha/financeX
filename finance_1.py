#import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
#import pandas_datareader.data as web

df = pd.read_csv('tesla.csv', parse_dates = True, index_col = 0)

'''
now we will implement simple moving average
the idea is take a window of time, and calculate the average price in that window. Then we shift that window over one period, and do it again. In our case, we'll do a 100 day rolling moving average. So this will take the current price, and the prices from the past 99 days, add them up, divide by 100, and there's your current 100-day moving average. Then we move the window over 1 day, and do the same thing again
'''
df['Mov_Avg'] = df['Close'].rolling(window = 100, min_periods = 0).mean()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

'''
we want to create two subplots, and both subplots are going to act like they're on a 6x1 grid, where we have 6 rows and 1 column. The first subplot starts at (0,0) on that grid, spans 5 rows, and spans 1 column. The next axis is also on a 6x1 grid, but it starts at (5,0), spans 1 row, and 1 column. The 2nd axis also has the sharex=ax1, which means that ax2 will always align its x axis with whatever ax1's is, and visa-versa
'''

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['Mov_Avg'])
ax2.bar(df.index, df['Volume'])
plt.savefig('moving_avg.svg')

