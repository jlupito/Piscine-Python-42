from load_image import ft_load
import numpy as np
from PIL import Image

def zoom_gray(path, left, right, up, low) -> np.array:
    """

    zoom_gray(path, left, right, up, low) -> np.array
    Load an image, zoom in on a specific region and convert it to grayscale.
    
    """
    try:
        img_pixels = ft_load(path)
        img_loaded = Image.fromarray(img_pixels)
        crop_area = (left, up, right, low)  # (gauche, haut, droite, bas)
        img_cropped = img_loaded.crop(crop_area)
        img_gray = img_cropped.convert("L")
        
        new_img = np.array(img_gray)
        new_shape = np.expand_dims(new_img, axis=-1)
        print(f"New shape after slicing: {new_shape.shape} or {new_img.shape}")
        print(new_shape)
        
        return new_img

    except Exception as e:
        print(f"Error: {e}")

def main():

    image = zoom_gray("animal.jpeg", 100, 500, 100, 500)
    Image.fromarray(image).show()

if __name__ == "__main__":
    main()
