import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main():
    """
    """
    try:
        img = Image.open("animal.jpeg")
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")

    cropimg = img.crop((450, 100, 850, 500))
    greyimg = cropimg.convert("L")
    array = np.expand_dims(np.array(greyimg), axis=2)
    print("The shape of image is : ", array.shape)
    print(array[:3, :3])
    trans = np.transpose(array, (1, 0, 2))
    trans = trans.squeeze()
    print("New shape after Transpose: ", trans.shape)
    print(trans)
    img.close()

    plt.imshow(trans, cmap="gray")
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    main()
