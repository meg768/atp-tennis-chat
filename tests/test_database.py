import tempfile
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from scripts import database


class DatabaseTests(unittest.TestCase):
    def test_local_credentials_and_literal_password(self):
        with tempfile.TemporaryDirectory() as folder:
            env = Path(folder) / ".env"
            env.write_text('DB_HOST=localhost\nDB_NAME=tennis\nDB_USER=test\n'
                           'DB_PASSWORD="${LITERAL}#secret"\nDB_PORT=3307\n')
            with patch.object(database, "ENV_FILE", env), \
                    patch.object(database.pymysql, "connect") as connect:
                database.connect()
            self.assertEqual(connect.call_args.kwargs["password"], "${LITERAL}#secret")
            self.assertEqual(connect.call_args.kwargs["port"], 3307)
            self.assertFalse(connect.call_args.kwargs["autocommit"])

    def test_invalid_settings_do_not_expose_values(self):
        with patch.object(database, "dotenv_values", return_value={"DB_PORT": "secret"}):
            with self.assertRaises(database.DatabaseError) as caught:
                database.connect()
        self.assertNotIn("secret", str(caught.exception))

    def test_connection_errors_are_sanitized(self):
        config = dict.fromkeys(("DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"), "secret")
        with patch.object(database, "dotenv_values", return_value=config), \
                patch.object(database.pymysql, "connect", side_effect=Exception("secret")):
            with self.assertRaises(database.DatabaseError) as caught:
                database.connect()
        self.assertNotIn("secret", str(caught.exception))

    def test_statements_parameters_and_result_sets(self):
        for sql in ("SELECT %s", "INSERT INTO t VALUES (%s)",
                    "UPDATE t SET a=%s", "DELETE FROM t WHERE a=%s",
                    "CREATE TABLE t (a INT)"):
            connection = MagicMock()
            cursor = connection.cursor.return_value.__enter__.return_value
            cursor.description = None
            cursor.rowcount = 1
            cursor.nextset.side_effect = [True, None]
            with patch.object(database, "connect", return_value=connection):
                result = database.execute(sql, (7,))
            cursor.execute.assert_called_once_with(sql, (7,))
            self.assertEqual(len(result), 2)
            connection.commit.assert_called_once()
            connection.rollback.assert_not_called()
            connection.close.assert_called_once()

    def test_select_rows(self):
        connection = MagicMock()
        cursor = connection.cursor.return_value.__enter__.return_value
        cursor.description = [("id",)]
        cursor.fetchall.return_value = [{"id": 7}]
        cursor.nextset.return_value = None
        with patch.object(database, "connect", return_value=connection):
            self.assertEqual(database.execute("SELECT id FROM t")[0]["rows"], [{"id": 7}])

    def test_failed_operation_rolls_back_and_sanitizes(self):
        connection = MagicMock()
        with patch.object(database, "connect", return_value=connection):
            with self.assertRaises(database.DatabaseError) as caught:
                with database.transaction():
                    raise ValueError("secret")
        self.assertNotIn("secret", str(caught.exception))
        connection.rollback.assert_called_once()
        connection.commit.assert_not_called()
        connection.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
