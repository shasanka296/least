import Least.Smath.Inverter as op
import math


class Matrix:
    """
    The following class initializes a matrix that is used for the least square calculation,
    the creation of the matrix along with different functions of the matrix resemble those of the
    convention of matrix manipulation.
        Attributes:
        matrix (list): The matrix represented as a list of lists.

    Methods:
        __init__(self, shape=None, content=None, mat=None): Initializes the matrix with the specified shape or content.
        __str__(self): Returns a string representation of the matrix.
        __getitem__(self, index): Retrieves an element from the matrix using row and column indices.
        Transpose(self): Computes and returns the transpose of the matrix.
        __mul__(self, other): Multiplies the matrix by another matrix or its transpose.
        equation(self, first, constant): Returns the values of the solution to a linear equation.
        axis(self, start, dt, stop): Generates a range of values for the X axis.
        row(self, i=0): Retrieves a specific row from the matrix.
        col(self, i=0): Retrieves a specific column from the matrix.
        Inverse(self): Computes and returns the inverse of the matrix, using the Invert module.
        ln(self): Calculates the natural logarithm of the elements in the matrix.
        exp(self, first, constant): Computes exp of given exp equation.

    """

    def __init__(self, shape=None, content=None, mat=None):
        """
                Initialize a Matrix object with optional shape, content, or matrix values.

                :param shape: A list representing the shape of the matrix, e.g., [rows, columns].
                :param content: A list representing the matrix content.
                :param mat: A list of lists representing the matrix directly.

                :raises TypeError: If input arguments are not of the correct type.
                :raises ValueError: If the specified shape is not a valid integer or shape/content mismatch.
                """
        self.matrix = []
        if shape is not None and not isinstance(shape, list):
            raise TypeError("The shape must be a list")
        if content is not None and not isinstance(content, list):
            raise TypeError("The content must be passed as a list")
        if mat is not None and not isinstance(mat, list):
            raise TypeError("The passed list is not a valid python list")
        if shape is not None and content is not None:
            try:
                self.matrix = [[0 for _ in range(shape[1])] for _ in range(shape[0])]
            except ValueError:
                raise ValueError("The specified shape is not a integer")
            try:
                self.matrix[:] = content
            except ValueError:
                raise ValueError("Shape of content and shape does not match")

        elif shape is not None and content is None:
            try:
                self.matrix = [[0 for _ in range(shape[1])] for _ in range(shape[0])]
            except TypeError:
                raise TypeError("The specified shape is not a integer")
        elif mat is not None:
            self.matrix[:] = mat

    def __str__(self):
        """
                Return a string representation of the matrix.

                :return: A string representation of the matrix.
                """

        return str(self.matrix)

    def __getitem__(self, index):
        """Retrieve an element from the matrix using row and column indices.

                Args:
                    index (tuple): A tuple representing the row and column indices.

                Returns:
                    float: The element at the specified position.

                Raises:
                    IndexError: If the indices are out of bounds.
                """

        row = index[0]
        col = index[1]
        try:
            return self.matrix[row][col]
        except IndexError:
            raise IndexError("index out of bound")

    def Transpose(self):
        """Compute and return the transpose of the matrix.

        Returns:
            Matrix: The transposed matrix.
        """

        transposed = [[0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]
        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                transposed[i][j] = self.matrix[j][i]
        return Matrix(mat=transposed)

    def __mul__(self, other):
        """Multiply the matrix by another matrix or its transpose.

                Args:
                    other (Matrix): The matrix to multiply.

                Returns:
                    Matrix: The result of the matrix multiplication.

                Raises:
                    AttributeError: If 'other' is not a valid matrix.
                    TypeError: If there is a shape mismatch.
                """

        output_mat = []
        try:
            other_trans = other.Transpose()
        except AttributeError:
            raise AttributeError("not a sha mat")
        if len(other.matrix) != len(self.matrix[0]):
            raise TypeError("Shape miss-match")
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other_trans.matrix)):
                partial_sum = 0
                for k in range(len(other_trans.matrix[0])):
                    partial_sum += self.matrix[i][k] * other_trans.matrix[j][k]
                row.append(partial_sum)
            output_mat.append(row)
        return Matrix(mat=output_mat)

    def equation(self, first, constant):
        """Solve an equation using the matrix.

                Args:
                    first (float): Coefficient for the linear term.
                    constant (float): Constant value.

                Returns:
                    list: A list of solutions to the equation.
                """

        output = []
        for teams in self.matrix:
            output.append((teams * first) + constant)
        return output

    def axis(self, start, dt, stop):
        """Generate a range of values for an axis.

                Args:
                    start (float): Start value.
                    dt (float): Step size.
                    stop (float): End value.

                Returns:
                    list: A list of values for the axis.
                """

        returner = []

        total_int = (float(stop) - float(start)) / float(dt)

        for i in range(int(total_int)):
            returner.append(float(start) + float(dt) * float(i))
        return returner

    def row(self, i=0):
        """Retrieve a specific row from the matrix.

        Args:
            i (int): Row index.

        Returns:
            list: The specified row from the matrix.
        """

        return self.matrix[i]

    def col(self, i=0):
        """Retrieve a specific column from the matrix.

                Args:
                    i (int): Column index.

                Returns:
                    list: The specified column from the matrix.
                """

        colum = []
        for r in self.matrix:
            colum.append(r[i])

        return colum

    def Inverse(self):
        """Compute and return the inverse of the matrix.

                Returns:
                    Matrix: The inverted matrix.
                """

        to_invert = self.matrix
        inverted = op.Inverter(to_invert).returner()
        return Matrix(mat=inverted)

    def ln(self):
        """Calculate the natural logarithm of the elements in the matrix.

        Returns:
            Matrix: The matrix with natural logarithms of elements.
        """

        output_mat = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                output_mat[i][k] = math.log(self.matrix[i][k])
        return Matrix(mat=output_mat)

    def exp(self, first, constant):
        """Compute the exponentiation of elements in the matrix.

        Args:
            first (float): Coefficient for exponentiation.
            constant (float): Constant value.

        Returns:
            list: A list of exponential values generated after the code is run.
        """

        output = []
        for teams in self.matrix:
            output.append(math.exp((float(teams) * float(first))) * math.exp(constant))
        return output
