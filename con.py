import numpy as np 
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

N = 100
x = np.linspace(0, 4*np.pi, N) 
y0 = np.sin(x) 
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)
output_file('linked_panning.html')

