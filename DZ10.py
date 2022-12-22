# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
#  были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

print('Programm to count the minimum coins quantity to be turned over to see the same side on all the coins')

n = int(input('Input the coins quantity: '))
m = []
count0 = 0
count1 = 0

for i in range(0, n):

        randomNumber = round(random.randint(0, 1))
        m.append(randomNumber)

        if m[i] == 0:
            count0 += 1
        if m[i] == 1:
           count1 += 1

print(m)

if count0 > count1:
    print(f'The minimum coins quantity to turn over: {count1}')

if count0 <= count1:
    print(f'The minimum coins quantity to turn over: {count0}')