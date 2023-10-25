import numpy as np
import sympy as s
import matplotlib.pyplot as plt
class LSQ:
    def __init__(self,x_val=[], y_val=[], file=None):
        x_fromfile=[]
        y_fromfile=[]
        if file!= None:
            with open(file,"r") as f:
                lines=f.readlines()
                for l in lines:
                    vals=l.split()
                    x_fromfile.append(float(vals[0].strip()))
                    y_fromfile.append(float(vals[1].strip()))
        left= [[i,1] for i in x_val] if len(x_val) !=0 else [[i,1] for i in x_fromfile]
        right=[[i] for i in y_val] if len(y_val) !=0 else [[i] for i in y_fromfile]
        arayl=np.array(left)
        arrayr=np.array(right)
        matl=s.matrices.Matrix(arayl)
        matr=s.matrices.Matrix(arrayr)
        matlT= matl.transpose()
        matlTR= matlT*matl
        matrTR=matlT*matr
        inverse=matlTR.inverse_GE()
        entries=inverse*matrTR
        m=float(entries[0])
        b=float(entries[1])
        x=np.array([left[i][0] for i in range(len(left))])
        y=[right[i][0]for i in range(len(right))]
        line_of_best_fit= m*x+b
        plt.plot(x,y,"o",x,line_of_best_fit)
        plt.show()

        print(f"The line of best fit is y= {m} X + {b}")
