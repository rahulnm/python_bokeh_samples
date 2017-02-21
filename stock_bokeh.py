import pandas as pd
import numpy as np
from bokeh.plotting import output_file, figure, show

# import datetime as dt
# import pandas_datareader.data as web
# temp tp create tsla data
# start = dt.datetime(2010, 1, 1)
# end = dt.datetime(2016, 12, 31)
# df = web.DataReader('TSLA', 'yahoo', start, end)
# df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True)
tsla = np.array(df['Adj Close'])
tsla_dates = np.array(df['Date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size) / float(window_size)
tsla_avg = np.convolve(tsla, window, 'same')

# output to static HTML file
output_file("stocks.html", title="stocks.py example")

# create a new plot with a a datetime axis type
p = figure(width=1200, height=650, x_axis_type="datetime")

# add renderers
p.circle(tsla_dates, tsla, size=4, color='darkgrey', alpha=0.2, legend='close')
p.line(tsla_dates, tsla_avg, color='navy', legend='avg')

# NEW: customize by setting attributes
p.title.text = "TSLA One-Month Average"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
p.ygrid.band_fill_color = "blue"
p.ygrid.band_fill_alpha = 0.1

# show the results
show(p)

print(df.head())
print(tsla)
print(tsla_dates)
print(window)
print(tsla_avg)
