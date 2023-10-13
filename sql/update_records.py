import psycopg2

def update_records():
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
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER NOT NULL PRIMARY KEY,
                year INTEGER NOT NULL,
                studentId INTEGER NOT NULL
            )
        """
        )

        connect.commit()
    finally:
        cursor.close()
        connect.close()
