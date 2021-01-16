import sqlite3 as sql
import datetime
from random import randint, uniform


def create_databases():
    """Создание трех таблиц"""
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS clients (client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(30),surname VARCHAR(30),city VARCHAR(45), email VARCHAR(50))""")

        cur.execute("""CREATE TABLE IF NOT EXISTS invoice  (invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    invoice INTEGER(20),bank_name VARCHAR(225), city VARCHAR(45), INN INTEGER(12), BIK INTEGER(9),
                    CUSTOMER_ID INT references clients(client_id))""")

        cur.execute("""CREATE TABLE IF NOT EXISTS transfer (transfer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_formation DATETIME  NOT NULL , debit_account INTEGER,credit_account INTEGER, 
                      total_transfer FLOAT,year_month TEXT)""")


def create_transfer():
    """добавлние значений в Проводок"""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    year_month = datetime.datetime.now().strftime("%Y_%m")
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO transfer (transfer_id, date_formation,"
                    " debit_account,credit_account,total_transfer,year_month) VALUES (null,?,?,?,?,?)",
                    (date, randint(100, 1000), randint(100, 1000), uniform(0.11, 1000.99), year_month))
    db.commit()


def create_client(name, surname, city, email):
    """Создание клиента"""
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO clients (client_id,name, surname, city,email) VALUES (null,?,?,?,?)",
                    (name, surname, city, email))
    db.commit()


def create_invoice(invoice, bank_name, city, inn, bik):
    """Добавление счета"""
    with sql.connect('Test.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO clients (invoice_id,invoice, bank_name, city, inn,bik,CUSTOMER_ID)"
                    " VALUES (null,?,?,?,?,?,?)",
                    (invoice, bank_name, city, inn, bik))
    db.commit()
