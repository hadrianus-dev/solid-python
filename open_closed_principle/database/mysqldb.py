class MySQLDB:
    def __init__(self) -> None:
        self.__connection = 'MySQL'

    def connect(self) -> str:
        print('connecting to {}'.format(self.__connection))
        return self.__connection
    
    def disconnect(self) -> str:
        print('disconnecting from {}'.format(self.__connection))
        return self.__connection