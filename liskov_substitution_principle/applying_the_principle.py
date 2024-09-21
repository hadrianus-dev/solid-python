class Bird:
    def move(self):
        raise NotImplementedError("Subclasses should implement this!")

class FlyingBird(Bird):
    def move(self):
        return "I can fly"

class NonFlyingBird(Bird):
    def move(self):
        return "I can't fly but I can walk or swim"

class Penguin(NonFlyingBird):
    def move(self):
        return "I can swim"

def make_bird_move(bird: Bird):
    print(bird.move())

# Agora, o pinguim se move de acordo com suas capacidades
penguin = Penguin()
make_bird_move(penguin)  # Saída: "I can swim"

# Outro pássaro que voa
sparrow = FlyingBird()
make_bird_move(sparrow)  # Saída: "I can fly"
