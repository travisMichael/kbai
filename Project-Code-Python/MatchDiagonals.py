from PIL import Image
from utility import calculate_image_similarity, apply_and_check, apply_and_check_3x3

THRESHOLD = 0.95


# def solve(imageMap, compared_to_A, image_to_compare_answers_with):
#
#     A = imageMap.get('A')
#     B = imageMap.get(compared_to_A)
#
#     similarity = calculate_image_similarity(A, B)
#
#     if similarity > 0.96:
#         C = imageMap.get(image_to_compare_answers_with)
#         similarity_C, best_answer = apply_and_check(C, imageMap)
#         return best_answer
#
#     return -1


# C-01
def solve_3x3(imageMap):

    A = imageMap.get('A')
    E = imageMap.get('E')

    similarity = calculate_image_similarity(A, E)

    if similarity < THRESHOLD:
        return -1

    similarity, best_answer = apply_and_check(E, imageMap)

    if similarity > THRESHOLD:
        return best_answer

    return -1
