class Repository:

    def insert(self, db_connection: any) -> None:
        connetion = db_connection.connect()
        print('database {} connected'.format(connetion))
        print('Inserting data on {}...'.format(connetion))
        db_connection.disconnect()

    def select(self, db_connection: any) -> None:
        connetion = db_connection.connect()
        print('database {} connected'.format(connetion))
        print('Selecting data on {}...'.format(connetion))
        db_connection.disconnect()