from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def get_area(self) -> int:
        pass

    @abstractmethod
    def get_perimeter(self) -> int:
        pass