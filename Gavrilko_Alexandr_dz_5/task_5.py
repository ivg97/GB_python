# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих
# элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Используйте генераторы или генераторные выражения.
# Сначала найдите способ определить уникальность элемента в списке.
# Подумайте о сохранении порядка исходного списка.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def inf(i, src):
    if src.count(i) == 1:
        return 1

result = [i for i in src if inf(i, src) == 1]
print(result)

# for i in src:
#     if i not in result:
#         result.append(i)
#     else:
#         src2.append(i)
# for i in result:
#     if i in src:
#         src.remove(i)
# for i in src:
#     if i in result:
#         result.remove(i)

