class Register:

    def make_registration(self, name: str, age: int) -> None: # with single responsibility principle
        if self.__check_data(name, age): 
           self.__register(name, age)
        else:
            self.__error()

    def __check_data(self, name: str, age: int) -> bool: # with single responsibility principle
        return isinstance(name, str) and isinstance(age, int)
    
    def __register(self, name: str, age: int) -> None: # with single responsibility principle
        print('Accessing data base...')
        print(f'Registered {name} with age {age}')
    
    def __error(self) -> None: # with single responsibility principle
        print('Invalid data')


register = Register()
register.make_registration('John', 25)