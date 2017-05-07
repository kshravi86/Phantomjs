from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [23, 15, 7, 12, 21]

output_file(“lines.html”)

p = figure(title=”Bokeh Demo for OSFY”, x_axis_label=’x’, y_axis_label=’y’)


p.line(x, y, legend=”Age”, line_width=3)

show(p)
