# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

lst = []

for i in range(20):
    lst.append(random.randint(-10, 11))
print(lst)
print(len(set(lst)))