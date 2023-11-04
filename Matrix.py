import Inverter as op
import math

class Matrix:


    """The following class initializes a matrix that is used for the least square calculation,
     the comption of the matrix along with different functions of the matrix resemble those the
      convention of matrix manipulation."""


    def __init__(self, shape=None, content=None, mat=None):

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
        return str(self.matrix)

    def __getitem__(self, index):
        row = index[0]
        col = index[1]
        try:
            return self.matrix[row][col]
        except IndexError:
            raise IndexError("index out of bound")

    def Transpose(self):
        transposed = [[0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]
        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                transposed[i][j] = self.matrix[j][i]
        return Matrix(mat=transposed)

    def __mul__(self, other):
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
    def equation(self,first,constat):
        output=[]
        for iteams in self.matrix:
            output.append((iteams*first)+constat)
        return output
    def axis(self,start,dt,stop):
        returner=[]
        print(start)
        print(stop)
        total_int=(float(stop)-float(start))/float(dt)
        print(float(stop))
        print(float(start))
        print(total_int)
        print(dt)
        for i in range(int(total_int)):
            returner.append(float(start)+float(dt)*float(i))
        return returner


    def row(self, i=0):
        return self.matrix[i]

    def col(self, i=0):
        colum = []
        for r in self.matrix:
            colum.append(r[i])

        return colum
    def Inverse(self):
        to_invert=self.matrix
        inverted=op.Iverter(to_invert).returner()
        return Matrix(mat=inverted)
    def ln(self):
        outputmat=[[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                outputmat[i][k]=math.log(self.matrix[i][k])
        return Matrix(mat=outputmat)
    def exp(self,first,constant):
        output=[]
        for iteams in self.matrix:
            output.append(math.exp((iteams*first))*math.exp(constant))
        return output

