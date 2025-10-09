
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    1/ verifier que h et w ont la meme taille et que ce soit des int/float
    2/ creer des paires, assembler height[0] avec weight[0] etc... (zip)
    3/ calculer un bmi : poids / taille au carré
    4/ stocker le resultat dans une liste
    5/ retourner le resultat
    """

    if (len(height) != len(weight)):
        print("AssertionError: height and weight must have the same length.")
        return

    if not isinstance(height, list):
        print("AssertionError: height and weight must be list only.")
        return

    if not all(isinstance(x, (int, float)) for x in height):
        print("AssertionError: elem in h list must be float or int only.")
        return

    if not all(isinstance(x, (float, int)) for x in weight):
        print("AssertionError: elem in w list must be float or int only.")
        return

    zip(height, weight)
    # print(list(pairs))
    newList = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        newList.append(bmi)
    return (newList)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    -> prend en param liste de BMI + limite
    -> indique si chaque BMI dépasse la limite
    -> renvoie une liste de booleen

    1/ verifier si les args sont bien une liste + un int
    2/ parcourir bmi et comparer avec la limite
    3/ renvoyer true or false selon le resultat
    4/ stocker le resultat
    5/ retourner le resultat
    """

    if not isinstance(bmi, list):
        print("AssertionError: bmi must be list only.")
        return

    if not isinstance(limit, int):
        print("AssertionError: limit must be a int onyl.")
        return

    newList = []
    for elem in bmi:
        if int(elem) > limit:
            res = False
            newList.append(res)
        else:
            res = True
            newList.append(res)
    return (newList)
