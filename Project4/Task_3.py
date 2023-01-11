# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

sequence = list(map(int, input().split()))
lst = []

for i in range(len(sequence)):
    if sequence[i] not in lst:
        lst.append(sequence[i])
print(lst)