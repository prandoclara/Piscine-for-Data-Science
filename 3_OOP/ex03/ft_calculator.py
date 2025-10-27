class calculator:
    """
    calculator
    """

    def __init__(self, vector):
        """Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        if isinstance(object, (int, float)):
            result = [x + object for x in self.vector]
            print(result)
        else:
            print("Error: only scalar addition is supported.")

    def __mul__(self, object) -> None:
        """Multiplication"""
        if isinstance(object, (int, float)):
            result = [x * object for x in self.vector]
            print(result)
        else:
            print("Error: only scalar multiplication is supported.")

    def __sub__(self, object) -> None:
        """Subtract"""
        if isinstance(object, (int, float)):
            result = [x - object for x in self.vector]
            print(result)
        else:
            print("Error: only scalar subtraction is supported.")

    def __truediv__(self, object) -> None:
        if isinstance(object, (int, float)):
            if object == 0:
                print("Error: division by zero.")
                return
            result = [x / object for x in self.vector]
            print(result)
        else:
            print("Error: only scalar division is supported.")
