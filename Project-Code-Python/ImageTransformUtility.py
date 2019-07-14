import numpy as np
from PIL import Image


def combine_dark_pixel_transform(image_1, image_2):
    height, width = image_1.size
    image_1 = np.array(image_1)
    image_2 = np.array(image_2)
    new_image = np.zeros((height, width), dtype=np.uint8)
    new_image[:] = 255

    for i in range(height):
        for j in range(width):
            if image_1[i][j] < 100 or image_2[i][j] < 100:
                new_image[i][j] = 0

    return Image.fromarray(new_image, mode="L")

def subtract_dark_pixels(image_1, image_2):
    height, width = image_1.size
    image_1 = np.array(image_1)
    image_2 = np.array(image_2)
    new_image = np.array(image_2)

    for i in range(height):
        for j in range(width):
            if image_1[i][j] < 100:
                new_image[i][j] = flip_pixel_value(image_2[i][j])

    return Image.fromarray(new_image, mode="L")

# returns a new image with the black pixels representing the similarity between 1 & 2
def similar_dark_pixels_transform(image_1, image_2):
    image_1 = np.array(image_1)
    image_2 = np.array(image_2)
    height, width = image_1.shape
    new_image = np.zeros((height, width), dtype=np.uint8)
    new_image[:] = 255

    for i in range(height):
        for j in range(width):
            if image_1[i][j] < 100 and image_2[i][j] < 100:
                new_image[i][j] = 0

    return Image.fromarray(new_image, mode="L")


def flip_pixel_value(pixel):
    if pixel > 100:
        return 0
    else:
        return 255
