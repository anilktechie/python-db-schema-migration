import sqlite3
from contextlib import contextmanager
from .schema_versioner import SchemaVersioner


@contextmanager
def sqlite_execute(conn, q, params=()):
    cursor = conn.cursor()
    try:
        cursor = conn.cursor()
        cursor.execute(q, params)
        conn.commit()
        yield cursor
    finally:
        cursor.close()
        conn.close()


class SqliteSchemaVersioner(SchemaVersioner):
    def __init__(self, sqlite_file: str):
        self.sqlite_file = sqlite_file

    def _new_conn(self):
        return sqlite3.connect(self.sqlite_file)

    def has_schema_version(self) -> bool:
        with sqlite_execute(self._new_conn(), 'PRAGMA table_info(schema_version)') as cursor:
            results = cursor.fetchall()
            return len(results) != 0

    def _get_schema_version(self) -> int:
        with sqlite_execute(self._new_conn(), 'SELECT v FROM schema_version') as cursor:
            result = cursor.fetchone()
            return result[0]

    def set_schema_version(self, v: int):
        with sqlite_execute(self._new_conn(), 'UPDATE schema_version SET v = ?', (v,)):
            pass
