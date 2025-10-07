from collections.abc import Iterable

##########
# PART 1 #
##########

# ----- CLASSIQUE ------
# def ft_filter(function, iterable):
#     newList = []
#     if function is None:
#         for elem in iterable:
#             if elem:
#               newList.append(elem)
#     else:
#         for elem in iterable:
#             if function(elem):
#               newList.append(elem)
#     return(iter(newList))


# ------ list comprehension -------
def ft_filter(function, iterable):
    """
    filter(function, iterable)

    - function : fonction appliquée à chaque élément, doit return T ou F
    - iterable : séquence (liste, tuple, string, etc.) à filtrer.

    filter() renvoie un objet 'filter' (un itérateur) contenant uniquement
    les éléments pour lesquels function(element) est True.
    Pour visualiser ou réutiliser le résultat, on peut le convertir en liste :
    list(filter(function, iterable))

    Exemple :
    numbers = [0, 1, 2, 3, 4]
    result = list(filter(lambda x: x % 2 == 0, numbers))  # [0, 2, 4]

    Si la fonction passée est None, filter() retire tous les éléments "falsy"
    (0, '', None, False, [], etc.)
    """
    if not isinstance(iterable, Iterable):
        print("Not an iterable")
        return
    if function is not None and not callable(function):
        print("First argument must be a function or None")
        return
    if function is None:
        newList = [elem for elem in iterable if elem]
    else:
        newList = [elem for elem in iterable if function(elem)]
    return iter(newList)

##########
# TESTER #
##########


print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
# [2, 4]

print(list(ft_filter(None, [0, 1, "", "Hello", False, 42])))
print(list(filter(None, [0, 1, "", "Hello", False, 42])))
# [1, 'Hello', 42]
