import tkinter as tk
#
# def get_values():
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     return num1, num2
#
#
# def insert_values(value):
#     answer_entry.delete(0, 'end')
#     answer_entry.insert(0, value)
#
#
# def add():
#     num1, num2 = get_values()
#     res = num1 + num2
#     insert_values(res)
#
#
# def sub():
#     num1, num2 = get_values()
#     res = num1 - num2
#     insert_values(res)
#
#
# def mul():
#     num1, num2 = get_values()
#     res = num1 * num2
#     insert_values(res)
#
# def div():
#     num1, num2 = get_values()
#     res = num1 / num2
#     insert_values(res)
#
#
# window = tk.Tk()
# window.title('калькулятор')
# window.geometry('400x500')
# window.resizable(False, False)
# button_add = tk.Button(window, text='+', width=5, height=3, command=add)
# button_add.place(x=100, y=350)
# button_sub = tk.Button(window, text='-', width=5, height=3, command=sub)
# button_sub.place(x=150, y=350)
# button_mul = tk.Button(window, text='*', width=5, height=3, command=mul)
# button_mul.place(x=200, y=350)
# button_div = tk.Button(window, text='/', width=5, height=3, command=div)
# button_div.place(x=250, y=350)
# number1_entry = tk.Entry(window, width=40)
# number1_entry.place(x=80, y=200)
# number2_entry = tk.Entry(window, width=40)
# number2_entry.place(x=80, y=250)
# answer_entry = tk.Entry(window, width=40)
# answer_entry.place(x=80, y=300)
# number1 = tk.Label(window, text='первое число:')
# number1.place(x=80, y=170)
# number2 = tk.Label(window, text='второе число:')
# number2.place(x=80, y=225)
# answer = tk.Label(window, text='ответ:')
# answer.place(x=80, y=275)
# window.mainloop()