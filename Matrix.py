
class Matrix:
    def __init__(self, shape=None,content=None,mat=None):
        self.matrix=[]
        if shape!=None and not isinstance(shape,list):
            raise TypeError("The shape must be a list")
        if content!=None and not isinstance(content,list):
            raise TypeError("The content must be passed as a list")
        if mat != None and not isinstance(mat,list):
            raise TypeError("The passed list is not a valid python list")
        if shape != None and content != None:
            try:
                self.matrix=[[0 for _ in range(shape[1])] for _ in range(shape[0])]
            except ValueError:
                 raise ValueError("The specified shape is not a integer")
            try:
                self.matrix[:]=content
            except ValueError:
               raise ValueError("Shape of content and shape does not match")

        elif shape != None and content == None:
            try:
                self.matrix = [[0 for i in range(shape[1])] for i in range(shape[0])]
            except TypeError:
                raise TypeError("The specified shape is not a integer")
        elif mat != None:
            self.matrix = mat

    def __str__(self):
        return str(self.matrix)

    def __getitem__(self,index):
        row=index[0]
        col=index[1]
        try:
            return self.matrix[row][col]
        except IndexError:
            raise IndexError("index out of bound")



    def Transpose(self):
        transposed=[[0 for _ in range (len(self.matrix))] for _ in range(len(self.matrix[0]))]
        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                transposed[i][j]= self.matrix[j][i]
        return Matrix(mat=transposed)

    def __mul__(self, other):
        output_mat=[]
        try:
            other_trans= other.Transpose()
        except:
            print("not a sha mat")
            return
        if len(other.matrix) != len(self.matrix[0]):
            raise TypeError("Shape miss-match")
        for i in range(len(self.matrix)):
            row=[]
            for j in range(len(other_trans.matrix)):
                sum = 0
                for k in range(len(other_trans.matrix[0])):
                    sum += self.matrix[i][k]* other_trans.matrix[j][k]
                row.append(sum)
            output_mat.append(row)
        return Matrix(mat=output_mat)


    def row(self,i=0):
        return self.matrix[i]

    def col(self,i=0):
        colum=[]
        for r in self.matrix:
            colum.append(r[i])

        return colum
    def Inverse(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise TypeError("not a squre matrix")
    def Det(self):
        det=0
        
        return det
