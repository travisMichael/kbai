from PIL import Image
from utility import calculate_image_similarity, apply_and_check_3x3
import numpy as np
import math

THRESHOLD = 0.93


def solve_3x3(imageMap):

    image_A = imageMap.get('A')
    image_B = imageMap.get('B')
    image_C = imageMap.get('C')
    image_D = imageMap.get('D')
    image_F = imageMap.get('F')
    image_G = imageMap.get('G')
    image_H = imageMap.get('H')
    #
    # print("first index", first_index(np.array(image_F)))
    # print("first index", first_index(np.array(image_C)))
    # print("last index", last_index(np.array(image_F)))
    # print("last index", last_index(np.array(image_C)))

    result = translate(image_A)
    if result is None:
        return -1
    similarity = calculate_image_similarity(image_C, result)
    if similarity < THRESHOLD:
        return -1

    result = translate(image_D)
    if result is None:
        return -1
    similarity = calculate_image_similarity(image_F, result)
    if similarity < THRESHOLD:
        return -1

    result = translate(image_G)
    if result is None:
        return -1
    similarity, best_answer = apply_and_check_3x3(result, imageMap)

    if similarity > THRESHOLD - 0.03:
        return best_answer

    return -1


def first_index(image):
    height, width = image.shape

    for i in range(width):
        column = image[:, i]
        minimum = np.amin(column)
        if minimum == 0:
            return i

    return -1


def last_index(image):
    height, width = image.shape

    for i in range(width-1, -1, -1):
        column = image[:, i]
        minimum = np.amin(column)
        if minimum == 0:
            return i

    return -1


def get(image):
    height, width = image.shape
    first_index = 0
    image_slice = None
    for i in range(width):
        column = image[:, i]
        minimum = np.amin(column)
        column = np.expand_dims(column, axis=1)
        if minimum == 0:
            if image_slice is None:
                first_index = i
                image_slice = column
            else:
                image_slice = np.hstack((image_slice, column))
        else:
            if image_slice is not None:
                return first_index, image_slice, width - i
    return None, None, None


def rest_of_image_is_white(image, begin_from):
    return True


def translate(image_1):
    image_1 = np.array(image_1)

    height, width = image_1.shape

    first_index, bounding_box, last_index = get(image_1)

    if first_index is None:
        return None

    bb_height, bb_width = bounding_box.shape

    padding = width - (bb_width * 2) - 16

    if padding < 1:
        return None

    rest_is_white = rest_of_image_is_white(image_1, 30)

    if not rest_is_white:
        return None

    slim_padding_left = np.zeros((height, 8), dtype=np.uint8)
    slim_padding_middle = np.zeros((height, padding), dtype=np.uint8)
    slim_padding_right = np.zeros((height, 8), dtype=np.uint8)
    slim_padding_left[:] = 255
    slim_padding_middle[:] = 255
    slim_padding_right[:] = 255

    result = np.hstack((slim_padding_left, bounding_box))
    result = np.hstack((result, slim_padding_middle))
    result = np.hstack((result, bounding_box))
    result = np.hstack((result, slim_padding_right))

    new_image = Image.fromarray(result, mode="L")

    return new_image

