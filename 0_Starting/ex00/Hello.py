ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

print("Avant :")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

ft_list[1] = "World!"
# list = mutable
# peut être modifié après sa création

ft_tuple = (ft_tuple[0], "France")
# tuple = immuable
# une fois créé, tu ne peux pas changer un élément

ft_set.remove("tutu!");
ft_set.add("Paris!");
# ft_set = {"Hello", "Paris"}
# set = peuvent etre mutables mais n'ont pas d'ordre

ft_dict["Hello"] = "42Paris"
# dictionnaire = mutable
# on peut modifier une valeur associée à une clé directement

print("\nAprès :")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
