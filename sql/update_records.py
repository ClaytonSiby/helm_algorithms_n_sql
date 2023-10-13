import psycopg2
from create_db import create_db_and_update_records

create_db_and_update_records()

def update_faulty_records():
    """
    TABLE enrollments
    id INTEGER NOT NULL PRIMARY KEY
    year INTEGER NOT NULL
    studentId INTEGER NOT NULL
    :update: the field (year) of every faulty (i.e records with ids between 20 and 100 (inclusive)) record of 2015
    """

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
            UPDATE enrollments
            SET year = 2015
            WHERE id BETWEEN 20 AND 100
        """
        )

        connect.commit()
        print("Records updated successfully! ✅")
    finally:
        cursor.close()
        connect.close()
        print("Connection closed! 🔥")

update_faulty_records()
