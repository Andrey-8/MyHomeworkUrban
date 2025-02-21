""" СТАТИЧЕСКИЕ МЕТОДЫ (@staticmethod)
 И МЕТОДЫ КЛАССА (@classmethod)"""


class Vector:
    # сначала добавим 2 атрибута класса Vector
    MIN_COORD = 0
    MAX_COORD = 100

    """МЕТОД КЛАССА, РАБОТАЕТ ТОЛЬКО С АТРИБУТАМИ ЭТОГО КЛАССА, НО НЕ МОЖЕТ ОБРАЩАТЬСЯ
    К ЛОКАЛЬНЫМ АТРИБУТАМ ЭКЗЕМПЛЯРОВ КЛАССА, потому что в классе def validate(cls, arg)
    нет ссылки на экземпляр класса, есть только ссылка на сам класс"""

    # теперь объявим метод класса
    # более того, мы можем вызвать метод (функцию) def validate(cls, arg), можем
    # вызвать прямо через класс Vector (см.ниже Vector.validate(50))
    @classmethod
    # а теперь объявим метод (свое название, cls - само встанет)
    def validate(cls, arg):  # пропишем параметр "arg", эта функция, просто для проверки
        # и проверим, если "arg" больше MIN_COORD и меньше MIN_COORD,
        # то вернем значение True
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    # теперь используем метод класса validate, внутри метода def __init__(self, x, y),
    # для проверки корректности координат x, y
    # для этого, сначала пропишем что x, y равны 0
    # а затем проверим их корректность, вызвав метод validateБ используя self
    # можно написать if Vector.validate(x) and Vector.validate(y):,
    # но если потом изменится имя класса, то будет ошибка
    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            # если проверка прошла, то значения меняем (в экземпляре класса),
            # если проверка не прошла, то значения останутся равными 0
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    """СТАТИЧЕСКИЕ МЕТОДЫ (@staticmethod) - определяет методы, которые не имеют доступ
     ни к атрибутам класса, ни к атрибутам его экземпляров. Значит создается независимая
     самостоятельная функция, внутри класса"""

    @staticmethod
    # например тут вычислим квадратичную норму какого-то вектора
    # с координатами (x, y)
    def norm2(x, y):
        return x * x + y * y


v = Vector(11, 22)  # создаем экземпляр класса
print(Vector.validate(50))  # вызов метода validate (см.выше)
print(v.norm2(9, 8))  # использовали функцию def norm2(x, y)
rezultat = v.get_coord()
print(rezultat)
