# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_Number():
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self):
        return self.number_1 + self.number_2

    def __mul__(self):
        return self.number_1 * self.number_2




num_1 = Complex_Number(2 + 3j, 4 + 5j)
print(num_1.__add__())
print(num_1.__mul__())
