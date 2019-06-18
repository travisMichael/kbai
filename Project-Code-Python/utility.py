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

