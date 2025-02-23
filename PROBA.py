# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
# file_names в виде списка или кортежа.

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names  # неограниченного количество названий файлов file_names в виде списка

    # Также объект класса WordsFinder должен обладать следующими методами:
    # get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    # Где:
    # 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    # ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
    # Алгоритм получения словаря такого вида в методе get_all_words:
    # Создайте пустой словарь all_words.
    # Переберите названия файлов и открывайте каждый из них, используя оператор with.
    # Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':',' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
    # Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    # В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names: # Переберите названия файлов
            with open(file_name, 'r', encoding='utf-8') as file: # открывайте каждый из них, используя оператор with
                for words in file:
                    words = file.read().lower() # каждого файла считывайте единые строки, переводя их в нижний регистр
                    for punct in [',', '.', '=', '!', '?', ';', ':',' - ']:
                        words = words.replace(punct, '') # избавляемся от всей пунктуации
                words = words.split() # Разбейте эту строку на элементы списка методом split()
    # for name, words in get_all_words().items():
        
                return all_words

    

# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция
# первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

# for name, words in get_all_words().items():
    # Логика методов find или count


# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:
# It's a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего



========================================================================================================================

# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
# file_names в виде списка или кортежа.
# from os.path import split


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = [*file_names]  # неограниченного количество названий файлов file_names в виде списка

    # Также объект класса WordsFinder должен обладать следующими методами:
    # get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    # Где:
    # 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    # ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
    # Алгоритм получения словаря такого вида в методе get_all_words:
    # Создайте пустой словарь all_words.
    # Переберите названия файлов и открывайте каждый из них, используя оператор with.
    # Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':',' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
    # Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    # В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.


    def get_all_words(self, file_name):
        all_words = {}
        string_punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(file_name, 'r', encoding='utf-8') as open_file:
            for string in open_file:
                string = string.lower()
                for p in string_punkt:
                    if p in string:
                        string = string.replace(p, '')
                split_string = string.split(sep='')
                all_words.append(split_string[:])
                return all_words

    def find(self, word):
        dict_ = self.get_all_words
        key = self.file_names
        count = 0
        for name, words in get_all_words().items():





# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция
# первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

# for name, words in get_all_words().items():
    # Логика методов find или count


# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:
# It's a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
