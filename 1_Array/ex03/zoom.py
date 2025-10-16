import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    This program loads an image in JPG format,
    prints its properties,
    performs a zoom by cropping a specific area,
    converts it to grayscale,
    and displays it with visible X and Y axes.
    """
    try:
        ft_load("./animal.jpeg")
    except ValueError:
        raise ValueError("Can't load the image")

    newimg = Image.open("./animal.jpeg")
    cropimg = newimg.crop((450, 100, 850, 500))
    greyimg = cropimg.convert("L")
    newarray = np.expand_dims(np.array(greyimg), axis=2)
    newimg.close()
    print(f'New shape after slicing: {newarray.shape}')
    print(newarray)

    plt.imshow(newarray.squeeze(), cmap='gray')
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    main()
