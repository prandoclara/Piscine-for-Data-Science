

def ft_tqdm(lst: range) -> None:
    """
    Simule le comportement basique de la bibliothèque tqdm :
    affiche une barre de progression dynamique pendant l'itération.

    Tqdm = "Te quiero demasiado"

    Arguments :
        lst (iterable): Une séquence sur laquelle itérer.

    Affiche :
        - Le pourcentage d'avancement
        - Une barre de progression visuelle (█████-----)
        - La fraction du nombre total d'itérations

    Mesures incluses :
        - Temps écoulé
        - Estimation du temps restant (ETA)
        - Performance (itérations/seconde)

    Exemple :
        for i in ft_tqdm(range(100)):
            time.sleep(0.01)
        42%|███████████████-------------| 42/100 [00:00<00:01, 98.3 it/s]
    """
    total = len(lst)
    for i, elem in enumerate(lst):
        progres = (i + 1) / total
        bar_len = 81
        filled = int(bar_len * progres)
        bar = "█" * filled + "-" * (bar_len - filled)
        print(f"\r{int(progres*100)}%|{bar}|{i+1}/{total}", end="")
        yield elem
    print()
