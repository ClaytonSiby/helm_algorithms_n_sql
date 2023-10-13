import unittest
import psycopg2
from unittest.mock import patch
from sql.update_records import update_records

class TestUpdateRecords(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_update_records(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_connect.return_value.__enter__.return_value = mock_cursor

        update_records()

        mock_cursor.execute.assert_called_once_with("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER NOT NULL PRIMARY KEY,
                year INTEGER NOT NULL,
                studentId INTEGER NOT NULL
            )
        """)

        mock_connect.return_value.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

