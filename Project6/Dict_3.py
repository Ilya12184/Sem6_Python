# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст)
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

N = int(input('Введите количество друзей: '))
friends = dict()

for i in range(N):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    friends[name] = age

summ = 0
maxim = 0

for k, v in friends.items():
    summ += v
    if len(k) > maxim:
        maxim = len(k)
        name = k
print(round(summ/N, 2))
print(name)