from interface_segragation.interfaces.shape import IShape

class LandSquare(IShape):
    def __init__(self, side: int) -> None:
        self.side = side

    def get_area(self) -> int:
        return self.side * self.side

    def get_perimeter(self) -> int:
        return self.side * 4