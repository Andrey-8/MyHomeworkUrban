"""МНОЖЕСТВА"""

import time

"""МНОЖЕСТВА НЕ МОГУЦ СОСТОЯТЬ ИЗ СПИСКОВ"""
"""В МНОЖЕСТВАХ НЕТ ИНДЕКСОВ И УПОРЯДОЧНОСТИ"""
"""МНОЖЕСТВА СОДЕРЖАТ ТОЛЬКО УНИКАЛЬНЫЕ ДАННЫЕ(ЗНАЧЕНИЯ НЕ ПОВТОРЯЮТСЯ)"""

t = {}  # если внести значения через запятую, то будет множество, иначе - словарь
y = set()

"""ЕЩЕ ОДИН МИНУС МНОЖЕТВА - ВЕС
ПРОВЕРИМ, ТАК ЛИ ЭТО, С ПОМОЩЬЮ ___sizeof__, КАКОЙ ТИП СКОЛЬКО ПАМЯТИ ЗАНИМАЕТ"""

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
d = {"1": 2, "3": 4, "5": 6, "7": 8, "9": 0}
f = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

print(a.__sizeof__())
print(s.__sizeof__())
print(d.__sizeof__())
print(f.__sizeof__())

"""НО В МНОЖЕСТВАХ, МОЖНО ГОРАЗДО БЫСТРЕЕ УДАЛИТЬ ДУБЛИРУЮЩИЕ ЗНАЧЕНИЯ (ЭЛЕМЕНТЫ)"""
"""НАПРИМЕР: """


# удаление дубликата из списка:
def f(*args):
    new_list = []
    for i in args:  # пробежимся по всем элементам списка args
        for y in i:  # проверим каждый элемент, из тех, что были в переборе выше
            if y not in new_list:  # если такого элемента нет в списке, то
                new_list.append(y)  # добавляем этот элемент в список
    return new_list  # после полного перебора и добавления, возвращаем готовый список


# есть несколько списков, значения в которых повторяются
q = list(range(10000))
a = list(range(5000, 15000))
z = list(range(10000, 20000))

# передаем эти списки в функцию f(), что бы создать один список с уникальными значениями
# без повторов элементов

start = time.time()
f(q, a, z)
stop = time.time() - start

# что бы засечь время, нужное для работы кода, импортируем модуль time (3-я строка кода)
# что бы засечь время выполения кода, перед функцией f(q, a, z), засекаем начало работы
# указав время старта: start =time.time()
# и после функции, высчитываем время на ее работу, отняв время окончания работы, от времени
# начала запуска функции: stop = time.time() - start
# и выводим на принт полученную разницу: stop (1.3880388736724854)
print(stop)

# теперь сделаем ту же операцию, с помощью множеств

start2 = time.time()  # начало времени операции
r = set(q)  # создаем переменную в которую в виде множества передаем список q
# далее объединяем множество из переменной r, с множествами в преобразованных в множества
# списках a и z, с помощью команды .union()
t = r.union(set(a), set(z))
stop2 = time.time() - start2  # высчитываем время на работу кода (0.0009925365447)
print(stop2)
