from utility import calculate_image_similarity, apply_and_check_3x3
import ImageTransformUtility
import numpy as np

THRESHOLD = 0.97


def solve_3x3(imageMap, groupings):

    image_1_1 = np.array(imageMap.get(groupings[0][0]))
    image_1_2 = np.array(imageMap.get(groupings[0][1]))
    image_1_3 = np.array(imageMap.get(groupings[0][2]))

    image_2_1 = np.array(imageMap.get(groupings[1][0]))
    image_2_2 = np.array(imageMap.get(groupings[1][1]))
    image_2_3 = np.array(imageMap.get(groupings[1][2]))

    expected_xor, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1_1, image_1_2, image_1_3])
    actual_result_2, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_2_1, image_2_2, image_2_3])

    similarity = calculate_image_similarity(expected_xor, actual_result_2)

    if similarity < 0.95:
        return -1

    image_3_1 = np.array(imageMap.get(groupings[2][0]))
    image_3_2 = np.array(imageMap.get(groupings[2][1]))


    best_answer = -1
    best_similarity = 1.88

    _, expected_matching_pixels = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2])
    for i in range (1, 9):
        similarity = check_answer_similarity(expected_xor, expected_matching_pixels, imageMap, str(i), image_3_1, image_3_2)
        if similarity > best_similarity:
            best_similarity = similarity
            best_answer = i



    return best_answer

def check_answer_similarity(expected_xor, expected_matching_pixels, imageMap, image_label, image_3_1, image_3_2):

    image = np.array(imageMap.get(image_label))

    final_result, matching_pixels = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image])
    similarity_1 = calculate_image_similarity(expected_xor, final_result)
    similarity_2 = calculate_image_similarity(matching_pixels, expected_matching_pixels)

    return similarity_1 + similarity_2
