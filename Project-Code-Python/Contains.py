from PIL import Image
from utility import calculate_image_similarity, apply_and_check_3x3
import numpy as np

THRESHOLD = 0.97


def solve_3x3(imageMap):

    image_A = imageMap.get('A')
    image_B = imageMap.get('B')
    image_C = imageMap.get('C')
    image_D = imageMap.get('D')
    image_F = imageMap.get('F')
    image_G = imageMap.get('G')
    image_H = imageMap.get('H')

    result = is_horizontally_contained(image_B, image_A)
    if not result:
        return -1

    result = is_horizontally_contained(image_C, image_B)
    if not result:
        return -1

    result = is_horizontally_contained(image_D, image_A)
    if not result:
        return -1

    result = is_horizontally_contained(image_G, image_D)
    if not result:
        return -1


    result_2 = is_horizontally_contained(image_A, image_B)

    return 5




def find_index_of_first_black_pixel(array, start_from_right_side):
    length = len(array)
    if start_from_right_side:
        for i in range(len(array) - 1, -1, -1):
            if array[i] == 0:
                return i
            pass
        return i
    else:
        for i in range(len(array)):
            if array[i] == 0:
                return i
        return i


# the black pixels of image_2 must be contained inside image 1
def is_horizontally_contained(image_1, image_2):
    height, width = image_1.size

    np_image_1 = np.array(image_1)
    np_image_2 = np.array(image_2)

    for i in range(height):
        # left to right check
        index_left_1 = find_index_of_first_black_pixel(np_image_1[i], False)
        index_left_2 = find_index_of_first_black_pixel(np_image_2[i], False)
        index_right_1 = find_index_of_first_black_pixel(np_image_1[i], True)
        index_right_2 = find_index_of_first_black_pixel(np_image_2[i], True)

        if index_left_1 > index_left_2:
            return False
        if index_right_1 < index_right_2:
            return False
    return True
