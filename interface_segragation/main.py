from .lands.rectangle import LandRectangle
from .lands.square import LandSquare
from .Engineer import Engineer

my_engineer = Engineer('John')
my_square = LandSquare(5)
my_engineer.measure_area(my_square)
print()
my_rectangle = LandRectangle(5, 10) 
my_engineer.measure_area(my_rectangle)