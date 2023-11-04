import matplotlib.pyplot as plt
import Least.Smath.Matrix as sha

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
        aray_l = sha.Matrix(mat=self.left)
        array_r = sha.Matrix(mat=self.right)
        mat_l_T = aray_l.Transpose()
        mat_l_T_R = mat_l_T * aray_l
        mat_r_T_R = mat_l_T * array_r
        inverse = mat_l_T_R.Inverse()
        entries = (inverse * mat_r_T_R).matrix
        print(entries)
        m = float(entries[0][0])
        b = float(entries[1][0])
        x = sha.Matrix(mat=[self.left[i][0] for i in range(len(self.left))])
        y = [self.right[i][0] for i in range(len(self.right))]
        line_of_best_fit = x.equation(m,b)
        plt.plot(x.matrix, y, "o", x.matrix, line_of_best_fit)
        plt.show()
        print(f"The line of best fit is y= {m} X + {b}")
    def exp(self):
        aray_l = sha.Matrix(mat=self.left)
        array_r = sha.Matrix(mat=self.right).ln() ##change this
        #array_r = np.log(np.array(self.right))
        mat_l_T = aray_l.Transpose()
        mat_l_T_R = mat_l_T * aray_l
        mat_r_T_R = mat_l_T * array_r
        inverse = mat_l_T_R.Inverse()
        entries = (inverse * mat_r_T_R).matrix
        m = float(entries[0][0])
        b = float(entries[1][0])
        x = sha.Matrix(mat=[self.left[i][0] for i in range(len(self.left))])
        y = [self.right[i][0] for i in range(len(self.right))]
        axix=sha.Matrix().axis(min(x.matrix),0.1, (max(x.matrix)+1))
        x_eq=sha.Matrix(mat=axix)
        line_of_best_fit = x_eq.exp(m, b)
        print(line_of_best_fit)
        print(min(x.matrix))
        print(max(x.matrix))
        plt.plot(x.matrix, y, "o", axix, line_of_best_fit)
        plt.show()

        print(f"The line of best fit is y= e^{b}*e^({m}*x)")
