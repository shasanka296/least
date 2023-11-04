class Inverter:
    """The 'Inverter' class is called by the Matrix module to compute inverse of the given matrix,
    it uses gauss-jordan reduction to compute the inverse, it is assumed that the matrix is invertible.

    Methods:
        __init__(self, mat): Initializes the Inverter with a matrix to invert.
        swapper(self, mas, swap_to, swap_from): Swaps rows in a matrix.
        pivot_corrector(self, use_this_mat): Makes sure each row has a pivot.
        row_adder(self, row1, row2, multi=1): Adds rows with an optional multiplication factor.
        row_unity(self, row, element): Normalizes a row by dividing all elements by the pivot element.
        norm(self, mat_norm): Normalizes a matrix by making diagonal element's unity.
        returner(self): Returns the inverted matrix.

    Note: This class is designed for internal use in matrix inversion and may not be suitable for general-purpose
    matrix operations.
    """

    def __init__(self, mat):
        """Initialize the Inverter with a matrix to invert.

        Args:
            mat (list): The matrix to be inverted.

        Raises:
            Exception: If the matrix is not invertible.
        """
        use_this_mat = []
        use_this_mat[:] = mat
        self.iden_mat = [[0 for _ in range(len(use_this_mat))] for _ in range(len(use_this_mat))]
        for i in range(len(self.iden_mat)):
            self.iden_mat[i][i] = 1

        for i in range(len(use_this_mat)):
            use_this_mat[:] = self.pivot_corrector(use_this_mat)
            use_this_mat[:] = self.norm(use_this_mat)
            current_pivot = use_this_mat[i][i]
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
                    multi_factor = -1 * float(use_this_mat[looking_at][i]) / float(current_pivot)
                except IndexError:
                    break
                new_row_id = self.row_adder(self.iden_mat[looking_at], self.iden_mat[i], multi=multi_factor)
                new_row_mat = self.row_adder(use_this_mat[looking_at], use_this_mat[i], multi=multi_factor)

                self.iden_mat[looking_at] = new_row_id
                use_this_mat[looking_at] = new_row_mat

    def swapper(self, mas, swap_to, swap_from):
        """Swap rows in a matrix.

        Args:
            mas (list): The matrix in which rows will be swapped.
            swap_to (int): Index of the first row to be swapped.
            swap_from (int): Index of the second row to be swapped.

        Returns:
            list: The matrix with swapped rows.
        """
        r_mat = mas
        temp_mat = r_mat[swap_from]
        r_mat[swap_from] = r_mat[swap_to]
        r_mat[swap_to] = temp_mat
        return r_mat

    def pivot_corrector(self, use_this_mat):
        """Correct pivot elements in the matrix.

        Args:
            use_this_mat (list): The matrix in which pivot elements will be corrected.

        Returns:
            list: The matrix with corrected pivot elements.
        """
        use_this = use_this_mat
        for i in range(len(use_this)):
            to_swap = 0
            swap_with = 0
            if use_this[i][i] == 0:
                to_swap = i
                looking = True
                a = 0
                while looking:
                    print("checking pivots")
                    a += 1
                    for j in range(len(use_this) - i):
                        if use_this[j + i][i] != 0:
                            swap_with = j + i
                            looking = False
                        else:
                            if a > len(use_this):
                                raise Exception("this mat is not invertible")
                            pass
                use_this = self.swapper(use_this, swap_with, to_swap)
                self.iden_mat = self.swapper(self.iden_mat, swap_with, to_swap)
        return use_this_mat

    def row_adder(self, row1, row2, multi=1):
        """Add rows with an optional multiplication factor.

        Args:
            row1 (list): The first row to be added.
            row2 (list): The second row to be added.
            multi (float): A multiplication factor to apply to the second row (default is 1).

        Returns:
            list: The result of adding the rows.
        """
        sums = []
        for i, k in zip(row1, row2):
            sums.append(float(i) + float(multi * k))
        return sums

    def row_unity(self, row, element):
        """Normalize a row by dividing all elements by a common factor.

        Args:
            row (list): The row to be normalized.
            element (float): The common factor for normalization.

        Returns:
            list: The normalized row.
        """
        unity = []
        non_unit = row
        for i in non_unit:
            unity.append(float(i) / float(element))
        return unity

    def norm(self, mat_norm):
        """Normalize a matrix by making diagonal element's unity.

        Args:
            mat_norm (list): The matrix to be normalized.

        Returns:
            list: The normalized matrix.
        """
        nor = mat_norm
        for i in range(len(nor)):
            current_pivot = nor[i][i]
            nor[i] = self.row_unity(nor[i], current_pivot)
            self.iden_mat[i] = self.row_unity(self.iden_mat[i], current_pivot)
        return nor

    def returner(self):
        """Return the inverted matrix.

        Returns:
            list: The inverted matrix.
        """
        return self.iden_mat
