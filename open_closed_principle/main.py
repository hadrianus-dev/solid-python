from repository import Repository
from database import MySQLDB, PostgresDB

db_conn_mysql = MySQLDB()
repo = Repository()
repo.insert(db_conn_mysql)
print()
repo.select(db_conn_mysql)
print()
db_conn_postgres = PostgresDB()
repo = Repository()
repo.insert(db_conn_postgres)
print()
repo.select(db_conn_postgres)