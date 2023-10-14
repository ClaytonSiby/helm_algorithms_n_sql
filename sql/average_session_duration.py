import psycopg2
import random

def generate_random_session_data():
    records = []
    for index in range(1, 1001):
        duration = random.randint(1, 30)
        records.append((index, index, duration))
    return records

def insert_session_records(db_cursor):
    insert_query = """
        INSERT INTO sessions (id, "userId", duration)
        VALUES (%s, %s, %s)
    """

    db_cursor.executemany(insert_query, generate_random_session_data())

def average_session_duration():
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
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY,
                "userId" INTEGER NOT NULL,
                duration INTEGER NOT NULL
            )
        """
        )

        insert_session_records(cursor)
        
        connect.commit()
        print("Records inserted successfully! ✅")
    finally:
        cursor.close()
        connect.close()
        print("Connection closed! 🔥")

average_session_duration()

def calc_average_session_duration(db_cursor):
    db_cursor.execute(
    """
        SELECT "userId", AVG("duration") AS average_session_duration
        FROM sessions
        GROUP BY "userId"
        HAVING AVG("duration") > 1
    """
    )

    print('Records updated successfully! ✅')
