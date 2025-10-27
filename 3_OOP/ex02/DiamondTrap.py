from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    class King
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """King constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def set_eyes(self, eyescolor: str):
        """Sets eye color"""
        self.eyes = eyescolor

    def set_hairs(self, haircolor: str):
        """Sets hair shade of colour"""
        self.hairs = haircolor

    def get_eyes(self) -> str:
        """Getter for eyes"""
        return self.eyes

    def get_hairs(self) -> str:
        """Getter for hairs"""
        return self.hairs
