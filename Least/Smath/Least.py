import matplotlib.pyplot as plt
import Least.Smath.Matrix as sha



class LSQ:
    """The 'LSQ' class performs least squares regression for linear and exponential models.
    It is assumed that the data given are suitable for such models.

    Methods:
        __init__(self, x_val=None, y_val=None, file=None): Initializes the LSQ instance with data for regression.
        One may use a file or input it manually.
        line(self): Performs linear regression and plots the line of best fit.
        exp(self): Performs exponential regression and plots the exp curve of best fit.

    Attributes:
        left (list of lists): The independent variables matrix.
        right (list of lists): The dependent variable matrix.

    Note:
        The module is still in progress and my not give results that are always accurate.
    """

    def __init__(self, x_val=None, y_val=None, file=None):
        """Initialize the LSQ instance with data for regression.

        Args:
            x_val (list, optional): List of independent variable values.
            y_val (list, optional): List of dependent variable values.
            file (str, optional): Path to a file containing data for regression.

        Raises:
            Exception: If the file does not exist or cannot be read.
        """
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
        """Performs linear regression and plots the line of best fit.

        This method calculates the linear regression coefficients and plots the line of best fit. The regression
        is performed by finding the weights of the vector projection of the solution vector on the column-space.

        Note:
            Requires 'matplotlib' for plotting.

        Raises:
            Exception: If the required data is not available.
        """
        aray_l = sha.Matrix(mat=self.left)
        array_r = sha.Matrix(mat=self.right)
        mat_l_T = aray_l.Transpose()
        mat_l_T_R = mat_l_T * aray_l
        mat_r_T_R = mat_l_T * array_r
        inverse = mat_l_T_R.Inverse()
        entries = (inverse * mat_r_T_R).matrix
        m = float(entries[0][0])
        b = float(entries[1][0])
        x = sha.Matrix(mat=[self.left[i][0] for i in range(len(self.left))])
        y = [self.right[i][0] for i in range(len(self.right))]
        line_of_best_fit = x.equation(m, b)
        plt.plot(x.matrix, y, "o", x.matrix, line_of_best_fit)
        plt.show()
        print(f"The line of best fit is y= {m} X + {b}")

    def exp(self):
        """Performs exponential regression and plots the curve of best fit.

        This method calculates the exponential regression coefficients and plots the curve of best fit. The
        regression is performed by first linearizing the equation and following the methods as in the linear model.

        Note:
            Requires 'matplotlib' for plotting.

        Raises:
            Exception: If the required data is not available.
        """
        aray_l = sha.Matrix(mat=self.left)
        array_r = sha.Matrix(mat=self.right).ln()
        mat_l_T = aray_l.Transpose()
        mat_l_T_R = mat_l_T * aray_l
        mat_r_T_R = mat_l_T * array_r
        inverse = mat_l_T_R.Inverse()
        entries = (inverse * mat_r_T_R).matrix
        m = float(entries[0][0])
        b = float(entries[1][0])
        x = sha.Matrix(mat=[self.left[i][0] for i in range(len(self.left))])
        y = [self.right[i][0] for i in range(len(self.right))]
        axis = sha.Matrix().axis(min(x.matrix), 0.1, (max(x.matrix) + 1))
        x_eq = sha.Matrix(mat=axis)
        line_of_best_fit = x_eq.exp(m, b)
        plt.plot(x.matrix, y, "o", axis, line_of_best_fit)
        plt.show()
        print(f"The line of best fit is y= e^{b}*e^({m}*x)")


