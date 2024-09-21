class Bird:
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

def make_bird_fly(bird: Bird):
    print(bird.fly())

# Tentando fazer um Penguin voar
penguin = Penguin()
make_bird_fly(penguin)  # Vai levantar um erro, violando o LSP
