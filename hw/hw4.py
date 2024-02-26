# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и
# возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
#
from math import sqrt


def square(a):
    return (4 * a, a * a, a * sqrt(2))


print(square(5))


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов
# и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
def person(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

person(name='John', last_name='Smith', age=35, position='web developer')

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа
#
my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)

from functools import reduce
print(reduce(lambda x, y: x*y, my_list))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time

def count_execution_time(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        exec_time = end - start
        print(f'{func.__name__} execution time is: {exec_time}')
        return result
    return wrapper

@count_execution_time
def greeting(name):
    return f'Hello {name}!'
# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
from my_calc import *

prod_res = prod(100, 20)
print(prod_res)

div_res1 = divide(45, 9)
print(div_res1)

div_res2 = divide(5, 0)
print(div_res2)

add_res = add(585, 1987)
print(add_res)

remain_res = remain(541, 6)
print(remain_res)

sub_res = subtract(230, 149)
print(sub_res)