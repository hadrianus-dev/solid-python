class Register:

    def make_registration(self, name: str, age: int) -> None: # without single responsibility principle
        if isinstance(name, str) and isinstance(age, int): 
            print('Accessing data base...')
            print(f'Registered {name} with age {age}')
        else:
            print('Invalid data')