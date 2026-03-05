import sqlite3
from typing import List
from .models import Actor

TABLE_NAME = 'actors'


class ActorManager:
    def __init__(self, db_path: str = ':memory:') -> None:
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'first_name TEXT NOT NULL, '
            'last_name TEXT NOT NULL)'
        )
        self.conn.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self.cursor.execute(
            f'INSERT INTO {TABLE_NAME} (first_name, last_name) VALUES (?, ?)',
            (first_name, last_name)
        )
        self.conn.commit()

    def all(self) -> List[Actor]:
        self.cursor.execute(
            f'SELECT id, first_name, last_name FROM {TABLE_NAME}'
        )
        rows = self.cursor.fetchall()
        return [
            Actor(id=row[0], first_name=row[1], last_name=row[2])
            for row in rows
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self.cursor.execute(
            f'UPDATE {TABLE_NAME} SET first_name = ?, last_name = ? '
            'WHERE id = ?',
            (new_first_name, new_last_name, pk)
        )
        self.conn.commit()

    def delete(self, pk: int) -> None:
        self.cursor.execute(
            f'DELETE FROM {TABLE_NAME} WHERE id = ?',
            (pk,)
        )
        self.conn.commit()
