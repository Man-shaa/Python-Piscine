from PIL import Image
import numpy as np


def ft_load(path: str):
    """Load an image from the specified file path, ensure it's in JPEG or\
    JPG format,
    convert it to RGB mode if necessary, and return its pixel data as a\
    NumPy array."""
    try:
        image = Image.open(path)
        if image.format not in ['JPEG', 'JPG']:
            raise ValueError("The image format should be JPG or JPEG")
        print("The format of the image is:", image.format)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image_array = np.array(image)
        print("The shape of the image is:", image_array.shape)
        return image_array

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)
