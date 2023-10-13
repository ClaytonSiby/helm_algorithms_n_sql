import random
import psycopg2

def generate_random_data():
    records = []
    for i in range(1, 111):
        year = random.choice([2019, 2018, 2016]) if 20 <= i <= 100 else 2015
        records.append((i, year, i))
    return records

def insert_records(db_cursor):
    insert_query = """
        INSERT INTO enrollments (id, year, studentId)
        VALUES (%s, %s, %s)
    """

    db_cursor.executemany(insert_query, generate_random_data())

def create_db_and_insert_records():
    connect = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='passes',
        host='127.0.0.1',
        port=5433
    )

    cursor = connect.cursor()

    try:
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER NOT NULL PRIMARY KEY,
                year INTEGER NOT NULL,
                studentId INTEGER NOT NULL
            )
        """
        )

        insert_records(cursor)

        connect.commit()
        print("Records inserted successfully! ✅")
    finally:
        cursor.close()
        connect.close()
        print("Connection closed! 🔥")
