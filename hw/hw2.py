"""Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре. 
Если оно равно или меньше нуля, выведите на экран False, в противном случае True."""

# health = int(input("Какой уровень здоровья у персонажа? "))
# if health <= 0:
#     print('False')
# else:
#     print('True')

"""Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. 
Если да, выведите на экран текст 'Четное', а иначе - 'Нечетное' """

# number = int(input('Введи число: '))
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

"""Задание 2.3
Напишите программу, которая проверяет является ли год високосным. 
Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) 
и не являются столетиями (500, 600). Однако, если год делится без остатка  
на 400, он также считается високосным (1200, 2000)
"""

# year = int(input('Введите год: '))
# if (year % 4 == 0) | (year % 400 == 0):
#     print('Високосный год')
# elif (year % 4 != 0) | (year % 100 == 0):
#     print('Невисокосный год')

"""Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, 
построчно. Текст и количество повторений нужно ввести с помощью input()"""

# txt = input('введите текст: ')
# count = int(input('введите количество повторений: '))
# print((txt + '\n') * count)

"""Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор 
(в формате str), производит заданное арифметическое действие и печатает 
результат в формате: {num1} {operator) {num2) = {result}"""

num1 = int(input('введите 1-е число: '))
num2 = int(input('введите 2-е число: '))
operator = input('введите оператор: ')

if operator == '+':
    print(f'{num1} {operator} {num2} = ', num1 + num2)
if operator == '-':
    print(f'{num1} {operator} {num2} = ', num1 - num2)
if operator == '*':
    print(f'{num1} {operator} {num2} = ', num1 * num2)
if operator == '/':
    print(f'{num1} {operator} {num2} = ', num1 / num2)