# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор. Например:
# gen1 = iterator_without_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
num = 11
generate = (i for i in range(1, num + 1, 2))
print(next(generate)) # 1
print(next(generate)) # 3
print(next(generate)) # 5
print(next(generate)) # 7
print(next(generate)) # 9
print(next(generate)) # 11
print(next(generate)) # StopIteration