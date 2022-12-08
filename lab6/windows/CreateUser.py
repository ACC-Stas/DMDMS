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
        self.command_type_getter = CommandGetter("Commands: register, show")
        self.data_getter = CommandGetter("Enter your data", names=['User name', 'Password', 'Role'], multiline=True)
        self.drop_getter = CommandGetter("Enter your data", names=['User name'], multiline=True)
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

    def show(self):
        try:
            self.db.cursor.execute("SELECT user FROM mysql.user")
        except Error as e:
            print("Error while reading:", e)
            return

        records = self.db.cursor.fetchall()
        print("You have read")
        for record in records:
            print(record)

    def drop(self):
        name = self.drop_getter.get()[0]
        try:
            self.db.cursor.execute(f"DROP  USER \'{name}\'@\'localhost\';")
        except Error as e:
            print("Error while reading:", e)
            return

        records = self.db.cursor.fetchall()
        print(records)

    def register(self):
        name, password, role = self.data_getter.get()

        create_user_query = f"""
                CREATE USER \'{name}\'@\'localhost\' IDENTIFIED BY \'{password}\';
                """

        roles = []
        grant_options = []
        if role == 'Admin':
            roles = ['Admin', 'Manager', 'Stuff']
            grant_options = ['WITH ADMIN OPTION', 'WITH ADMIN OPTION', 'WITH ADMIN OPTION']

        if role == 'Manager':
            roles = ['Manager', 'Stuff']
            grant_options = ['', 'WITH ADMIN OPTION']

        if role == 'Stuff':
            roles = ['Stuff']
            grant_options = ['']

        roles_list_str = "\', \'".join(roles)
        set_default_role_query = f"""
                                 SET DEFAULT ROLE \'{roles_list_str}\' TO \'{name}\'@\'localhost\';
                                 """
        drop_user_query = f"""
                          DROP USER \'{name}\'@\'localhost\';
                          """

        self.db.connection.start_transaction()
        try:
            self.db.cursor.execute(create_user_query)
        except Error as e:
            self.db.connection.rollback()
            print("Error while creating user:", e)
            return

        try:

            for cur_role, cur_grant in zip(roles, grant_options):
                grant_role_query = f"""
                                       GRANT \'{cur_role}\' TO \'{name}\'@\'localhost\' {cur_grant};
                                       """

                self.db.cursor.execute(grant_role_query)

            self.db.cursor.execute("FLUSH PRIVILEGES;")
            self.db.cursor.execute(set_default_role_query)
        except Error as e:
            print("Error while granting role:", e)
            self.db.connection.rollback()
            self.db.cursor.execute(drop_user_query)
            self.db.connection.commit()
            return

        record = self.db.cursor.fetchall()
        print("created: ", record)
        self.db.connection.commit()


