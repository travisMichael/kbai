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

    best_answer = -1
    best_similarity = 0.5

    horizontal_reflection_G = horizontal_reflection(image_G)

    for i in range(1, 9):
        similarity = calculate_image_similarity(horizontal_reflection_G, imageMap.get(str(i)))
        if similarity > best_similarity:
            best_similarity = similarity
            best_answer = i

    return best_answer


def horizontal_reflection(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def vertical_reflection(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)


def calculate(imageMap, reflected_image, label):
    return calculate_image_similarity(reflected_image, imageMap.get(label))
# the black pixels of image_2 must be contained inside image 1
# def radial_reflection_transform(image):
#     height, width = image.size
#     image_copy = image.copy()
#
#     np_image = np.array(image)
#     np_copy = np.array(image_copy)
#
#     for i in range(height):
#         for j in range(width):
#             row_column_sum = i + j
#             if row_column_sum < height:
#                 diff = height - row_column_sum - 1
#                 np_copy[i + diff][j + diff] = np_image[i][j]
#             if row_column_sum > height:
#                 diff = row_column_sum % (height - 1)
#                 np_copy[i - diff][j - diff] = np_image[i][j]
#
#     return Image.fromarray(np_copy, mode="L")



