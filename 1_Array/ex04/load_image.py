import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image JPG/JPEG, la convertit en RGB et renvoie
    un numpy.ndarray de forme (H, W, 3).

    - Vérifie que `path` est une chaîne non vide
    - Vérifie que l’extension du fichier est .jpg ou .jpeg
    """
    if not isinstance(path, str) or not path:
        raise ValueError("path must be a non-empty string")

    ext = os.path.splitext(path)[1].lower()
    if ext not in (".jpg", ".jpeg") or not ext:
        raise ValueError("Only JPG or JPEG files are supported")

    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

    rgb_img = img.convert("RGB")
    array = np.array(rgb_img)
    img.close()
    print(f"The shape of image is: {array.shape}")
    print(array)
    return array
