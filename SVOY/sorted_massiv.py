"""В этом ката вам будет дана последовательность измерений прямоугольников
(последовательность с указанием ширины и длины) и
окружностей (радиус - просто число).
Ваша задача - вернуть новую последовательность измерений,
отсортированную по возрастанию площади."""

def sort_by_area(seq):
    def func(x):
        if isinstance(x, tuple): # если кортеж, то площадь = длина * ширина
            return x[0] * x[1]
        else:
            return 3.14 * x * x # если не кортеж, то вычисляем площадь круга
    print(sorted(seq, key=func))

             # прямоугольник,круг,круг, прямоугольник
sort_by_area([(4.23, 6.43), 1.23, 3.444, (1.342, 3.212)])