# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
#
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
#
# В Domain part обязательно должна быть хотя бы одна точка.
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл
# в данном случае использовать функцию re.compile()?

import re


# \w+@\w+.\w{2,6}|[a-zA-z0-9]+.[a-zA-Z0-9]+@\w+.\w{2,6}
def email_parse(email_address):
    """  """
    re_user = re.compile(r"[A-Za-z0-9_*.-/'+]+@")
    re_domain = re.compile(r"@[a-zA-Z0-9.-]+.[a-zA-Z]{2,6}$")
    name = re.findall(re_user, email_address)
    domain = re.findall(re_domain, email_address)
    if not name or not domain:
        message = f'wrong email: {email_address}'
        raise ValueError(message)


    result = {'username': name[0].replace('@', ''), 'domain': domain[0].replace('@', '')}
    return result

print(email_parse('someone@geekbrains.ru'))
print(email_parse("example-'0'.1_+@example-1.com"))