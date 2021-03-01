# 4. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных
# и для вывода на экран записанных данных.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# При записи передавать из командной строки значение суммы продаж.
# Новая запись дозаписывается в конец файла.
# Для чтения данных реализовать в командной строке следующую логику.
# Предполагаем, что первая запись имеет номер 1.
# 1) просто запуск скрипта — выводить все записи;
# 2) запуск скрипта с одним параметром-числом — выводить все записи с номера,
# равного этому числу, до конца;
# 3) запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно;
#
# Примеры запуска скриптов:
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
# Усложнение Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

def write_sale(argv):
    total, *argv = argv
    line_count = 0
    with open('bakery.csv', encoding='utf-8') as f:
        content = f.read()
        f.close()
    count = content.count('\n')
    with open('bakery.csv', encoding='utf-8') as f:
        if len(argv) == 1:
            for line in f:
                if count >= line_count >= int(argv[0]) - 1:
                    print(line.strip())
                else:
                    line_count += 1
        elif len(argv) == 2:
            for line in f:
                line_count += 1
                if int(argv[1]) >= line_count >= int(argv[0]):
                    print(line.strip())
                else:
                    break
        elif not argv:
            print(content)

if __name__ == '__main__':
    import sys
    exit(write_sale(sys.argv))