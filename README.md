# least
This is a small package that can be used to create least square plots, supports only lines for now.

Dependencies:
numpy
mathplotlib
sympy

Example use:

import Least as least
least.LSQ(x_val=[2,6,10,12], y_val=[1,2,3,4]) 

For when one wants to manualy type in the x and y values


import Least as least
least.LSQ(file="Path")

When one has a file with the data instead

The data file must be in the following format:
X Y

Where the x vlaues is listed first and the y after it, the empty spaces between x and y is not relevent
