from getpass import getpass
from mysql.connector import connect, Error


def connect_to_mysql():
    try:
        with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
        ) as connection:
            print(connection)
    except Error as e:
        print(e)


def create_database(database_name):
    try:
        with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
        ) as connection:
            # Чтобы создать новую базу данных, например, с именем
            # online_movie_rating, нужно выполнить инструкцию SQL
            # Примечание
            # MySQL обязывает ставить точку с запятой [;] в конце оператора.
            # Однако MySQL Connector / Python автоматически добавляет точку
            # с запятой в конце каждого запроса.
            create_db_query = "CREATE DATABASE " + database_name
            with connection.cursor() as cursor:
                # Чтобы выполнить SQL-запрос, нам понадобится курсор, который
                # абстрагирует процесс доступа к записям базы данных. MySQL
                # Connector/Python предоставляет соответствующий класс
                # MySQLCursor, экземпляр которого также называется курсором.
                cursor.execute(create_db_query)
    except Error as e:
        print(e)


def show_databases():
    try:
        with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
        ) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)


def connect_database(database_name):
    try:
        with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
            database=database_name,
        ) as connection:
            print(connection)
    except Error as e:
        print(e)
