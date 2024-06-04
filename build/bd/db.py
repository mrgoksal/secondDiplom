# C:\Users\Роман\Desktop\secondDiplom\build\bd\db.py

import mysql.connector as con

def get_connection():
    try:
        connection = con.connect(
            host='localhost',
            user='root',
            password='2004',
            database='world'
        )
        print("Подключение к базе данных успешно")
        return connection
    except con.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Соединение с базой данных закрыто")

def execute_query(query, params=()):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            print("Запрос выполнен успешно")
            return cursor.fetchall()
        except con.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)
    else:
        print("Не удалось подключиться к базе данных для выполнения запроса.")
        return None
