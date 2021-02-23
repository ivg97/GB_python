# 3. Написать функцию thesaurus(),
# принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имен,
# а значения — списки, содержащие имена, начинающиеся с соответствующей
# буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Замечание: Заранее неизвестно сколько фамилий передадут в
# функцию thesaurus
# Подумайте: полезен ли будет вам оператор распаковки?
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus(*args):
    ''' return sorted dictionary and print simple dictionary '''
    name_dict = {}
    for i in args:
        if i[0] in name_dict.keys():
            name_dict[i[0]].append(i)
        else:
            name_dict[i[0]] = [i]
    print(name_dict)

#     Сортировка по ключам
    name_list = list(name_dict.keys())
    name_list.sort()
    sort_name_dict = dict()
    for i in name_list:
        sort_name_dict[i] = name_dict[i]

    return sort_name_dict

thesaurus("Иван", "Мария", "Петр", "Илья", "Иван", "Анастания", "Ольга")
