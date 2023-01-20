# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

f = open(r"C:\Users\79520\Desktop\GB\Python\Мороз и солнце.txt", 'r', encoding = 'utf=8')
s = f.read()

for i in s:
    text = list(filter(lambda x: 'абв' not in x, s.split()))
f.close()

with open(r"C:\Users\79520\Desktop\GB\Python\del абв.txt","w") as file:
    for j in text:
        file.write(j + ' ')
