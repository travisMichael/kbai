from PIL import Image
from utility import calculate_image_similarity, apply_and_check_3x3
import numpy as np
import math

THRESHOLD = 0.97


def solve_3x3(imageMap):

    image_A = imageMap.get('A')
    image_B = imageMap.get('B')
    image_C = imageMap.get('C')
    image_D = imageMap.get('D')
    image_F = imageMap.get('F')
    image_G = imageMap.get('G')
    image_H = imageMap.get('H')

    black_pixels_in_A = calculate_number_of_black_pixels(image_A)
    black_pixels_in_B = calculate_number_of_black_pixels(image_B)

    diff = abs(black_pixels_in_A - black_pixels_in_B)

    if diff > 1000:
        return -1

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

    image_1 = imageMap.get('1')
    result = is_horizontally_contained(image_1, image_H)
    if result:
        return 1

    image_2 = imageMap.get('2')
    result = is_horizontally_contained(image_2, image_H)
    if result:
        return 2

    image_3 = imageMap.get('3')
    result = is_horizontally_contained(image_3, image_H)
    if result:
        return 3

    image_4 = imageMap.get('4')
    result = is_horizontally_contained(image_4, image_H)
    if result:
        return 4

    image_5 = imageMap.get('5')
    result = is_horizontally_contained(image_5, image_H)
    if result:
        return 5

    image_6 = imageMap.get('6')
    result = is_horizontally_contained(image_6, image_H)
    if result:
        return 6

    image_7 = imageMap.get('7')
    result = is_horizontally_contained(image_7, image_H)
    if result:
        return 7

    image_8 = imageMap.get('8')
    result = is_horizontally_contained(image_8, image_H)
    if result:
        return 8

    return -1


def calculate_number_of_black_pixels(image):
    np_image = np.array(image)
    height, width = np_image.shape
    number_of_black_pixels = 0
    for i in range(height):
        for j in range(width):
            if np_image[i][j] == 0:
                number_of_black_pixels += 1
    return number_of_black_pixels


def find_index_of_first_black_pixel(array, start_from_right_side):
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


def calculate_is_same(array_1, array_2, left_index, right_index):

    if right_index < left_index:
        return True

    number_of_different_pixels = 0
    if right_index - left_index > 10:
        for i in range(left_index + 5, right_index - 4):
            if array_1[i] != array_2[i]:
                number_of_different_pixels += 1

    if number_of_different_pixels > 5:
        return False

    return True


# the black pixels of image_2 must be contained inside image 1
def is_horizontally_contained(image_1, image_2):
    height, width = image_1.size

    np_image_1 = np.array(image_1)
    np_image_2 = np.array(image_2)
    is_same = True

    for i in range(height):
        # left to right check
        index_left_1 = find_index_of_first_black_pixel(np_image_1[i], False)
        index_left_2 = find_index_of_first_black_pixel(np_image_2[i], False)
        index_right_1 = find_index_of_first_black_pixel(np_image_1[i], True)
        index_right_2 = find_index_of_first_black_pixel(np_image_2[i], True)
        if 85 < i and i < 100:
            is_same = calculate_is_same(np_image_1[i], np_image_2[i], index_left_2, index_right_2)

        if not is_same:
            return False
        if index_left_1 > index_left_2:
            return False
        if index_right_1 < index_right_2:
            return False
    return True
