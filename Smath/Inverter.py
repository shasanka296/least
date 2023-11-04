class Iverter():
    def __init__(self,mat):
        use_this_mat = mat
        self.iden_mat = [[0 for _ in range(len(use_this_mat))] for _ in range(len(use_this_mat))]
        for i in range(len(self.iden_mat)):
            self.iden_mat[i][i] = 1

        for i in range(len(use_this_mat)):
            to_swap = 0
            swap_with = 0
            if use_this_mat[i][i] == 0:
                to_swa = i
                looking = True
                while looking:
                    print("checking pivots")
                    for j in range(len(use_this_mat) - i):
                        if use_this_mat[j + i][i] != 0:
                            swap_with = j + i
                            looking = False
                        else:
                            pass
            use_this_mat = self.swaper(use_this_mat, swap_with, to_swap)
            self.iden_mat = self.swaper(self.iden_mat, swap_with, to_swap)

        for i in range(len(use_this_mat)):
            use_this_mat = self.norm(use_this_mat)
            current_piviot = use_this_mat[i][i]
            multi_factor = 0
            looking_at = 0
            number_of_negative_iterations = 0
            number_of_positive_iterations = 0
            for t in range(len(use_this_mat) - 1):

                if i - (number_of_negative_iterations + 1) >= 0:
                    number_of_negative_iterations += 1
                    looking_at = i - number_of_negative_iterations
                else:
                    number_of_positive_iterations += 1
                    looking_at = i + number_of_positive_iterations

                try:
                    multi_factor = -1 * float(use_this_mat[looking_at][i]) / float(current_piviot)
                except IndexError:
                    break
                new_row_id = self.row_adder( self.iden_mat[looking_at],  self.iden_mat[i], multi=multi_factor)
                new_row_mat = self.row_adder(use_this_mat[looking_at], use_this_mat[i], multi=multi_factor)


                self.iden_mat[looking_at] = new_row_id

                use_this_mat[looking_at] = new_row_mat

    def swaper(self, mas, swap_to, swap_from):
        r_mat = mas
        temp_mat = r_mat[swap_from]
        r_mat[swap_from] = r_mat[swap_to]
        r_mat[swap_to] = temp_mat
        return r_mat

    def row_adder(self,row1, row2, multi=1):
        sum = []
        for i, k in zip(row1, row2):
            sum.append(float(i) + float(multi * k))
        return sum

    def row_unity(self,row, element):
        unity = []
        non_unit = row
        for i in non_unit:
            unity.append(float(i) / float(element))
        return unity

    def norm(self, mat_norm):
        nor = mat_norm
        for i in range(len(nor)):
            current_piviot = nor[i][i]
            nor[i] = self.row_unity(nor[i], current_piviot)
            self.iden_mat[i] = self.row_unity(self.iden_mat[i], current_piviot)
        return nor
    def returner(self):
        return self.iden_mat