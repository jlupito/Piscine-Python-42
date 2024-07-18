from load_image import ft_load
import numpy as np
from PIL import Image

def main():
    try:
        img_pixels = ft_load("animal.jpeg")
        img_loaded = Image.fromarray(img_pixels)
        crop_area = (left, up, right, low)  # (gauche, haut, droite, bas)
        img_cropped = img_loaded.crop(crop_area)
        img_gray = img_cropped.convert("L")
        
        cropped_array = np.array(img_cropped)
        new_shape = cropped_array.shape[:2]
        print(f"New shape after slicing: {new_shape}")
        print(cropped_array[:,:,0])
        
        img_cropped.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
