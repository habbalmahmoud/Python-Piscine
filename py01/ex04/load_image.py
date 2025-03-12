from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """loads an image, prints its format, and its pixels
content in RGB format."""
    try:
        with Image.open(path) as img:
            if img.format not in ['JPEG', 'JPG']:
                raise TypeError("Invalid Format")
            rgb = img.convert("RGB")
            arr = np.array(rgb)
            print("The shape of the image is:", arr.shape)
            return arr
    except Exception as e:
        print(e)
        exit(1)
