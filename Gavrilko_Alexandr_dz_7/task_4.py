# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых
# не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os

work_dir = os.getcwd() + '/some_data'
dict_some_data = {}
count_10 = 0
count_100 = 0
count_1000 = 0
count_10000 = 0
count_100000 = 0
count_1000000 = 0

for root, dirs, files in os.walk(work_dir):
    for file in files:
        dir_file = os.path.join(work_dir, file)
        size = os.path.getsize(dir_file)

        if size <= 10:
            count_10 += 1
            dict_some_data[10] = count_10
        elif 10 < size <= 100:
            count_100 += 1
            dict_some_data[100] = count_100
        elif 100 < size <= 1000:
            count_1000 += 1
            dict_some_data[1000] = count_1000
        elif 1000 < size <= 10000:
            count_10000 += 1
            dict_some_data[10000] = count_10000
        elif 10000 < size <= 100000:
            count_100000 += 1
            dict_some_data[100000] = count_100000
        elif 100000 < size <= 1000000:
            count_1000000 += 1
            dict_some_data[1000000] = count_1000000
print(dict_some_data)





