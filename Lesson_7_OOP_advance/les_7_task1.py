# 1. Реализовать класс Matrix (матрица).


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        result = [[0 for x in self.my_list] for y in self.my_list]
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[0])):
                result[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix(result)

    def __str__(self):
        str_view = ""
        for row in self.my_list:
            for column in row:
                str_view = str_view + str(column) + (abs(5 - len(str(column))) * " ")
            str_view = str_view + "\n"
        return str_view


matrix_1 = Matrix([[3, 5, 32], [2, 4, 16], [-1, 64, -8]])
matrix_2 = Matrix([[7, 0, 10], [0, 0, 1], [-5, -42, 40]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
