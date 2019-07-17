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

    result = translate(image_A)
    if result is None:
        return -1
    similarity = calculate_image_similarity(image_C, result)
    if similarity < 0.95:
        return -1

    result = translate(image_D)
    similarity = calculate_image_similarity(image_F, result)
    if similarity < 0.95:
        return -1

    result = translate(image_G)
    similarity, best_answer = apply_and_check_3x3(result, imageMap)

    return best_answer


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


def translate(image_1):
    image_1 = np.array(image_1)

    height, width = image_1.shape

    first_half = image_1[:, 0:int(width/2)]
    second_half = image_1[:, int(width/2):width-0]

    first_index, bounding_box, last_index = get(first_half)
    first_index_2, bounding_box_2, last_index_2 = get(second_half)

    if first_index is None or first_index_2 is None:
        return None

    slim_padding_left = np.zeros((height, first_index), dtype=np.uint8)
    slim_padding_left_middle = np.zeros((height, last_index), dtype=np.uint8)
    slim_padding_right_middle = np.zeros((height, first_index_2), dtype=np.uint8)
    slim_padding_right = np.zeros((height, last_index_2), dtype=np.uint8)
    slim_padding_left[:] = 255
    slim_padding_left_middle[:] = 255
    slim_padding_right_middle[:] = 255
    slim_padding_right[:] = 255

    first_half = np.hstack((slim_padding_left, bounding_box_2))
    first_half = np.hstack((first_half, slim_padding_left_middle))

    second_half = np.hstack((slim_padding_right_middle, bounding_box))
    second_half = np.hstack((second_half, slim_padding_right))

    reflected_halves = np.hstack((first_half, second_half))

    new_image = Image.fromarray(reflected_halves, mode="L")

    return new_image

