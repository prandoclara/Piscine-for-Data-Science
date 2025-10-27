class calculator:
    """Calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """multyply each 2 nb at index"""
        print(f'Dot product is: {sum(v1 * v2 for v1, v2 in zip(V1, V2))}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add each 2 nb at index"""
        res = [v1 + v2 for v1, v2 in zip(V1, V2)]
        result = [f'{val:.1f}' for val in res]
        print(f"Add vector is: [{', '.join(result)}]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """substract each 2 nb at index"""
        res = [v1 - v2 for v1, v2 in zip(V1, V2)]
        result = [f'{val:.1f}' for val in res]
        print(f"Sous vector is: [{', '.join(result)}]")
