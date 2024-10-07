from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import matplotlib.pyplot as plt


def main():
    image = ft_load("landscape.jpg")
    if image is None:
        return
    print(f"The shape of image is: {image.shape}")
    print(image)
    try:
        invert = ft_invert(image)
        red = ft_red(image)
        green = ft_green(image)
        blue = ft_blue(image)
        gray = ft_grey(image)
        print(ft_invert.__doc__)
        print(ft_red.__doc__)
        print(ft_green.__doc__)
        print(ft_blue.__doc__)
        print(ft_grey.__doc__)

        filtered_images = [image, invert, red,
                           green, blue, gray]
        titles = ["Figure VIII.1: Original ",
                  "Figure VIII.2: Invert ",
                  "Figure VIII.3: Red ",
                  "Figure VIII.4: Green",
                  "Figure VIII.5: Blue ",
                  "Figure VIII.6: Grey "]

        axs = plt.subplots(3, 2, figsize=(6, 8))[1]
        # retourne un tuple contenant la figure et les axes
        # mais on ne veut que les axes
        # ensuite on itere syr tous les subplots de la grille
        for i, ax in enumerate(axs.flat):
            if ('Grey' in titles[i]):
                ax.imshow(filtered_images[i], cmap='gray')
            else:
                ax.imshow(filtered_images[i])
            ax.set_xlabel(titles[i])
            ax.set_xticks([])
            ax.set_yticks([])

        plt.show()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()
