import numpy as np
from PIL import Image

def ft_invert(array) -> np.array:
    """
    ft_invert(array) -> np.array
    
    Inverts the color of the image received.
    """
    # verifier si tableau de type np.uint8 sinon pb de sous-overflow
    if array.dtype != np.uint8:
        array = array.astype(np.uint8)
    # on soustrait chaque valeur de pixel de la valeur maximale pour inverser
    array = 255 - array
    Image.fromarray(array).show()

def ft_red(array) -> np.array:
    """
    ft_red(array) -> np.array
    
    Transform the colors of the image received into red levels.
    """
    # verifier si tableau de type np.uint8 sinon pb de sous-overflow
    if array.dtype != np.uint8:
        array = array.astype(np.uint8)
    # on crée un masque qui laisse le R inchangé et met a zero G et B
    mask = np.array([1, 0, 0], dtype=np.uint8)
    red = array * mask
    Image.fromarray(red).show()

def ft_green(array) -> np.array:
    """
    ft_green(array) -> np.array
    
    Transform the colors of the image received into green levels.
    """
    # verifier si tableau de type np.uint8 sinon pb de sous-overflow
    if array.dtype != np.uint8:
        array = array.astype(np.uint8)
    # on soustrait les R et B a leur propre valeur pour que = 0
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    Image.fromarray(green).show()

def ft_blue(array) -> np.array:
    """
    ft_blue(array) -> np.array
    
    Transform the colors of the image received into blue levels.
    """
    # verifier si tableau de type np.uint8 sinon pb de sous-overflow
    if array.dtype != np.uint8:
        array = array.astype(np.uint8)
    # on soustrait les G et R a  = 0
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Image.fromarray(blue).show()

def ft_grey(array) -> np.array:
    """
    ft_grey(array) -> np.array
    
    Transform the colors of the image received into grayscale levels.
    """
    #oon convertie le tableau en image
    image = Image.fromarray(array)
    # convert pour convertir l image et 'L' pour les niveaux de gris (chaque pixel aura une seule valeur d'intensité lumineuse)
    grey = image.convert("L")
    grey.show()