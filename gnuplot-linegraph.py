#!/usr/bin/env python

import numpy
import Gnuplot
import os

g = Gnuplot.Gnuplot()

# Title of the graph
g.title("Family A Water Use")

# Labels for each axis
g.xlabel("time (min)")
g.ylabel("total gallons used")

# Draw a grid on the graph
g("set grid")

# Numeric labels on each axis
g("set xtic 1")
g("set ytic 5")

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [0, 1, 4, 6, 8, 8, 8, 8, 12, 16, 20]

# Plot a line graph
d1 = Gnuplot.Data (x, y, title="Water consumption", with_="lines")

# Draw the graph and store it as a PNG
g("set terminal png size 600,400")
g("set output '/tmp/water.png'")
g.plot(d1)
g.close()

# Make a syscall to open the image
os.system('xdg-open /tmp/water.png')
