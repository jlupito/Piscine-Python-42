import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    """
    Inverts the color of the image received.
    Args:
        array (np.array): the image to invert.
    Returns: the inverted image.
    """
    # verifier si tableau de type np.uint8 sinon pb de sous-overflow
    if array.dtype != np.uint8:
        array = array.astype(np.uint8)
    # on soustrait chaque valeur de pixel de la valeur maximale pour inverser
    inverted = 255 - array
    return inverted


def ft_red(array) -> np.array:
    """
    Transform the colors of the image received into red levels.
    Args:
        array (np.array): the image to turn into red levels.
    Returns: the red image.
    """
    # on multiplie pour laisser R inchangé et mettre a zero G et B
    red = np.copy(array)
    red = array * [1, 0, 0]
    return red


def ft_green(array) -> np.array:
    """
    Transform the colors of the image received into green levels.
    Args:
        array (np.array): the image to turn into green levels.
    Returns: the green image.
    """
    # on soustrait les R et B a eux memes pour que = 0
    green = np.copy(array)
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    return green


def ft_blue(array) -> np.array:
    """
    Transform the colors of the image received into blue levels.
    Args:
        array (np.array): the image to turn into blue levels.
    Returns: the blue image.
    """
    # on met les R et G a  = 0
    blue = np.copy(array)
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(array) -> np.array:
    """
    Transform the colors of the image received into grey levels.
    Args:
        array (np.array): the image to turn into grey levels.
    Returns: the grey image.
    """
    # on convertie le tableau en image
    image = Image.fromarray(array)
    # convert pour convertir l image et 'L' pour les niveaux de gris
    # (chaque pixel aura une seule valeur d'intensité lumineuse)
    grey = image.convert("L")
    greyed = np.array(grey)
    return greyed
