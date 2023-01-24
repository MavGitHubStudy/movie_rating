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


def create_database(database_name):
    try:
        with connect(
                host="localhost",
                user=input("Имя пользователя: "),
                password=getpass("Пароль: "),
        ) as connection:
            # Запрос CREATE DATABASE сохраняется в виде строки в переменной
            # create_db_query, а затем передается на выполнение в cursor.execute()
            create_db_query = "CREATE DATABASE " + database_name
            with connection.cursor() as cursor:
                # Если база данных с таким именем уже существует на сервере, мы получим сообщение
                # об ошибке.
                cursor.execute(create_db_query)
                print(f"База данных {database_name} успешно создана.")
    except Error as e:
        print(e)


def show_databases():
    try:
        # Приведенный код выведет имена всех баз данных, находящихся на нашем сервере
        # MySQL. Команда SHOW DATABASES в нашем примере также вывела базы данных, которые
        # автоматически создаются сервером MySQL и предоставляют доступ к метаданным баз
        # данных и настройкам сервера.
        with connect(
                host="localhost",
                user=input("Имя пользователя: "),
                password=getpass("Пароль: "),
        ) as connection:
            # Используя тот же объект MySQLConnection, что и ранее, выполним запрос
            # SHOW DATABASES, чтобы увидеть все таблицы, хранящиеся в базе данных
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)


def connect_to_database(database_name):
    try:
        with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
            database=database_name
        ) as connection:
            print(connection)
            print(f"Соединение с БД {database_name} успешно установлено.")
    except Error as e:
        print(e)
