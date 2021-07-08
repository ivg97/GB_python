# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например,
#
#         месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

from datetime import date
class Date:
    def __init__(self, dates):
        self.dates = dates

    @classmethod
    def transform_in_int(crs, dt):
        date_list = dt.split('-')
        return [int(i) for i in date_list]

    @staticmethod
    def validator_date(dt):
        dt = Date.transform_in_int(dt)
        day, month, year = dt[0], dt[1], dt[2]
        if 0 < month <= 12:
            if 0 < day <= 31:
                if len(str(year)) == 4 and year <= int(date.today().strftime('%Y')):

                    return f'{dt} -> {True}'


print(Date.transform_in_int('21-03-2021'))
print(Date.validator_date('21-03-2021'))