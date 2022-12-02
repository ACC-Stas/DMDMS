class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(object, metaclass=Singleton):
    connection = None
    cursor = None

    def connect(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
