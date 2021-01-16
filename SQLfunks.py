import sqlite3 as sql
import datetime
from random import randint, uniform
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


def create_databases():
    """Создание трех таблиц"""
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS clients (client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(30),surname VARCHAR(30),INN VARCHAR(12),city VARCHAR(45), email VARCHAR(50))""")

        cur.execute("""CREATE TABLE IF NOT EXISTS invoice  (invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    invoice VARCHAR(20),bank_name VARCHAR(225), city VARCHAR(45), BIK VARCHAR(9),
                    CUSTOMER_ID VARCHAR references clients(client_inn))""")

        cur.execute("""CREATE TABLE IF NOT EXISTS transfer (transfer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_formation DATETIME  NOT NULL , debit_account VARCHAR(20),credit_account VARCHAR(20), 
                      total_transfer FLOAT,year_month TEXT)""")


def create_transfer(debit_account, credit_account, total_transfer):
    """добавлние значений в Проводок"""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    year_month = datetime.datetime.now().strftime("%Y_%m")
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO transfer (transfer_id, date_formation,"
                    " debit_account,credit_account,total_transfer,year_month) VALUES (null,?,?,?,?,?)",
                    (date, debit_account, credit_account, total_transfer, year_month))
    db.commit()


def create_client(name, surname,inn, city, email):
    """Создание клиента"""
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO clients (client_id,name, surname,inn, city,email) VALUES (null,?,?,?,?,?)",
                    (name, surname,inn, city, email))
    db.commit()


def create_invoice(invoice, bank_name, city,inn_client,bik,):
    """Добавление счета"""
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO invoice (invoice_id,invoice, bank_name, city,CUSTOMER_ID,bik)"
                    " VALUES (null,?,?,?,?,?)",
                    (invoice, bank_name, city,inn_client,bik))
    db.commit()


def show_tables():
    class Table(tk.Frame):
        def __init__(self, parent=None, headings=tuple(), rows=tuple()):
            super().__init__(parent)

            table = ttk.Treeview(self, show="headings", selectmode="browse")
            table["columns"] = headings
            table["displaycolumns"] = headings

            for head in headings:
                table.heading(head, text=head, anchor=tk.CENTER)
                table.column(head, anchor=tk.CENTER)

            for row in rows:
                table.insert('', tk.END, values=tuple(row))

            scrolltable = tk.Scrollbar(self, command=table.yview)
            table.configure(yscrollcommand=scrolltable.set)
            scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
            table.pack(expand=tk.YES, fill=tk.BOTH)

    data = (",")
    with sqlite3.connect('test.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clients")
        data = (row for row in cursor.fetchall())

    root = tk.Tk()
    table = Table(root, headings=('№', 'Имя', 'Фамилия', 'ИНН', 'Город','Почта'), rows=data)
    table.pack(expand=tk.YES, fill=tk.BOTH)


def show_invoices():
    class Table(tk.Frame):
        def __init__(self, parent=None, headings=tuple(), rows=tuple()):
            super().__init__(parent)

            table = ttk.Treeview(self, show="headings", selectmode="browse")
            table["columns"] = headings
            table["displaycolumns"] = headings

            for head in headings:
                table.heading(head, text=head, anchor=tk.CENTER)
                table.column(head, anchor=tk.CENTER)

            for row in rows:
                table.insert('', tk.END, values=tuple(row))

            scrolltable = tk.Scrollbar(self, command=table.yview)
            table.configure(yscrollcommand=scrolltable.set)
            scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
            table.pack(expand=tk.YES, fill=tk.BOTH)

    data = (",")
    with sqlite3.connect('test.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM invoice")
        data = (row for row in cursor.fetchall())

    root = tk.Tk()
    table = Table(root, headings=('№', 'Счет', 'Банк', 'Город', 'ИНН', 'Бик'), rows=data)
    table.pack(expand=tk.YES, fill=tk.BOTH)


def show_transfers():
    class Table(tk.Frame):
        def __init__(self, parent=None, headings=tuple(), rows=tuple()):
            super().__init__(parent)

            table = ttk.Treeview(self, show="headings", selectmode="browse")
            table["columns"] = headings
            table["displaycolumns"] = headings

            for head in headings:
                table.heading(head, text=head, anchor=tk.CENTER)
                table.column(head, anchor=tk.CENTER)

            for row in rows:
                table.insert('', tk.END, values=tuple(row))

            scrolltable = tk.Scrollbar(self, command=table.yview)
            table.configure(yscrollcommand=scrolltable.set)
            scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
            table.pack(expand=tk.YES, fill=tk.BOTH)

    data = (",")
    with sqlite3.connect('test.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM transfer")
        data = (row for row in cursor.fetchall())

    root = tk.Tk()
    table = Table(root, headings=('№', 'Дата', 'Счет-дебит', 'Счет-кредит', 'Сумма'), rows=data)
    table.pack(expand=tk.YES, fill=tk.BOTH)
