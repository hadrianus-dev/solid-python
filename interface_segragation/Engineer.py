from typing import Type
from .interfaces.shape import IShape

class Engineer:
    def __init__(self, name: str) -> None:
        self.name = name

    def measure_perimeter(self, shape: Type[IShape]):
        perimeter = shape.get_perimeter()
        print(f'{self.name} measures perimeter: {perimeter}')
    
    def measure_area(self, shape: Type[IShape]):
        area = shape.get_area()
        print('{} measures area: {}'.format(self.name, area))
