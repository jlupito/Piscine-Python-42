from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def zoom_gray(img, x_start, x_end, y_start, y_end) -> np.array:
    """
    Load an image, zoom in on a specific region and 
    convert it to grayscale.

    Args:
        - img (array): the image to zoom in and gray.
        - x_start (int): x axis starting point (left).
        - x_end (int): x axis ending point (right).
        - y_start (int): y axis starting point (up).
        - y_end (int): y axis ending point (low).
    Returns:
        A numpy array countaining the zoomed and grayed image.
    
    """
    img_zoomed = img[y_start:y_end, x_start:x_end]
    img_img = Image.fromarray(img_zoomed)
    img_grayed = img_img.convert("L")
    
    new_img = np.array(img_grayed)
    new_shape = np.expand_dims(new_img, axis=-1)
    print(f"New shape after slicing: {new_shape.shape} or ")
    print(new_shape)
    
    return new_img

def main():

    img_pixels = ft_load("animal.jpeg")
    if img_pixels is None:
        return
    try:
        img_zoomed = zoom_gray(img_pixels, 100, 500, 100, 500)
        plt.imshow(img_zoomed, cmap='gray')
        plt.show()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return

if __name__ == "__main__":
    main()
