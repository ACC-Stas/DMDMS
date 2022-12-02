from abc import ABC, abstractmethod
import typing as tp


class IWindow(ABC):
    def __init__(self, help_desc: str, parent: tp.Optional['IWindow']):
        self.help_desc = help_desc
        self.parent = parent
        self.child_output = None

    def help(self):
        print(self.help_desc)

    def set_parent(self, parent):
        self.parent = parent

    def handle_command(self, command: list[tp.Any]) -> None:
        if len(command) == 0:
            print("EMPTY COMMAND")
            return

        try:
            func = getattr(self, command[0])
        except AttributeError:
            print(f"Don't have such command: {command[0]}")
            return

        func(*command[1:])

    @abstractmethod
    def run(self) -> None:
        pass

    def back(self) -> None:
        if self.parent is None:
            return

        self_dict = vars(self)
        self.parent.child_output = self_dict

