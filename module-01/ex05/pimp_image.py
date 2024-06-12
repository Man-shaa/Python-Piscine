import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    res = np.copy(array)
    res[:, :, 0] = 255 - array[:, :, 0]
    res[:, :, 1] = 255 - array[:, :, 1]
    res[:, :, 2] = 255 - array[:, :, 2]
    return (res)


def ft_red(array: np.array) -> np.array:
    """applies red filter"""
    res = np.copy(array)
    res[:, :, 1] = 0
    res[:, :, 2] = 0
    return (res)


def ft_green(array: np.array) -> np.array:
    """applies green filter"""
    res = np.copy(array)
    res[:, :, 0] -= array[:, :, 0]
    res[:, :, 2] -= array[:, :, 2]
    return (res)


def ft_blue(array: np.array) -> np.array:
    """applies blue filter"""
    res = np.copy(array)
    res[:, :, 1] = 0
    res[:, :, 0] = 0
    return (res)


def ft_grey(array: np.array) -> np.array:
    """applies grayscale filter"""
    res = (array[:, :, 0] / 3.344) + (array[:, :, 1] / 1.704)\
        + (array[:, :, 2] / 8.772)
    return (res)


def main():
    try:
        # Loading the image
        array = ft_load("landscape.jpeg")
        print(array)
        # Apply invert and display the result

        plt.imshow(ft_invert(array))
        plt.title('Inverted')
        plt.show()

        # Apply red and display the result
        plt.imshow(ft_red(array))
        plt.title('Red')
        plt.show()

        # Apply green and display the result
        plt.imshow(ft_green(array))
        plt.title('Green')
        plt.show()

        # Apply blue and display the result
        plt.imshow(ft_blue(array))
        plt.title('Blue')
        plt.show()

        # Apply grey and display the result
        plt.imshow(ft_grey(array), cmap='gray')  # Grayscale image needs a
        # gray colormap
        plt.title('Grey')
        plt.show()

        print(ft_invert.__doc__)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)
    return (0)


if __name__ == "__main__":
    main()
