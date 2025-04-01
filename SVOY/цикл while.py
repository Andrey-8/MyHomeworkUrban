"""цикл while"""

# вычислим сумму чисел (количество чисел будет любое)

n = int(input('введите число: ')) # максимальное число
s = 0 # сумма чисел
i = 1 # переменная для перебора всех чисел

# цикл выполняется, пока и 1 и 2 условия верны.Как только 1 условие не верно, цикл прекращается.
while i <= n and i <= 500: # условие цикла (заголовок цикла)
    # операторы цикла (тело цикла)
    s += i # каждый цикл прибавляем следующее число к предыдущей сумме чисел
    i += 1 # каждый цикл, переходим к следующему числу(можно сделать сумму нечетных чисел, если прибавлять 2)
print(s)

"""2 пример"""

# нужно ввести верный пароль

pass_true = 'qwerty' # реальный пароль
ps = '' # переменная, в которую пользователь будет вводить пароль для входа

# цикл проверки, верно ли введен пароль

while ps != pass_true: # пользователь будет вводить пароль, до тех пор, пока не угадает реальный пароль
    ps = input('введите пароль: ')
print('введен верный пароль.')

'''третий пример - вывести на экран числа, кратные трем'''

n = int(input('введите число: ')) # введите число
i = 1 # переменная для перебора всех чисел

while i <= n: # перебор пока i меньше или равна n
    # проверим, кратно число 3 или нет
    if i % 3 ==0:
        print(i) # кратные 3, выводим на экран

    i += 1 # увеличиваем i для каждого цикла
