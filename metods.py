# x = [9, 8, 7, 6, 5]
# x.append(11)  # ДОБАВЛЯЕТ ЭЛЕМЕНТ В КОНЕЦ СПИСКА
# x.insert(1, 2)  # добавляет эл-т по индексу 1- индекс, куда вставить, 2- объект вставки
# print(x.count(9))  # показывает кол-во одинаковых элементов в списке (тут одна 9)
# x.sort()  # сортирует список по возрастанию
# x.reverse()  # обратная сортировка
# y = x.pop(
#     0
# )  # удаляет эл-т по индексу, если не указать индекс, то удаляет последний эл-т в списке
# # но сохраняет удаленный эл-т в переменной (Y)
# x.remove(2)  # удаляет 1 указанный элемент (2)
# x.clear()  # очищает список полностью
# x.extend(["a", "s", "d"])  # добавляет в конец списка значения из другого списка
# h = x.copy()  # копирует список в другую переменную
#
# print(x)
# print(y)
# print(h)

"""сделаем из списка чисел 2 списка 1-с четными, 2- с нечетными числами, сохранив первоначальный
список в другой переменной"""
n = list(range(1, 21))
b = n.copy()  # сохраняем список в новой переменной
m = []  # создаем пустой список, куда будут вводится новые элементы
for i in n:  # перебираем первоначальный список
    if i % 2 == 0:  # если число в переменной i равно 0 (четное)
        m.append(i)  # то добавляем это число в список m
        n.remove(i)  # одновременно удаляя это число из списка n
else:
    print(m)
    print(n)
print(b)

""" все это можно было просто сделать с помощью метода срезов b = n[старт:стоп:шаг]:
n = list(range(1, 21))
b = n[::] - тут копируется список со всеми эл-тами
b = n[::2] - тут копируются только нечетные эл-ты
b = n[1::2] - тут копируются только четные эл-ты"""
