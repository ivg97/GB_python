# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
#
#

class Matrix():

    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def __str__(self):
        print(f'-- matrix --')
        for line in self.list_matrix:
            line = str(line).replace('[', '|').replace(']', '|').replace(',', '')
            print(line)
        return f'Result matrix from {self.list_matrix}'





matrix_1 = Matrix([[1, 2, 3],[4, 3, 2],[7, 5, 5]])
print(matrix_1)
matrix_2 = Matrix([[1, 2],[4, 2],[7, 5]])
print(matrix_2)


