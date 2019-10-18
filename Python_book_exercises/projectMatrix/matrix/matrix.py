from find_lenght import find_lenght


class Matrix:

    def __init__(self, li):
        self.matrix = li

        if self.validate() == False:
            raise ValueError('Invalid dimension')

    def add(self, matrix_object):
        """adds two matrix and returns the sum"""
        first_matrix = self.matrix

        second_matrix = matrix_object.matrix

        # creating a three dimensional array
        matrix_sum = [[0 for _ in x] for x in first_matrix]

        for i in range(len(first_matrix)):
            for j in range(len(first_matrix)):
                matrix_sum[i][j] = first_matrix[i][j] + second_matrix[i][j]

        return matrix_sum

    def validate(self):

        lenght_of_value = None
        for value in self.matrix:
            if lenght_of_value is None:
                lenght_of_value = find_lenght(value)
            else:
                if lenght_of_value != find_lenght(value):
                    return False
        return True

    def __str__(self):
        if find_lenght(self.matrix[0]) == 0:
            return f'{self.matrix}'
        else:
            rep = 'Matrix => ['
            for a in self.matrix:
                rep += '['
                for b in a:
                    rep += str(b) + '  '
                rep = rep.strip()
                rep += ']\n'
            rep += ']'

            return rep

def main():
    pass

if __name__ == '__main__':
    main()