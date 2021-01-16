import sqlite3 as sql
import SQLfunks
from tkinter import *
import re

# Создаем главный объект (по сути окно приложения)
root = Tk()


def sum_month(sum_year, sum_month):
    if sum_year == "":
        return 'Введите год'
    if len(sum_year) != 4:
        return 'Введите год'
    if sum_month == '':
        return 'Введите месяц'
    if len(sum_month) == 1:
        m = list(sum_month)
        m.insert(0, '0')
        sum_month = ''.join(m)
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        y_m = f'{sum_year.strip()}_{sum_month.strip()}'
        a = cur.execute(f"SELECT SUM(total_transfer) from transfer where year_month='{y_m}'")
        a = list(a)[0][0]
    if a:
        return round(a, 2)
    else:
        return 'Отсуствуют платежи\n за выбранный месяц'


# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"


def get_sum():
    # Полученные данные добавляем в текстовую надпись для отображения пользователю

    info['text'] = sum_month(yearField.get(), monthField.get())


def clean():
    nameField.delete(0, END)
    nameField.insert(0, "")
    surnameField.delete(0, END)
    surnameField.insert(0, "")
    cityField.delete(0, END)
    cityField.insert(0, "")
    emailField.delete(0, END)
    emailField.insert(0, "")


def res_add(res_name, res_surname, res_city, res_email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if any(map(str.isdigit, res_name)) or len(res_name) <= 3:
        return 'Введите корректоное имя'
    if any(map(str.isdigit, res_surname)) or len(res_surname) <= 3:
        return 'Введите фамилию'
    if any(map(str.isdigit, res_city)) or len(res_city) <= 3:
        return 'Введите город'
    if re.search(regex, res_email):
        SQLfunks.create_client(res_name, res_surname, res_city, res_email)
        clean()
        return 'добавлен в бд'
    else:
        return 'Неправильная почта'


def add_client():
    add_name = nameField.get()
    add_surname = surnameField.get()
    add_city = cityField.get()
    add_email = emailField.get()
    added['text'] = res_add(add_name, add_surname, add_city, add_email)


# Настройки главного окна

# Указываем фоновый цвет
# root['bg'] = '#ffffff'
# Указываем название окна
root.title('Тест БД')
# Указываем размеры окна
root.geometry('800x900')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка

# Для суммы за месяц
year = Label(text='Введите год', font=40)
year.grid(row=0, column=0, sticky=W)

yearField = Entry(bg='white', font=20)
yearField.grid(row=0, column=1, padx=10)

month = Label(text='Введите месяц', font=40)
month.grid(row=1, column=0, sticky=W)

monthField = Entry(bg='white', font=30)
monthField.grid(row=1, column=1)

btn = Button(text='Вычислить сумму', command=get_sum)
btn.grid(row=2, column=0, sticky=W, pady=5)

info = Label(text='Сумма за месяц', font=40)
info.grid(row=2, column=1, sticky=E + W)

name = Label(text='Введите имя', font=40)
name.grid(row=6, column=0, sticky=W)

nameField = Entry(bg='white', font=20)
nameField.grid(row=6, column=1, padx=10)

surname = Label(text='Введите фамилию', font=40)
surname.grid(row=7, column=0, sticky=W)

surnameField = Entry(bg='white', font=30)
surnameField.grid(row=7, column=1)

city = Label(text='Введите город', font=40)
city.grid(row=8, column=0, sticky=W)

cityField = Entry(bg='white', font=30)
cityField.grid(row=8, column=1)

email = Label(text='Введите почту', font=40)
email.grid(row=9, column=0, sticky=W)

emailField = Entry(bg='white', font=30)
emailField.grid(row=9, column=1)

btn_add_client = Button(text='Добавить клиента', command=add_client)
btn_add_client.grid(row=10, column=0, sticky=W, pady=5)

added = Label(text='', font=40)
added.grid(row=10, column=1, pady=5)

root.mainloop()
