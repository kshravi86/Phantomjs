from bokeh.plotting import figure, output_file, show
# 1. Load some data in X,Y variables
x = [1, 2, 3, 4, 5] 
y = [23, 15, 7, 12, 21]
# 2. Specify the name of the output HTML file 
output_file(“lines.html”)
#3. create a new plot with a title and axis labels 
p = figure(title=”Bokeh Demo for OSFY”, x_axis_label=’x’, y_axis_label=’y’)
#4. add a line renderer with legend and line thickness
p.line(x, y, legend=”Age”, line_width=3)
#5. show the results 
show(p)
