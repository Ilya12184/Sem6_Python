# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

N = int(input('Введите количество друзей: '))
friends = dict()

for i in range(N):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    friends[name] = age
minim = sorted(friends.items(), key=lambda item: item[1])
print(minim[0][0])