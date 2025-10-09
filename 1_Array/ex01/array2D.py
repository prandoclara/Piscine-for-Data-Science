def slice_me(family: list, start: int, end: int) -> list:
    """
    1/ verifier que family est une list
    2/ verifier que start et end sont des int
    3/ verifier que family n'est pas vide
    4/ verifier que chaque elem de family est une list
    5/ verifier le nombre de colonnes de chaque sous liste
    6/ verifier que chaque sous liste possedent le meme nombre de colonne
    7/ calcul et affichage de la shape
    8/ effectuer la decoupe avec le slicing
    9/ calcul et affichage de la nouvelle shape
    10/ retourner nouvelle liste
    """

    if not isinstance(family, list):
        raise TypeError("family must be a list of lists")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    if len(family) == 0:
        raise ValueError("family list is empty")

    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a list of lists")

    n_rows = len(family)
    n_cols = len(family[0])

    for row in family:
        if len(row) != n_cols:
            raise ValueError("all rows in family must have the same size")

    print(f"My shape is: ({n_rows}, {n_cols})")
    res = family[start:end]
    new_rows = len(res)
    new_cols = n_cols
    print(f"My new shape is: ({new_rows}, {new_cols})")
    return res
