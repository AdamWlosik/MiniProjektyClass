import sqlite3


class ToDoListSQLlite:

    @staticmethod
    def create_table(connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE task(task text)""")
        except:
            pass
        # nie zwraca błędu, jeśli tabela jest już utowrzona

    @staticmethod
    def show_tasks(connection):
        cursor = connection.cursor()
        cursor.execute("""SELECT rowid, task FROM task""")
        results = cursor.fetchall()

        for row in results:
            print(str(row[0]) + " - " + row[1])

    @staticmethod
    def add_task(connection):
        print("Dodajemy zadanie")
        task = input("Wpisz treść zadania: ")
        if task == "0":
            print("Powrót do menu")
        else:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
            connection.commit()
            print("Dodano zadanie!")

    @staticmethod
    def delete_task(connection):
        task_index = int(input("Podaj indeks zadania do usunięcia: "))
        cursor = connection.cursor()
        rows_deleted = cursor.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
        if rows_deleted == 0:
            print("Takie zadanie nie istnieje")
        else:
            print("Usunięto zadanie")

    @staticmethod
    def to_do_list_sql_lile_main():

        connection = sqlite3.connect("todo.db")
        connection.commit()
        ToDoListSQLlite.create_table(connection)

        while True:
            print()
            print("1. Pokaż zadania")
            print("2. Dodaj zadanie")
            print("3. Usuń zadanie")
            print("4. Wyjdź")

            user_choice = int(input("Wybierz liczbę: "))
            print()
            if user_choice == 1:
                ToDoListSQLlite.show_tasks(connection)

            if user_choice == 2:
                ToDoListSQLlite.add_task(connection)

            if user_choice == 3:
                ToDoListSQLlite.delete_task(connection)

            if user_choice == 4:
                break

        connection.close()
