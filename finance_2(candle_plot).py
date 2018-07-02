import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('tesla.csv', parse_dates = True, index_col = 0)

from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates


#creating our own ohlc data(open high low close)

df_ohlc = df['Close'].resample('10D').ohlc()
'''
What we've done here is created a new dataframe, based on the df['Close']column, resamped with a 10 day window, and the resampling is an ohlc. We could also do things like .mean() or .sum() for 10 day averages, or 10 day sums. Keep in mind, this 10 day average would be a 10 day average, not a rolling average. Since our data is daily data, resampling it to 10day data effectively shrinks the size of our data significantly. This is how you can normalize multiple datasets.
'''

#resampling the volume data

df_vol = df['Volume'].resample('10D').sum()
#doing the same with dates to visualize it properly
df_ohlc = df_ohlc.reset_index()
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.xaxis_date()
#candlestic graph
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

ax2.fill_between(df_vol.index.map(mdates.date2num),df_vol.values,0)

plt.savefig('candlestick.svg')
