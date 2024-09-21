from interface_segragation.interfaces.shape import IShape
class LandRectangle(IShape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.height * self.width

    def get_perimeter(self) -> int:
        return (self.height * 2) + (self.width * 2)