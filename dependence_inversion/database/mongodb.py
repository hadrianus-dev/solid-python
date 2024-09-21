from dependence_inversion.interfaces.repository import IRepository

class MongoRepository(IRepository):
    def __init__(self) -> None:
        self.__connection = 'mongodb'

    def save(self) -> None:
        print('saving data on {}'.format(self.__connection))

    def load(self) -> None:
        print('loading data on {}'.format(self.__connection))