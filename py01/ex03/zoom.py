from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """This program loads the image "animal.jpeg" using
ft_load from load_image.py,
prints information about it, and then displays a "zoomed" version of the image.

Specifically, it:
  • Prints the original image's size (in pixels) and channel count.
  • Prints the pixel content of the image.
  • Extracts (via slicing) a 400x400 region from the image and takes one
channel so that the new shape is (400, 400, 1).
  • Prints the new shape and pixel content of the zoomed region.
  • Displays the zoomed region with x and y axis scales.

If any error occurs, the program prints a clear error message without
stopping abruptly."""
    image_path = "animal.jpeg"
    img = ft_load(image_path)
    print(img)
    if img is None:
        print("Failed to load the image.")
        return

    try:
        img_array = np.array(img)
        height, width, channels = img_array.shape
        if height < 500 or width < 500:
            print("Error: The image is too small for the zoom region.")
            return

        zoom_region = img_array[100:500, 500:1000, :]
        zoom_region_single = zoom_region[:, :, 0:1]
        print(f"New shape after slicing: {zoom_region_single.shape} or {zoom_region_single.shape[0], zoom_region_single.shape[1]}")
        print(zoom_region_single)
        plt.figure(figsize=(8, 8))
        plt.imshow(zoom_region_single.squeeze(), cmap="gray")
        plt.title("Zoomed Image")
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.xticks(range(0, 401, 50))
        plt.yticks(range(0, 401, 50))
        plt.show()
    except Exception as e:
        print(f"Error during zooming process: {e}")


if __name__ == "__main__":
    main()
