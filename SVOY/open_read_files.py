import os

# 'r' - открыть для чтения (по умолчанию)
# 't' - открыть в текстовом режиме (по умолчанию)
# 'w' - открыть в режиме перезаписи, если файла нет, создается новый
# 'a' - открыть для дозаписи в конец содержимого, если файла нет, создается новый
# 'b' - открыть в бинарном режиме
# '+' - открыть для чтения и записи 'r+', 'w+', 'a+'

# функция walk принимает один обязательный аргумент — имя каталога и выдает кортеж,
# где 3 элемента: 1 - строка(путь), 2 - список с именами папок
# и 3 - список имен файлов, которые есть по данному адресу

# Функция join() в Python используется для объединения списка строк в одну строку
# с использованием указанного разделителя.
# разделитель.join(список_строк)

# Функция Path в Python относится к модулю pathlib, который позволяет
# взаимодействовать с файловой системой.

# Для записи в файл в Python используется функция write(). В качестве аргумента
# ей следует передать строку, содержимое которой будет записано.

"""РАБОТА В ТЕКСТОВОМ РЕЖИМЕ"""
list_paths = []

for adress, papka, file in os.walk("D:\\Музыка"):
    for i in file:
        full_path = os.path.join(adress, i)
        list_paths.append(full_path)

# если файл "text.txt", там же, где код для запуска, то путь к нему не указываем
r = open("text.txt", "w", encoding="utf-8")
r.write("новая строка текста")
r.close()
r = open("text.txt", encoding="utf-8")
u = r.read()
# print(u)
r.close()
r = open("text.txt", "w", encoding="utf-8")

# мы решили записать весь массив файлов и адресов к ним "os.walk("D:\\")"
# в текстовый файл text.txt
# записать можно только используя тип данных СТРОКА, а у нас СПИСОК (list_paths = [])
# значит пройдемся по списку, при помощи for x in list_paths:

for x in list_paths:
    # каждую сработку цикла, один путь будет добавляться в файл
    # что бы разделить строки, укажем разделитель строки (перенос) + "\n"
    r.write(x + "\n")
r.close()

# просто прочитаем файл и даже выведем через принт
r = open("text.txt", encoding="utf-8")
file = r.read()
# print(file)
r.close()

# просмотрим список файлов с расширением мр3
# r = open("text.txt", encoding="utf-8")
# for i in r:
#     if ".mp3" in i:
#         print(i)
# r.close()

""" РАБОТА В БИНАРНОМ РЕЖИМЕ"""
# позволяет читать и записывать бинарные файлы
# Бинарный файл — это набор данных, закодированных в биты в виде нулей и единиц.
# Эти биты собираются в байты, а уже из них складывается содержимое файла, который
# может быть представлен в виде текста, изображения, музыки, видео или даже исполняемой программы

r = open("game.exe", "rb")  # прочитать в бинарном режиме

# работать с бинарным кодом мы не можем, потому создадим копию файла
y = open("копия game.exe", "wb")

# для последовательного считывания содержимого файла (вдруг объем большой),
# напишем цикл while
while True:
    # создаем переменную, куда будут считываться данные, по 1 мб за проход (1048576 байт)
    var = r.read(1048576)
    # посмотрим содержимое файла и размер содержимого __sizeof__()
    print(var.__sizeof__())

    # цикл будет бесконечно показывать размер файла, так что укажем прерывание цикла
    if var.__sizeof__() == 33:
        break

    # теперь записываем содержимое файла и созданную копию
    y.write(var)

print("КОНТРОЛ")

r.close()
y.close()
