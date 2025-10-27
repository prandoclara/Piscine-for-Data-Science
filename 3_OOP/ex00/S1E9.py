from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor Abstract Class"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """First Method"""
        self.is_alive = False


class Stark(Character):
    """Stark Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor Stark Class"""
        super().__init__(first_name, is_alive)
