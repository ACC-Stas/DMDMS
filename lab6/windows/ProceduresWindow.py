from .IWindow import IWindow
from .CommandGetter import CommandGetter
import typing as tp
import sys
import mysql.connector
from mysql.connector import Error

sys.path.append('..')
from lab6.DBConnection import DataBase  # noqa


class ProceduresWindow(IWindow):
    def __init__(self, help_desc: str,
                 procedures: tp.Mapping[str, tp.List[str]],
                 parent: tp.Optional[IWindow] = None):

        super().__init__(help_desc, parent)
        self.db = DataBase()
        command_help = f"Type procedure name to run or back.\nAvailable procedures: {', '.join(procedures.keys())}"
        self.command_getter = CommandGetter(command_help)

        self.procedures = {}
        for procedure_name, procedure_args in procedures.items():
            self.procedures[procedure_name] = CommandGetter(f'Enter args for {procedure_name}',
                                                            names=procedure_args,
                                                            multiline=True)

    def run_procedure(self, proc_name) -> None:
        proc_args = self.procedures[proc_name].get()
        proc_args_str = '\', \''.join(proc_args)
        if len(proc_args_str) > 0:
            proc_args_str = f"\'{proc_args_str}\'"

        try:
            self.db.cursor.execute(f"""
                                    CALL {proc_name}({proc_args_str});
                                    """
                                   )
        except Error as e:
            print(f"Error during proc {proc_name} with args {proc_args}: {e}")

        records = self.db.cursor.fetchall()
        print("Procedure result:")
        for record in records:
            print(record)

        self.db.connection.next_result()

    def run(self) -> None:
        self.help()
        while True:
            command = self.command_getter.get()
            if len(command) == 0:
                print('no command')
                continue

            if command[0] in self.procedures:
                self.run_procedure(command[0])
                continue

            self.handle_command(command)

            if command[0] == 'back':
                break
