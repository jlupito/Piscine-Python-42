from PIL import Image
from os import access, R_OK
import numpy as np


def ft_load(path: str) -> np.array: 
    """
    Loads an JPG or JPEG image, prints its shape, and its pixels
    content in RGB format.

    Args:
        Path (str): path to the image to load.

    Returns:
        A numpy array containing the image in RGB format.
    """
    try:
        try:
            image = Image.open(path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"{e}.")
        except IOError:
            if not access(path, R_OK):
                print(f"The file '{path}' is not readable.")
            else:
                print(f"The file '{path}' is not a valid image file.")
            return None
        
        if image.format not in ["JPEG", "JPG"]:
            raise ValueError("Image must be in JPG or JPEG format.")
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        pixels = np.array(image)
        print(f"The shape of image is: {pixels.shape}")
        #imprime sous la forme (hauteur, largeur, nb de canaux)
        return pixels

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return