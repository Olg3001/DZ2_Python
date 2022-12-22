# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
# подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math

print('Program to find the positive integers fom their inputed sum and product.')

sum = int(input('First clue. Sum of two integers: '))
product = int(input('Second clue. Product of those integers: '))

if (sum <= 0 or product <= 0):
    print('Wrong inout. Input positive integers')

else:
    discriminant = sum * sum - 4 * product

    if (discriminant < 0):  print('There is no any solution.')
    else:
        number1 = int((sum + math.sqrt(discriminant)) / 2)
        number2 = int(sum - number1)

        if (product == number1 * number2):
            print(f'The numbers are {number1} and {number2}')
        else:
            print('There is no any solution.')