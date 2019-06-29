import numpy as np
# from PIL import Image


# returns a value from 0-1. 0 = no similarity, 1 = exactly similar
def calculate_image_similarity(image_1, image_2):
    image_1 = np.array(image_1)
    image_2 = np.array(image_2)
    number_of_pixels_different = 0
    for i in range(184):
        for j in range(184):
            if image_1[i][j] != image_2[i][j]:
                number_of_pixels_different += 1

    x, y = image_1.shape
    total = x * y
    return (total - number_of_pixels_different) / total


def calculate_pixel_ratio(image):
    image = np.array(image)
    white_pixels = 0
    black_pixels = 0
    for i in range(184):
        for j in range(184):
            if image[i][j] == 255:
                white_pixels += 1
            if image[i][j] == 0:
                black_pixels += 1
    pixel_object = {'black_pixels': black_pixels, 'white_pixels': white_pixels}

    ratio = 0.0
    if black_pixels != 0 and white_pixels != 0:
        if black_pixels > white_pixels:
            ratio = white_pixels / black_pixels
        else:
            ratio = black_pixels / white_pixels

    pixel_object['ratio'] = ratio
    return pixel_object


def calculate_pixel_ratio_map(image_map):

    pixel_ratio_map = {}

    pixel_ratio_map['A'] = calculate_pixel_ratio(image_map.get('A'))
    pixel_ratio_map['B'] = calculate_pixel_ratio(image_map.get('B'))
    pixel_ratio_map['C'] = calculate_pixel_ratio(image_map.get('C'))
    pixel_ratio_map['D'] = calculate_pixel_ratio(image_map.get('D'))
    pixel_ratio_map['E'] = calculate_pixel_ratio(image_map.get('E'))
    pixel_ratio_map['F'] = calculate_pixel_ratio(image_map.get('F'))
    pixel_ratio_map['G'] = calculate_pixel_ratio(image_map.get('G'))
    pixel_ratio_map['H'] = calculate_pixel_ratio(image_map.get('H'))
    pixel_ratio_map['1'] = calculate_pixel_ratio(image_map.get('1'))
    pixel_ratio_map['2'] = calculate_pixel_ratio(image_map.get('2'))
    pixel_ratio_map['3'] = calculate_pixel_ratio(image_map.get('3'))
    pixel_ratio_map['4'] = calculate_pixel_ratio(image_map.get('4'))
    pixel_ratio_map['5'] = calculate_pixel_ratio(image_map.get('5'))
    pixel_ratio_map['6'] = calculate_pixel_ratio(image_map.get('6'))
    pixel_ratio_map['7'] = calculate_pixel_ratio(image_map.get('7'))
    pixel_ratio_map['8'] = calculate_pixel_ratio(image_map.get('8'))

    return pixel_ratio_map


# return the similarity between C and D after C has been calculated by the operators
def apply_and_check(convertedImage, imageMap):

    similarity = 0.0
    bestImageChoice = -1
    for i in range(6):
        temp_similarity = calculate_image_similarity(convertedImage, imageMap.get(str(i+1)))
        if temp_similarity > similarity:
            similarity = temp_similarity
            bestImageChoice = i+1

    return similarity, bestImageChoice

def apply_and_check_3x3(convertedImage, imageMap):

    similarity = 0.0
    bestImageChoice = -1
    for i in range(8):
        temp_similarity = calculate_image_similarity(convertedImage, imageMap.get(str(i+1)))
        if temp_similarity > similarity:
            similarity = temp_similarity
            bestImageChoice = i+1

    return similarity, bestImageChoice


def find_answer_with_same_similarity(convertedImage, imageMap, similarity_to_target):

    # similarity = 0.0
    # bestImageChoice = -1
    for i in range(6):
        temp_similarity = calculate_image_similarity(convertedImage, imageMap.get(str(i+1)))
        if is_close(temp_similarity, similarity_to_target):
            return i + 1

    return None


def is_close(value_1, value_2):
    if value_1 + 0.001 <  value_2 and value_1 - 0.001 < value_2:
        return True
    return False

