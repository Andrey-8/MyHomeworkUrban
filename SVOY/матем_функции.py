"""математические функции: abs, min, max, pow, round"""

from math import factorial

"""другие математические функции, можно импортировать, с помощью модуля
math, с помощью команды: import math"""
import math

"""модуль числа - преобразование отрицательных чисел, в положительные"""
d = -99
f = abs(d)  # abs - функция модуля числа
print(f)  # выход +99

""" функция min - вычисляет минимальное число, из переданных"""
a = (2, 4, 7, 4, -5, 6, -8, 11)
b = min(a)  # выход  -8

""" функция max - вычисляет максимальное число"""
s = (2, 4, 7, 4, -5, 6, -8, 11)
q = max(s)  # выход  11

"""функция pow, позволяет возводить числа в степень"""
w = pow(4, 2)  # будет возведена 4 в квадратную степень
print(w)  # выход 16

""" round - позволяет округлять числа к ближайшему целому"""
r = round(5.5)
t = round(8.3483, 2)  # можно указать 2-й аргумент, указать, сколько цифр оставить,
# после целого числа
y = round(67.987, -1)  # указав аргумент -1 = это округление до десятков,
# указав -2 = округление, до сотен
print(r)  # выход 6
print(t)  # выход 8.35
print(y)  # выход 70.0

"""все эти функции, можно вызывать и друг из друга"""
u = max(1, 3, abs(-8), -9)
print(u)  # выход 8

""" ceil - округление числа, до наибольшего целого"""
z = math.ceil(9.3)
print(z)  # на выходе 10

""" floor - округляет до наименьшего целого"""
math.floor(9.99)  # на выходе 9


"""factorial() - вычисляет факториал числа"""
math.factorial(5)  # на выходе 120

"""trunc - просто отбрасывает дробную часть"""
math.trunc(5.76)  # на выходе 5

"""log(9, 3) - вычислить логарифм (тут логарифм 3, что бы получить 9)
Логарифм числа в математике — это показатель степени, 
в которую нужно возвести основание, чтобы получить определённое число."""
print(math.log(25, 5))  # выход 2.0 (2 степень или 5 в квадрате)
