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

    # row 1
    result = is_proper_subset(image_B, image_C)
    if not result:
        return -1
    result = is_proper_subset(image_A, image_B)
    if not result:
        return -1
    result = is_proper_subset(image_C, image_F)
    if not result:
        return -1
    # row 2
    result = is_proper_subset(image_D, image_G)
    if not result:
        return -1
    result = is_proper_subset(image_A, image_D)
    if not result:
        return -1

    # check answers ----------------------------
    answer = -1
    answers = []
    image_1 = imageMap.get('1')
    result = is_proper_subset(image_H, image_1)
    result_2 = is_proper_subset(image_F, image_1)
    if result and result_2:
        answers.append(1)
        answer = 1

    image_2 = imageMap.get('2')
    result = is_proper_subset(image_H, image_2)
    result_2 = is_proper_subset(image_F, image_2)
    if result and result_2:
        answers.append(1)
        answer = 2

    image_3 = imageMap.get('3')
    result = is_proper_subset(image_H, image_3)
    result_2 = is_proper_subset(image_F, image_3)
    if result and result_2:
        answers.append(1)
        answer = 3

    image_4 = imageMap.get('4')
    result = is_proper_subset(image_H, image_4)
    result_2 = is_proper_subset(image_F, image_4)
    if result and result_2:
        answers.append(1)
        answer = 4

    image_5 = imageMap.get('5')
    result = is_proper_subset(image_H, image_5)
    result_2 = is_proper_subset(image_F, image_5)
    if result and result_2:
        answers.append(1)
        answer = 5

    image_6 = imageMap.get('6')
    result = is_proper_subset(image_H, image_6)
    result_2 = is_proper_subset(image_F, image_6)
    if result and result_2:
        answers.append(1)
        answer = 6

    image_7 = imageMap.get('7')
    result = is_proper_subset(image_H, image_7)
    result_2 = is_proper_subset(image_F, image_7)
    if result and result_2:
        answers.append(1)
        answer = 7

    image_8 = imageMap.get('8')
    result = is_proper_subset(image_H, image_8)
    result_2 = is_proper_subset(image_F, image_8)
    if result and result_2:
        answers.append(1)
        answer = 8

    if len(answers) > 1:
        print("more than one answer found!!")
        return -1
    return answer


def is_proper_subset(image_1, image_2):
    height, width = image_1.size

    number_of_pixels = 0

    np_image_1 = np.array(image_1)
    np_image_2 = np.array(image_2)

    for i in range(height):
        for j in range(width):
            if np_image_1[i][j] == 0 and np_image_2[i][j] == 255:
                number_of_pixels += 1

    if number_of_pixels > 10:
        return False

    return True

