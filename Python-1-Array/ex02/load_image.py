from PIL import Image, UnidentifiedImageError
import numpy as np

def ft_load(path: str) -> np.array: 
    """
    ft_load(str) -> array

    loads an JPG or JPEG image, prints its shape, and its pixels
    content in RGB format.
    """
    try:
        image = Image.open(path)
    except ValueError as e:
        raise ValueError(f"{e}.")
    
    if image.format not in ["JPEG", "JPG"]:
        raise ValueError("Image must be in JPG or JPEG format.")
    
    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = np.array(image)
    print(f"The shape of image is: {pixels.shape}")
    #ca va imprimer sous la forme (hauteur, largeur, nb de canaux)
    return pixels