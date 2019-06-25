from PIL import Image
from utility import calculate_image_similarity, apply_and_check_3x3
import numpy as np

THRESHOLD = 0.97


def solve_3x3(imageMap):

    image_A = imageMap.get('A')
    image_B = imageMap.get('B')
    image_C = imageMap.get('C')
    image_D = imageMap.get('D')
    image_F = imageMap.get('F')
    image_G = imageMap.get('G')
    image_H = imageMap.get('H')

    # row 1
    image_A.save("image_A.png")
    result = translate(image_A)
    similarity = calculate_image_similarity(image_C, result)
    if similarity > 0.97:
        return -1

    # result = translate(image_G)
    # similarity, best_answer = apply_and_check_3x3(result, imageMap)
    #
    # if similarity > 0.97:
    #     return best_answer

    return -1


def translate(image_1):
    image_1.save("image_1.png")
    image_1 = np.array(image_1)

    height, width = image_1.shape

    first_half = image_1[:, 0:int(width/2)]
    second_half = image_1[:, int(width/2):width]

    # padding = np.zeros((height, 10))
    # padding[:] = 255
    # second_half = np.hstack((padding, second_half))
    #
    # first_half = np.hstack((first_half, padding))

    swapped = np.hstack((second_half, first_half))

    new_image = Image.fromarray(swapped, mode="L")
    new_image.save("translate.png")



    return new_image

