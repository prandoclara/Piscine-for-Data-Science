from load_image import ft_load

try:
    print(ft_load("./landscape.jpg"))
except FileNotFoundError as fnf:
    print("Caught Error: ", fnf)
except ValueError as e:
    print("Caught Error: ", e)
