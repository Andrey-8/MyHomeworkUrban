class Student:
    # В ИНИЦИАЛИЗАТОР КЛАССА, ПЕРЕДАЕМ ДВА ПАРАМЕТРА ИМЯ СТУДЕНТА (name) И
    # СПИСОК ЕГО ОЦЕНОК (marks)
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
        
    # ЧТО БЫ ОБРАЩАТЬСЯ К ЗНАЧЕНИЯМ ОБЪЕКТА КЛАССА НАПРЯМУЮ, НЕ УКАЗЫВАЯ
    # КАЖДЫЙ РАЗ ПАРАМЕТР, А ПРОСТО УКАЗАВ ИНДЕКС, ИСПОЛЬЗУЕМ МЕТОД __getitem__
    # ключ из индекса, будет передаваться в параметр item, метода __getitem__
    def __getitem__(self, item):
        
        # УКАЗЫВАЕМ, ЧТО ЗНАЧЕНИЕ ИНДЕКСА НЕ ДОЛЖНО БЫТЬ БОЛЬШЕ СУЩЕСТВУЮЩЕГО
        # КОЛИЧЕСТВА ИНДЕКСОВ В СПИСКЕ ОЦЕНОК
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            return ('НЕВЕРНЫЙ ИНДЕКС')
        
    # ЧТО БЫ МЕНЯТЬ ОЦЕНКИ СТУДЕНТА, ТАК ЖЕ ПРОСТО ИСПОЛЬЗУЯ ИНДЕКС,
    # ИСПОЛЬЗУЕМ МЕТОД __setitem__
    # key - ЭТО ИНДЕКС, value - ЭТО БУДУЩАЯ НОВАЯ ОЦЕНКА
    def __setitem__(self, key, value):
        # СНАЧАЛА ПРОВЕРИМ, ЯВЛЯЕТСЯ ЛИ ИНДЕКС, ЦЕЛЫМ ПОЛОЖИТЕЛЬНЫМ ЗНАЧЕНИЕМ (int)
        if not isinstance(key, int) or key < 0:
            raise TypeError ('ИНДЕКС ДОЛЖЕН БЫТЬ ЦЕЛЫМ ПОЛОЖИТЕЛЬНЫМ ЧИСЛОМ')
        
        # ПРОВЕРИМ, ЕСТЬ ЛИ ТАКОЙ ИНДЕКС, ДЛЯ СМЕНЫ ОЦЕНКИ
        if key >= len(self.marks):
            # ЕСЛИ ЗНАЧЕНИЕ key (ИНДЕКС НОВОЙ ОЦЕНКИ), БОЛЬШЕ ЛИБО РАВЕН
            # ДЛИНЕ НАШЕГО СПИСКА (self.marks), ТО 1- ВЫЧИСЛЯЕМ, СКОЛЬКО ЭЛЕМЕНТОВ
            # НУЖНО ДОБАВИТЬ В СПИСОК (self.marks) СОЗДАДИМ ВРЕМЕННУЮ ПЕРЕМЕННУЮ
            # (off = key + 1 - len(self.marks), А ПОТОМ РАСШИРИМ СПИСОК ОЦЕНОК
            # (self.marks), С ПОМОЩЬЮ МЕТОДА extend - это метод списка, в нем укажем
            # ЧТО БУДЕМ РАСШИРЯТЬ СПИСОК НА (off) количество неизвестных
            # элементов (None)
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
                                
            
        self.marks[key] = value
        
        # МЕТОД __delitem__, ВЫЗЫВАЕТСЯ ДЛЯ УДАЛЕНИЕ ЭЛЕМЕНТА ПО ИНДЕКСУ
    def __delitem__(self, key):
        
        # ПРОВЕРЯЕМ ЧТО КЛЮЧ, ЯВЛЯЕТСЯ ЦЕЛЫМ ЗНАЧЕНИЕМ
        if not isinstance(key, int):
            raise TypeError ('ИНДЕКС ДОЛЖЕН БЫТЬ ЦЕЛЫМ ЧИСЛОМ')
        
        # ТЕПЕРЬ ПИШЕМ УДАЛЕНИЕ ИЗ СПИСКА ОЦЕНОК (self.marks), НУЖНЫЙ ЭЛЕМЕНТ
        del self.marks[key]
        
        
# СОЗДАЕМ ОБЪЕКТ КЛАССА
s1 = Student('Andrey', [3, 3, 4, 3, 5, 3])
s1[8] = 2  # ПРОПИСАЛИ НОВУЮ ОЦЕНКУ ПО ИНДЕКСУ 8
print(s1[5]) # ВЫВОД ОЦЕНКИ ПО ИНДЕКСУ
del s1[3] # указываем, какую оценку удалить
print(s1.marks) # ВЫВОД ВСЕГО СПИСКА ОЦЕНОК
        
        
        
