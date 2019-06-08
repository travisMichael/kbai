from PIL import Image
from utility import calculate_image_similarity, apply_and_check


def solve(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)

    similarity = calculate_image_similarity(A, B)

    if similarity > 0.96:
        C = imageMap.get(image_to_compare_answers_with)
        similarity_C, best_answer = apply_and_check(C, imageMap)
        return best_answer

    return -1
