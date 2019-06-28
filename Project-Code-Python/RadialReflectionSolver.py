from PIL import Image
from utility import calculate_image_similarity, apply_and_check_3x3
import numpy as np

# C-07
def solve_3x3(imageMap):

    image_A = imageMap.get('A')
    image_B = imageMap.get('B')
    image_C = imageMap.get('C')
    image_D = imageMap.get('D')
    image_F = imageMap.get('F')
    image_G = imageMap.get('G')
    image_H = imageMap.get('H')

    horizontal_reflection_A = horizontal_reflection(image_A)
    similarity = calculate_image_similarity(horizontal_reflection_A, image_C)
    if similarity < 0.95:
        return -1

    horizontal_reflection_D = horizontal_reflection(image_D)
    similarity = calculate_image_similarity(horizontal_reflection_D, image_F)
    if similarity < 0.95:
        return -1

    vertical_reflection_A = vertical_reflection(image_A)
    similarity = calculate_image_similarity(vertical_reflection_A, image_G)
    if similarity < 0.95:
        return -1

    result = radial_reflection_transform(image_A)

    similarity, best_answer = apply_and_check_3x3(result, imageMap)
    return best_answer
    # if similarity > 0.88:


def horizontal_reflection(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def vertical_reflection(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)


# the black pixels of image_2 must be contained inside image 1
def radial_reflection_transform(image):
    height, width = image.size
    image_copy = image.copy()

    np_image = np.array(image)
    np_copy = np.array(image_copy)

    for i in range(height):
        for j in range(width):
            row_column_sum = i + j
            if row_column_sum < height:
                diff = height - row_column_sum - 1
                np_copy[i + diff][j + diff] = np_image[i][j]
            if row_column_sum > height:
                diff = row_column_sum % (height - 1)
                np_copy[i - diff][j - diff] = np_image[i][j]

    return Image.fromarray(np_copy, mode="L")



