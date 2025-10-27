from typing import Any


def callLimit(limit: int):
    """La fonction principale :
    crée callLimiter(function)
    Crée le décorateur et fixe la limite d’appels
    """
    count = 0

    def callLimiter(function):
        """La fonction décoratrice elle-même.
        crée limit_function(*args, **kwds)
        Prend la fonction à décorer et prépare la version contrôlée
        """

        def limit_function(*args: Any, **kwds: Any):
            """La fonction finale qui remplace ta fonction originale
            exécute ou bloque la vraie fonction
            vérifie le compteur à chaque appel"""
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call to many times")
        return limit_function
    return callLimiter
