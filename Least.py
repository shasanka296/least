import numpy as np
import sympy as s
import matplotlib.pyplot as plt


class LSQ:
    def __init__(self, x_val=None, y_val=None, file=None):
        if y_val is None:
            y_val = []
        if x_val is None:
            x_val = []
        x_fromfile = []
        y_fromfile = []
        if file is not None:
            with open(file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    vals = line.split()
                    x_fromfile.append(float(vals[0].strip()))
                    y_fromfile.append(float(vals[1].strip()))
        self.left = [[i, 1] for i in x_val] if len(x_val) != 0 else [[i, 1] for i in x_fromfile]
        self.right = [[i] for i in y_val] if len(y_val) != 0 else [[i] for i in y_fromfile]


    def line(self):
        aray_l = np.array(self.left)
        array_r = np.array(self.right)
        mat_l = s.matrices.Matrix(aray_l)
        mat_r = s.matrices.Matrix(array_r)
        mat_l_T = mat_l.transpose()
        mat_l_T_R = mat_l_T * mat_l
        mat_r_T_R = mat_l_T * mat_r
        inverse = mat_l_T_R.inverse_GE()
        entries = inverse * mat_r_T_R
        m = float(entries[0])
        b = float(entries[1])
        x = np.array([self.left[i][0] for i in range(len(self.left))])
        y = [self.right[i][0] for i in range(len(self.right))]
        line_of_best_fit = m * x + b
        plt.plot(x, y, "o", x, line_of_best_fit)
        plt.show()
        print(f"The line of best fit is y= {m} X + {b}")
    def exp(self):
        aray_l = np.array(self.left)
        array_r = np.log(np.array(self.right))
        mat_l = s.matrices.Matrix(aray_l)
        mat_r = s.matrices.Matrix(array_r)
        mat_l_T = mat_l.transpose()
        mat_l_T_R = mat_l_T * mat_l
        mat_r_T_R = mat_l_T * mat_r
        inverse = mat_l_T_R.inverse_GE()
        entries = inverse * mat_r_T_R
        m = float(entries[0])
        b = float(entries[1])
        x = np.array([self.left[i][0] for i in range(len(self.left))])
        axix = np.linspace(0, max(x), int(max(x)) * 50)
        y = [self.right[i][0] for i in range(len(self.right))]
        line_of_best_fit = np.exp(b) * np.exp(m * axix)
        plt.plot(x, y, "o", axix, line_of_best_fit)
        plt.show()

        print(f"The line of best fit is y= {np.exp(b)}*e^{m}*x")
