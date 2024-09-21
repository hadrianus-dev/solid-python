from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def load(self):
        pass