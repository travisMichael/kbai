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

    expected_xor, s_1, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1_1, image_1_2, image_1_3])
    actual_result_2, s_2, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_2_1, image_2_2, image_2_3])

    # expected_xor.save("xor.png")
    # actual_result_2.save("actual.png")
    # s_1.save("s_1.png")
    # s_2.save("s_2.png")

    similarity = calculate_image_similarity(expected_xor, actual_result_2)

    if similarity < 0.95:
        return -1

    image_3_1 = np.array(imageMap.get(groupings[2][0]))
    image_3_2 = np.array(imageMap.get(groupings[2][1]))

    best_answer = -1
    best_similarity = 1.88

    _, expected_matching_pixels, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2])
    for i in range (1, 9):
        similarity = check_answer_similarity(expected_xor, expected_matching_pixels, imageMap, str(i), image_3_1, image_3_2)
        if similarity > best_similarity:
            best_similarity = similarity
            best_answer = i

    return best_answer

def solve_3x3_match_only(imageMap, groupings):

    image_1_1 = np.array(imageMap.get(groupings[0][0]))
    image_1_2 = np.array(imageMap.get(groupings[0][1]))
    image_1_3 = np.array(imageMap.get(groupings[0][2]))

    image_2_1 = np.array(imageMap.get(groupings[1][0]))
    image_2_2 = np.array(imageMap.get(groupings[1][1]))
    image_2_3 = np.array(imageMap.get(groupings[1][2]))

    _, s_1, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1_1, image_1_2])
    _, s_2, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1_1, image_1_2, image_1_3])

    _, s_1, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_2_1, image_2_2])
    _, s_2, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_2_1, image_2_2, image_2_3])

    similarity = calculate_image_similarity(s_1, s_2)

    if similarity < 0.95:
        return -1

    image_3_1 = np.array(imageMap.get(groupings[2][0]))
    image_3_2 = np.array(imageMap.get(groupings[2][1]))

    potential_answers = []

    _, expected_matching_pixels, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2])
    for i in range (1, 9):
        similarity, meta = check_answer_similarity_matching_only(expected_matching_pixels, imageMap, str(i), image_3_1, image_3_2)
        if similarity > 0.95:
            potential_answers.append({'label': i, 'meta': meta})

    best_answer = -1
    lowest_number_of_dark_pixels = 100000
    for i in range(len(potential_answers)):
        number_of_dark_pixels = potential_answers[i].get('meta').get('number_of_almost_matching_pixels')
        label = potential_answers[i].get('label')
        if number_of_dark_pixels < lowest_number_of_dark_pixels:
            lowest_number_of_dark_pixels = number_of_dark_pixels
            best_answer = label

    return best_answer


def check_answer_similarity_matching_only(expected_matching_pixels, imageMap, image_label, image_3_1, image_3_2):


    image = np.array(imageMap.get(image_label))

    similarity = calculate_image_similarity(image_3_1, image)
    if similarity > 0.97:
        return 0.0, None
    similarity = calculate_image_similarity(image_3_2, image)
    if similarity > 0.97:
        return 0.0, None

    final_result, matching_pixels, meta = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image])
    # if meta.get('number_of_almost_matching_pixels') > 100:
    #     return 0.0
    return calculate_image_similarity(matching_pixels, expected_matching_pixels), meta


def check_answer_similarity(expected_xor, expected_matching_pixels, imageMap, image_label, image_3_1, image_3_2):

    image = np.array(imageMap.get(image_label))

    final_result, matching_pixels, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_3_1, image_3_2, image])
    similarity_1 = calculate_image_similarity(expected_xor, final_result)
    similarity_2 = calculate_image_similarity(matching_pixels, expected_matching_pixels)

    return similarity_1 + similarity_2
