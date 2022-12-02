from .IWindow import IWindow
from .CommandGetter import CommandGetter
import typing as tp
import sys
import mysql.connector
from mysql.connector import Error


class ListWindow(IWindow):
    def __init__(self, help_desc: str, windows: tp.Mapping[str, IWindow], parent: tp.Optional[IWindow] = None):
        super().__init__(help_desc, parent)
        self.windows = windows
        command_help = "Available: redirect"
        self.command_getter = CommandGetter(command_help)
        self.redirect_getter = CommandGetter(f"Available: {', '.join(windows.keys())}")

    def redirect(self) -> None:
        window_name = self.redirect_getter.get()[0]
        if window_name not in self.windows:
            print(f"no such window {window_name}")
            return
        self.windows[window_name].run()

    def run(self) -> None:
        self.help()
        while True:
            command = self.command_getter.get()
            if len(command) == 0:
                print('no command')
                continue

            self.handle_command(command)

            if command[0] == 'back':
                break

