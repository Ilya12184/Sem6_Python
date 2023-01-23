# "Пора учить английский язык", - сказал себе Степа и решил написать программу
# для изучения английского языка. Программа получает на вход слово на английском языке
# и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово,
# а значение - это список русских слов. В этой задаче нужно использовать строчный метод split().

N = int(input('Введите количество слов: '))
Dictionary = dict()

for i in range(N):
    k, v = input('Введите слово на англ: '), input('Введите всевозможные переводы на русском: ').split(', ')
    Dictionary[k] = v
print(Dictionary)