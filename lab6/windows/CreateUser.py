from .IWindow import IWindow
from .CommandGetter import CommandGetter
import sys
import mysql.connector
from mysql.connector import Error

sys.path.append('..')
from lab6.DBConnection import DataBase  # noqa


class CreateUser(IWindow):
    def __init__(self, help_desc=None, parent=None):
        if help_desc is None:
            help_desc = 'Here you can create new user'

        super().__init__(help_desc, parent)
        self.command_type_getter = CommandGetter("Commands: register")
        self.data_getter = CommandGetter("Enter your data", names=['User name', 'Password', 'Role'], multiline=True)
        self.db = DataBase()

    def run(self) -> None:
        self.help()
        while True:
            command = self.command_type_getter.get()
            if len(command) == 0:
                print("zero input is incorrect")
                continue

            self.handle_command(command)

            if command[0] == 'back':
                break

    def register(self):
        name, password, role = self.data_getter.get()

        create_user_query = f"""
                CREATE USER \'{name}\'@\'localhost\' IDENTIFIED BY \'{password}\';
                """

        grant_option = 'WITH GRANT OPTION' if role == 'Admin' or role == 'Manager' else ''
        grant_role_query = f"""
                        GRANT \'{role}\' TO \'{name}\'@\'localhost\' {grant_option};
                        """
        print(grant_role_query)

        try:
            self.db.cursor.execute(create_user_query)
        except Error as e:
            self.db.connection.rollback()
            print("Error while creating user:", e)
            return

        try:
            self.db.cursor.execute(grant_role_query)
            self.db.cursor.execute("FLUSH PRIVILEGES;")
        except Error as e:
            self.db.connection.rollback()
            print("Error while granting role:", e)
            return

        record = self.db.cursor.fetchall()
        print("created: ", record)
        self.db.connection.commit()


