from PIL import Image
from utility import calculate_image_similarity, apply_and_check, apply_and_check_3x3

THRESHOLD = 0.97


def solve(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)

    similarity = calculate_image_similarity(A, B)

    if similarity > 0.96:
        C = imageMap.get(image_to_compare_answers_with)
        similarity_C, best_answer = apply_and_check(C, imageMap)
        return best_answer

    return -1


def solve_3x3(imageMap, group_1, group_2, group_3):

    last_label = group_1[0]
    for i in range(len(group_1) - 1):
        current_label = group_1[i + 1]
        last_image = imageMap.get(last_label)
        current_image = imageMap.get(current_label)
        similarity = calculate_image_similarity(last_image, current_image)
        if similarity < THRESHOLD:
            return -1
    # -------------------
    last_label = group_2[0]
    for i in range(len(group_2) - 1):
        current_label = group_2[i + 1]
        last_image = imageMap.get(last_label)
        current_image = imageMap.get(current_label)
        similarity = calculate_image_similarity(last_image, current_image)
        if similarity < THRESHOLD:
            return -1

    group_3_image_one = imageMap.get(group_3[0])
    group_3_image_two = imageMap.get(group_3[1])

    similarity = calculate_image_similarity(group_3_image_one, group_3_image_two)

    if similarity < THRESHOLD:
        return -1

    similarity, best_answer = apply_and_check_3x3(group_3_image_two, imageMap)

    if similarity > THRESHOLD:
        return best_answer


    pass
