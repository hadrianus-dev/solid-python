from dependence_inversion.interfaces.repository import IRepository

class MySQLRepository(IRepository):
    def __init__(self) -> None:
        self.__connection = 'mysql'

    def save(self) -> None:
        print('saving data on {}'.format(self.__connection))

    def load(self) -> None:
        print('loading data on {}'.format(self.__connection))