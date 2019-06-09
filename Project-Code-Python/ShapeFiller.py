from PIL import Image, ImageDraw
from utility import calculate_image_similarity, apply_and_check


# todo Make this more generic by also accounting for inverted images
def solve(imageMap, compared_to_A, image_to_compare_answers_with):

    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)
    # A.save('A.png')

    height, width = A.size
    if A.getpixel((height/2, width/2)) == 0:
        return -1

    A_transformed = transform(A)

    similarity = calculate_image_similarity(A_transformed, B)

    if similarity > 0.95:
        C = imageMap.get(image_to_compare_answers_with)
        C_transformed = transform(C)
        similarity_C, best_answer = apply_and_check(C_transformed, imageMap)
        return best_answer

    return -1


def transform(image):
    height, width = image.size
    copy = image.copy()

    ImageDraw.floodfill(copy, (height/2, width/2), 0)
    copy.save('filled.png')

    return copy

