import pandas as pd
from bokeh.plotting import output_file, figure, show
from math import pi

df = pd.read_csv(filepath_or_buffer='tsla.csv',
                 parse_dates=True)[:50]
df.rename(columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])

inc = df.close > df.open
dec = df.close < df.open
w = 12 * 60 * 60 * 1000  # half day in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save,hover,crosshair"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title="TSLA Candlestick")
p.xaxis.major_label_orientation = pi / 4
p.grid.grid_line_alpha = 0.3

p.segment(df.date, df.high, df.date, df.low, color="black")
p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#a3db0a", line_color="black")
p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#e94316", line_color="black")

output_file("candlestick.html", title="candlestick.py example")

show(p)  # open a browser
print(df.head())
print(df.date[inc])
print(df.date[dec])
