from .IWindow import IWindow
from .CommandGetter import CommandGetter
import typing as tp
import sys
import mysql.connector
from mysql.connector import Error

sys.path.append('..')
from lab6.DBConnection import DataBase  # noqa


class CRUDWindow(IWindow):
    def __init__(self, table_name: str, insert_columns: tp.Optional[list[str]] = None,
                 update_columns: tp.Optional[list[str]] = None,  # last one is used as where cond = val
                 delete_column: tp.Optional[str] = None,
                 select_columns: tp.Optional[list[str]] = None,
                 help_desc=None, parent=None):
        if help_desc is None:
            help_desc = f'Enter \n Here you can do CRUD on {table_name}'

        super().__init__(help_desc, parent)
        self.db = DataBase()

        self.command_getter = CommandGetter("Options: create read update delete")
        self.table_name = table_name
        self.insert_columns = insert_columns
        if self.insert_columns is not None:
            self.insert_getter = CommandGetter('Enter value to insert', names=self.insert_columns, multiline=True)
        else:
            self.insert_getter = None

        self.update_columns = update_columns
        if self.update_columns is not None and len(self.update_columns) >= 2:
            self.update_getter = CommandGetter('Enter value to update (last used to find row)',
                                               names=self.update_columns, multiline=True)
        else:
            self.update_getter = None

        self.delete_column = delete_column
        if self.update_columns is not None:
            self.delete_getter = CommandGetter('Enter value to delete', names=[delete_column], multiline=True)
        else:
            self.delete_getter = None

        self.select_columns = select_columns

    def run(self) -> None:
        while True:
            command = self.command_getter.get()
            if len(command) == 0:
                print("zero input is incorrect")
                continue

            self.handle_command(command)

            if command[0] == 'back':
                break

    def read(self):
        columns = f"{', '.join(self.select_columns)}"
        query = f"""
                SELECT {columns}
                FROM {self.table_name}
                """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while reading:", e)
            return

        records = self.db.cursor.fetchall()
        print("You have read")
        for record in records:
            print(record)

    def create(self):
        columns = f"{', '.join(self.insert_columns)}"
        values = self.insert_getter.get()
        values = '\', \''.join(values)
        values = f"(\'{values}\')"

        query = f"""
                INSERT INTO {self.table_name} ({columns})
                VALUES
                {values};
                """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while creating:", e)
            return

        record = self.db.cursor.fetchall()
        print("created: ", record)
        self.db.connection.commit()

    def update(self):
        values = self.update_getter.get()
        columns = self.update_columns
        pairs = [f"{column} = \'{value}\', \n" for value, column in zip(values[:-1], columns[:-1])]

        set_body = " ".join(pairs)[:-3]
        where_body = f"{columns[-1]} = {values[-1]}"

        query = f"""
                UPDATE {self.table_name}
                SET {set_body}
                WHERE {where_body};
                """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while updating:", e)
            return

        record = self.db.cursor.fetchall()
        print("updated: ", record)
        self.db.connection.commit()

    def delete(self):
        val = self.delete_getter.get()[0]
        query = f"""
                DELETE FROM {self.table_name}
                WHERE {self.delete_column} = {val}
                """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while deleting:", e)
            return

        record = self.db.cursor.fetchall()
        print("deleted: ", record)
        self.db.connection.commit()
