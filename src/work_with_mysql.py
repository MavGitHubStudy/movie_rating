from getpass import getpass
from mysql.connector import connect, Error


def connect_mysql():
    # Чтобы установить соединение, используем connect() из модуля mysql.connector.
    # Эта функция принимает параметры host, user и password, а возвращает объект
    # MySQLConnection. Учетные данные можно получить в результате ввода от
    # пользователя
    try:
        with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
        ) as connection:
            print(connection)
    except Error as e:
        print(e)
