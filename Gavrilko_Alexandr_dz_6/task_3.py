# 3. Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении данных используется
# принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# то для оставшихся ФИО значение в словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из
# скрипта с кодом «1». Примечание: При решении задачи считать, что объём
# данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи

def user_hobby():
    result = {}
    content_user = []
    content_hobby = []

    with open('users.csv', encoding='utf-8') as us:
        with open('hobby.csv', encoding='utf-8') as hob:
            for line in us:
                line = [i for i in line.strip().split(',')]
                content_user.append(line)
            for line in hob:
                line = [i for i in line.strip().split(',')]
                content_hobby.append(line)

    if len(content_user) >= len(content_hobby):
        for i in range(0, len(content_hobby)):
            result[tuple(content_user[i])] = content_hobby[i]
        for i in range(len(content_hobby), len(content_user)):
            result[tuple(content_user[i])] = None
        print(result)
    else:
        for i in range(len(content_user)):
            result[tuple(content_user[i])] = content_hobby[i]
        print(result)
        return 1


print(user_hobby())