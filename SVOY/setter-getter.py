"""МЕХАНИЗМ ИНКАПСУЛЯЦИИ, СЕТТЕРЫ И ГАТТЕРЫ, ОГРАНИЧЕНИЕ ДОСТУПА К ДАННЫМ И МЕТОДАМ КЛАССА ИЗВНЕ"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(11, 22)  # к данным есть свободный ПОЛНЫЙ доступ
print(pt.x, pt.y)
""" ЕСЛИ ПОЛНЫЙ ДОСТУП ОПАСЕН, ТО НАДО ПОМЕТИТЬ ДАННЫЕ ЗАКРЫТЫМИ"""
""" ОДНО НИЖНЕЕ ПОДЧЕРКИВАНИЕ, ПЕРЕД ИМЕНЕМ ПЕРЕМЕННОЙ, НЕ БЛОКИРУЕТ ВОЗМОЖНОСТЬ ЕЕ ИЗМЕНЕНИЯ,
НО СООБЩАЕТ О ТОМ, ЧТО ЕЕ НЕЛЬЗЯ МЕНЯТЬ. ЭТО РЕЖИМ PROTECTED, СЛУЖИТ ДЛЯ ОБРАЩЕНИЯ ВНУТРИ КЛАССА И
ВО ВСЕХ ДОЧЕРНИХ КЛАССАХ"""


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(11, 22)
print(pt._x, pt._y)

"""ДВА НИЖНИХ ПОДЧЕРКИВАНИЯ - РЕЖИМ PRIVAT, СЛУЖИТ ДЛЯ ОБРАЩЕНИЯ, ТОЛЬКО ВНУТРИ КЛАССА"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    """ ЧТО БЫ ОБРАТИТЬСЯ К ЗАЩИЩЕННЫМ ЛОКАЛЬНЫМ АТРИБУТАМ (КОТОРЫЕ С 2 ПОДЧЕРКИВАНИЕМ), МОЖНО ИСПОЛЬЗОВАТЬ
    МЕТОДЫ set_coord и get_coord"""
    """ МЕТОДЫ, ПОЗВОЛЯЮЩИЕ ОБРАЩАТЬСЯ К ЛОКАЛЬНЫМ ДАННЫМ, НАЗЫВАЮТСЯ СЕТТЕРАМИ И ГЕТТЕРАМИ"""

    def set_cord(self, x, y):  # сначала создаем метод set_cord, с такими же атрибутами
        self.__x = x
        self.__y = y

    # потом создаем метод get_coord, который возвращает значения этих атрибутов.
    def get_coord(self):
        return self.__x, self.__y


pt = Point(11, 22)
# print(pt.__x, pt.__y)  # ТЕПЕРЬ ВНЕ КЛАССА, НЕТ ДОСТУПА К ПЕРЕМЕННЫМ x и y.
pt.set_cord(55, 88)
print(pt.get_coord())

"""ТЕПЕРЬ ДОБАВИМ В КЛАСС ПРИВАТНЫЙ МЕТОД, ДЛЯ ПРОВЕРКИ КОРРЕКТНОСТИ КООРДИНАТ (У ПРИВАТНЫХ МЕТОДОВ,
    ПЕРЕД ИМЕНЕМ, ТОЖЕ 2 НИЖНИХ ПОДЧЕРКИВАНИЯ"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod  # сделаем метод __chek_value, методом класса
    def __chek_value(cls, x):  # х -  координата, которую будем проверять
        return type(x) in (int, float)

    # далее в методе set_coord, вызовем этот метод __chek_value, которым проверили корректность координат

    """ ЧТО БЫ ОБРАТИТЬСЯ К ЗАЩИЩЕННЫМ ЛОКАЛЬНЫМ АТРИБУТАМ (КОТОРЫЕ С 2 ПОДЧЕРКИВАНИЕМ), МОЖНО ИСПОЛЬЗОВАТЬ
    МЕТОДЫ set_coord и get_coord"""
    """ МЕТОДЫ, ПОЗВОЛЯЮЩИЕ ОБРАЩАТЬСЯ К ЛОКАЛЬНЫМ ДАННЫМ, НАЗЫВАЮТСЯ СЕТТЕРАМИ И ГЕТТЕРАМИ"""

    def set_cord(self, x, y):  # сначала создаем метод set_cord, с такими же атрибутами
        if self.__chek_value(x) and self.__chek_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('КООРДИНАТЫ ДОЛЖНЫ БЫТЬ ЧИСЛАМИ')

            # потом создаем метод get_coord, который возвращает значения этих атрибутов.

    def get_coord(self):
        return self.__x, self.__y


pt = Point(11, 22)
# print(pt.__x, pt.__y)  # ТЕПЕРЬ ВНЕ КЛАССА, НЕТ ДОСТУПА К ПЕРЕМЕННЫМ x и y.
pt.set_cord(55, 88)
print(pt.get_coord())
