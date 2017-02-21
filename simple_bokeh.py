from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5, 5, 6]
y = [2, 3, 3, 5, 3, 3, 5]

output_file('output_ex1.html')

my_plot = figure(title='My Plot',
                 x_axis_label='x',
                 y_axis_label='y')

my_plot.line(x, y, legend='TEMP', line_width=2)
show(my_plot)
