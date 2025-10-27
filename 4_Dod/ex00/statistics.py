from typing import Any


def Mean(total: float, nbArgs: int) -> None:
    """Mean"""
    print(f"mean : {total / nbArgs}")


def Median(lst: list, nbArgs: int) -> None:
    """Median"""
    lst.sort()
    median = nbArgs // 2
    if nbArgs % 2 == 0:
        res = (lst[median - 1] + lst[median]) / 2
    else:
        res = lst[median]
    print(f"median: {res}")


def Quartile(lst: list, nbArgs: int) -> None:
    """Quartile 25% et 75%"""
    lst.sort()
    quarter = nbArgs // 4
    quarter25 = lst[quarter]
    lastquarter = quarter * 3
    quarter75 = lst[lastquarter]
    print(f"quartile: [{quarter25.__float__()}, {quarter75.__float__()}]")


def Var(lst: list, nbArgs: int) -> None:
    """
    Variance : mesure à quel point les valeurs
    s’éloignent de la moyenne (Unité au carré)
    Exemple :
    list = [2, 4, 4, 4, 5, 5, 7, 9]
    Moyenne = (2+4+4+4+5+5+7+9) / 8 = 5
    Écarts à la moyenne :[-3,-1,-1,-1,0,0,2,4]
    Carrés : [9,1,1,1,0,0,4,16]
    Moyenne des carrés : (9+1+1+1+0+0+4+16) / 8 = 4
    Variance = 4
    => Plus elle est grande, plus les valeurs sont dispersées
    => La variance te dit si tes données sont “serrées” ou
    => “éparpillées” autour de la moyenne.
    => Plus elle est grande, plus tes données varient.
    => Elle est essentielle pour comprendre la stabilité,
    => la précision ou le risque d’un phénomène.
    """
    mean = sum(lst) / nbArgs
    total = sum((x - mean) ** 2 for x in lst)
    variance = total / nbArgs
    print(f"variance : {variance}")


def Std(lst: list, nbArgs: int) -> None:
    """
    Std (écart-type) : racine carrée de la variance
    √4 = 2
    En moyenne, chaque valeur s’éloigne de 2 unités de la moyenne.
    => Plus il est grand, plus les valeurs varient autour de la moyenne
    """
    mean = sum(lst) / nbArgs
    total = sum((x - mean) ** 2 for x in lst)
    variance = total / nbArgs
    std_dev = variance ** 0.5
    print(f"std : {std_dev}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Stats"""

    nbArgs = 0
    total = 0
    lst = []

    for arg in args:
        try:
            lst.append(arg)
            nbArgs += 1
            total += arg
        except TypeError:
            return

    if nbArgs == 0:
        for kwarg in kwargs.items():
            print('ERROR')
        return

    for kwarg in kwargs.values():
        if kwarg == "mean":
            Mean(total, nbArgs)
        elif kwarg == "median":
            Median(lst, nbArgs)
        elif kwarg == "quartile":
            Quartile(lst, nbArgs)
        elif kwarg == "std":
            Std(lst, nbArgs)
        elif kwarg == "var":
            Var(lst, nbArgs)
