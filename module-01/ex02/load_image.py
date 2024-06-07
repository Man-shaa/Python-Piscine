from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image from the specified file path, ensure it's in JPEG or JPG \
    format, convert it to RGB mode if necessary, and return its pixel data as \
    a NumPy array."""
    image = Image.open(path)
    if image.format not in ['JPEG', 'JPG']:
        raise TypeError("The image format should be JPG or JPEG")
    print("The format of the image is:", image.format)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    print("The shape of the image is:", image_array.shape)
    print(image_array)
    return image_array


def main():
    image_path = "landscape.jpg"
    try:
        ft_load(image_path)
    except Exception as e:
        print(type(e).__name__ + ":", e)
        return (1)


if __name__ == "__main__":
    main()
