import typing as tp


class CommandGetter:
    def __init__(self, help_desc: str,
                 constructors: tp.Optional[list[tp.Callable[[str], tp.Any]]] = None,
                 names: tp.Optional[list[str]] = None,
                 multiline=False):
        self.help = help_desc
        if constructors is None:
            constructors = [str] * 25
        self.constructors = constructors
        self.names = names
        self.multiline = multiline

        # if names is not None and len(self.names) != len(self.constructors):
        #     raise ValueError("names for constructors and constructors should be the same length")

    def get(self) -> list[tp.Any]:
        print(self.help)
        if self.multiline:
            return self._get_multiliner()
        return self._get_oneliner()

    def _get_oneliner(self):
        user_input = input()
        result = []
        try:
            for part, constructor in zip(user_input.split(), self.constructors):
                result.append(constructor(part))

        except ValueError:
            print("Invalid input")
            result = []

        return result

    def _get_multiliner(self):
        result = []
        idx = -1
        try:
            while True:
                idx += 1
                if idx >= len(self.names):
                    break
                print(f"Enter {self.names[idx]}:", end=' ')
                user_input = input()

                if user_input == '':
                    break

                result.append(self.constructors[idx](user_input))

        except ValueError:
            print("Invalid input")
            result = []

        return result
