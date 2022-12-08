from .IWindow import IWindow
from .CommandGetter import CommandGetter
import sys
import mysql.connector
from mysql.connector import Error

sys.path.append('..')
from lab6.DBConnection import DataBase  # noqa


class Enter(IWindow):
    def __init__(self, child_window, help_desc=None, parent=None):
        if help_desc is None:
            help_desc = 'Enter \n Here you can login and quit'

        super().__init__(help_desc, parent)
        self.command_type_getter = CommandGetter("Commands: login, quit")
        self.data_getter = CommandGetter("Enter your data", [str, str], ['User name', 'Password'], multiline=True)
        self.db = DataBase()
        self.child_window = child_window

    def run(self) -> None:
        self.help()
        while True:
            command = self.command_type_getter.get()
            if len(command) == 0:
                print("zero input is incorrect")
                continue

            self.handle_command(command)

            if command[0] == 'quit':
                break

    def login(self):
        self.quit()
        login, password = self.data_getter.get()

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='DMDMS',
                                                 user=login,
                                                 password=password)
            self.db.connect(connection)

            db_Info = self.db.connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            self.db.cursor.execute("select database();")
            record = self.db.cursor.fetchone()
            print("You're connected to database: ", record)

            self.db.cursor.execute("SET autocommit=0;")

        except Error as e:
            print("Error while connecting to MySQL", e)
            return

        self.child_window.run()

    def quit(self):
        if self.db.connection is None:
            return

        if self.db.connection.is_connected():
            self.db.cursor.close()
            self.db.connection.close()
