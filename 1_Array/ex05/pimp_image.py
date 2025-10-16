import matplotlib.pyplot as plt


def show_img(array, title: str):
    """
    Displays an image with the given title.
    """
    plt.imshow(array, cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show()


def ft_invert(array):
    """Invert the colors of the image (negative filter)."""
    invert = array.copy()
    invert = 255 - invert
    show_img(invert, "Figure VIII.2: Invert")
    return invert


def ft_red(array):
    """Keep only the red channel of the image."""
    red = array.copy()
    red[:, :, 1] = 0  # on retire le vert
    red[:, :, 2] = 0  # on retire le bleu
    show_img(red, "Figure VIII.3: Red")
    return red


def ft_green(array):
    """Keep only the green channel of the image."""
    green = array.copy()
    green[:, :, 0] = 0  # on retire le rouge
    green[:, :, 2] = 0  # on retire le bleu
    show_img(green, "Figure VIII.4: Green")
    return green


def ft_blue(array):
    """Keep only the blue channel of the image."""
    blue = array.copy()
    blue[:, :, 0] = 0  # on retire le rouge
    blue[:, :, 1] = 0  # on retire le vert
    show_img(blue, "Figure VIII.5: Blue")
    return blue


def ft_grey(array):
    """Convert the image to grayscale. (R + G + B) / 3"""
    grey = array.copy()
# reduire l'intensité
    grey[:, :, 0] = grey[:, :, 0] / 3
    grey[:, :, 1] = grey[:, :, 1] / 3
    grey[:, :, 2] = grey[:, :, 2] / 3
# homogénéiser G sur R
    grey[:, :, 1] = grey[:, :, 0]
# homogénéiser B sur R
    grey[:, :, 2] = grey[:, :, 0]
# [v, v, v] = gris uniforme

    show_img(grey, "Figure VIII.6: Grey")
    return grey
