# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    def logger(*args, **kwargs):
        ar = [i for i in args]
        kwar = [i for i in kwargs.values()]
        result = func(*args, **kwargs)
        if ar:
            for el_args in ar:
                print(f'{func.__name__}({el_args}: {type(el_args)})', end=', ')
        print('')
        if kwargs:
            for el_kwargs in kwar:
                print(f'{func.__name__}({el_kwargs}: {type(el_kwargs)})', end=', ')
        print('')
        for el in result:
            print(f'Result {func.__name__}({el}: {type(el)})')

        return
    return logger


@type_logger
def calc_number_one(x):
    return x ** 2,


@type_logger
def calc_number_two(x, y=0):
    return x ** 2, y ** 2


calc_number_one(3)
# calc_number_two(2, 5)
# calc_number_two(4, y=10) # именованные аргументы