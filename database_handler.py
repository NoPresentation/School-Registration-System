import sqlite3

class DatabaseHandler():
    DB_NAME = "students.db"


    @staticmethod
    def _connection():
        return sqlite3.connect(DatabaseHandler.DB_NAME)
    

    @staticmethod
    def create_table():
        with DatabaseHandler._connection() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS STUDENT(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME TEXT NOT NULL,
                     EMAIL TEXT NOT NULL,
                     AGE INTEGER NOT NULL,
                     GENDER TEXT NOT NULL
                     );""")
            
    
    @staticmethod
    def insert_student(name, email, age, gender):
        with DatabaseHandler._connection() as conn:
            conn.execute("INSERT INTO STUDENT (NAME, EMAIL, AGE, GENDER) VALUES(?, ?, ?, ?)", (name, email, age, gender))

    @staticmethod
    def read_students():
        with DatabaseHandler._connection() as conn:
            return conn.execute("SELECT * FROM STUDENTS").fetchall()
        

DatabaseHandler.create_table()