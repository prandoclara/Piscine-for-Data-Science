def square(x: int | float) -> int | float:
    """
    Cette fonction prend un nombre et
    retourne ce nombre multiplié par lui-même.
    """
    if isinstance(x, (int, float)):
        return x * x
    print("ERROR")


def pow(x: int | float) -> int | float:
    """
    Cette fonction élève le nombre à la puissance de lui-même
    """
    if isinstance(x, (int, float)):
        return x ** x
    print("ERROR")


def outer(x: int | float, function) -> object:
    """Retourne une fonction qui exécute 'function(x)'
    quand on l'appelle plusieurs fois"""
    count = 0

    if not callable(function):
        print("ERROR")
        return None

    def inner() -> float:
        nonlocal count
        count += 1
        if isinstance(x, (int, float)):
            result = x
            for _ in range(count):
                result = function(result)
            return result
        print("ERROR")
        return None
    return inner
