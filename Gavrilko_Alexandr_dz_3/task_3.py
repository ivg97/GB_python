# 5. Реализовать функцию get_jokes(),
# возвращающую n шуток, сформированных из двух случайных слов,
# взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Усложнение: * Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
from random import choice

def get_jokes(quantity, flag=True):
    ''' return n joke '''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if quantity > min(len(nouns), len(adverbs), len(adjectives)):
        error = f'Данное количество шуток не может быть сгенерировано'
        return error

    return_jokes = list()
    if flag:
        for i in range(0, quantity):
            joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            return_jokes.append(joke)
        return return_jokes

    nouns_flag = nouns.copy()
    adverbs_flag = adverbs.copy()
    adjectives_flag = adjectives.copy()
    for i in range(0, quantity):
        rand_nouns, rand_adverbs, rand_adjective = choice(nouns_flag), \
                                                   choice(adverbs_flag), \
                                                   choice(adjectives_flag)
        joke = f'{rand_nouns} {rand_adverbs} {rand_adjective}'
        nouns_flag.remove(rand_nouns)
        adverbs_flag.remove(rand_adverbs)
        adjectives_flag.remove(rand_adjective)
        return_jokes.append(joke)
    return return_jokes





print(get_jokes(5, False)) # 5 шуток без повтороения
print(get_jokes(6, False)) # Нельзя сделать 6 шуток без посторений
print(get_jokes(3)) # 3 шутки с повторением слов
print(get_jokes(35)) # 35 шуток с повторением слов