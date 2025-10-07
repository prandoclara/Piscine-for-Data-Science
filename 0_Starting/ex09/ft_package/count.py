# necessaire si je veux ajouter du code, des fonctions additionnelles
def count_in_list(lst, item):
    """
    Compte le nombre d'occurrences de `item` dans `lst`.
    """
    count = 0
    for elem in lst:
        if elem == item:
            count += 1
    return count
