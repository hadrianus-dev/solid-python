from database.mysqldb import MySQLRepository
from interfaces.repository import IRepository
from typing import Type

class User:

    def __init__(self, repository: Type[IRepository]) -> None:
        self.__repo = repository

    def create(self, data: any) -> None:
        self.__repo.save()

    def read(self) -> None:
        self.__repo.load()

my_user = User(MySQLRepository)
my_user.create(23)
my_user.read()