from load_image import ft_load


def main():
    image = ft_load("landscape.jpg")
    if image is None:
        return
    print(image)


if __name__ == "__main__":
    main()
