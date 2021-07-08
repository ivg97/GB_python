# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroExeptionNew(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


data = input('Enter value: ')

try:
    result = int(data)
    if result == 0:
        raise ZeroExeptionNew(f'Error: {ZeroExeptionNew.__name__} ->  /0 no')
except ZeroExeptionNew as error:
    print(error)

