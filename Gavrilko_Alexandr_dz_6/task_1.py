# 1. Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.
#
# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Примечание:
# - Уверены ли вы, что максимальное кол-во запросов - уникально? Т.е. найденный спамер - только один?
# Или таких спамеров может быть несколько?

from time import perf_counter
start = perf_counter()
requests_addr_type_resource = list()
ip_list = list()
ip = {}

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        response_line = tuple([line[0], line[5].replace('"',''), line[6]])
        ip_list.append(line[0])
        requests_addr_type_resource.append(response_line)



for i in ip_list:
    ip_count = ip_list.count(i)
    ip[ip_count] = i
max_count = max(ip.keys())
print(f'{requests_addr_type_resource}')
print(f'Список кортежей - ^')
print(f'Спамер - {ip[max_count]}')
print(f'Затраченное время - {perf_counter()-start}')




