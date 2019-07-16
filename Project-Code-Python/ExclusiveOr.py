from utility import calculate_image_similarity, apply_and_check_3x3
import ImageTransformUtility
import numpy as np

THRESHOLD = 0.97


def solve_3x3(imageMap, groupings):
    #
    # if len(groupings) != len(expected_results):
    #     return -1

    image_1_1 = np.array(imageMap.get(groupings[0][0]))
    image_1_2 = np.array(imageMap.get(groupings[0][1]))
    image_1_3 = np.array(imageMap.get(groupings[0][2]))

    image_2_1 = np.array(imageMap.get(groupings[1][0]))
    image_2_2 = np.array(imageMap.get(groupings[1][1]))
    image_2_3 = np.array(imageMap.get(groupings[1][2]))

    actual_result_1 = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1_1, image_1_2, image_1_3])
    actual_result_2 = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_2_1, image_2_2, image_2_3])

    similarity = calculate_image_similarity(actual_result_1, actual_result_2)

    if similarity < 0.95:
        return -1

    image_3_1 = np.array(imageMap.get(groupings[2][0]))
    image_3_2 = np.array(imageMap.get(groupings[2][1]))

    image_1 = np.array(imageMap.get('1'))
    image_2 = np.array(imageMap.get('2'))
    image_3 = np.array(imageMap.get('3'))
    image_4 = np.array(imageMap.get('4'))
    image_5 = np.array(imageMap.get('5'))
    image_6 = np.array(imageMap.get('6'))
    image_7 = np.array(imageMap.get('7'))
    image_8 = np.array(imageMap.get('8'))

    best_answer = -1
    best_similarity = 0.9

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_1])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 1

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_2])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 2

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_3])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 3

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_4])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 4

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_5])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 5

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_6])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 6

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_7])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_similarity = similarity
        best_answer = 7

    final_result = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image_8])
    similarity = calculate_image_similarity(actual_result_1, final_result)

    if similarity > best_similarity:
        best_answer = 8

    return best_answer
