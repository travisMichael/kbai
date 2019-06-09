from PIL import Image
from utility import calculate_image_similarity, apply_and_check


def solve_rotate_90(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)

    rotated_A = A.transpose(Image.ROTATE_90)

    similarity = calculate_image_similarity(rotated_A, B)

    if similarity > 0.97:
        C = imageMap.get(image_to_compare_answers_with)
        rotated_C = C.transpose(Image.ROTATE_90)
        similarity_C, best_answer = apply_and_check(rotated_C, imageMap)
        return best_answer

    return -1

def solve_rotate_270(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)

    rotated_A = A.transpose(Image.ROTATE_270)

    similarity = calculate_image_similarity(rotated_A, B)

    if similarity > 0.97:
        C = imageMap.get(image_to_compare_answers_with)
        rotated_C = C.transpose(Image.ROTATE_270)
        similarity_C, best_answer = apply_and_check(rotated_C, imageMap)
        return best_answer

    return -1
