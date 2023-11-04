# Least
This is a small package that can be used to create the least square plots, supports lines and exps. It is functional but is still in development 

Dependencies:
mathplotlib

Example use:

```python
from Least.Smath import Least as least
from Least.Smath import Matrix as mat

Transposed=a.Transpose()

least.LSQ(x_val=[0,1,2,3], y_val=[1,10,100,1000]).exp()
a=mat.Matrix(mat=[[1,1,2,3],[1,2,3,4],[2,3,4,5],[2,3,6,5]])
inverted_a=a.Inverse()
value_in_row_1_colum_0=a[1,0]
Transposed=a.Transpose()
identity=a*inverted_a
least.LSQ(x_val=[2,6,10,12], y_val=[1,2,3,4]).line()
least.LSQ(x_val=[2,6,10,12], y_val=[1,2,3,4]).exp()
```


For when one wants to type in the x and y values manually.

```python
least.LSQ(file="Path").line()
least.LSQ(file="Path").exp()
```
When one has a file with the data instead.

The data file must be in the following format:
X Y

Where the x value is listed first and the y after it, the empty spaces between x and y are irrelevant.
