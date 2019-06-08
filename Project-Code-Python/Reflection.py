from PIL import Image
from utility import calculate_image_similarity, apply_and_check


def solve_horizontal(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)

    reflected_A = A.transpose(Image.FLIP_LEFT_RIGHT)

    similarity = calculate_image_similarity(reflected_A, B)

    if similarity > 0.95:
        C = imageMap.get(image_to_compare_answers_with)
        reflected_C = C.transpose(Image.FLIP_LEFT_RIGHT)
        similarity_C, best_answer = apply_and_check(reflected_C, imageMap)
        return best_answer

    return -1

def solve_vertical(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)

    reflected_A = A.transpose(Image.FLIP_TOP_BOTTOM)

    similarity = calculate_image_similarity(reflected_A, B)

    if similarity > 0.99:
        C = imageMap.get(image_to_compare_answers_with)
        reflected_C = C.transpose(Image.FLIP_TOP_BOTTOM)
        similarity_C, best_answer = apply_and_check(reflected_C, imageMap)
        return best_answer

    return -1
