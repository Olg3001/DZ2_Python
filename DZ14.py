# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), 
# не превосходящие числа N.
# 5 => 1 2 4
# 17 => 1 2 4 8 16

print('Programm to find integer power for number 2 not being in access of number N.')

n = int(input('Input number N: '))

if n < 1:
    print('Wrong input. Input number > 1.')

else:    
    result = 1

    while result <= n:
        degree = 0    
        print(result, end = ' ')
        degree += 1
        result *= 2 ** degree