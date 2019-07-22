from PIL import Image, ImageChops, ImageOps
from utility import calculate_image_similarity, apply_and_check, apply_and_check_3x3
import ImageTransformUtility
import numpy as np


# ImageOps.invert(convertedImage)
# todo Make this more generic by also accounting for subtracting first
def solve(imageMap, compared_to_A, image_to_compare_answers_with):
    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)
    C = imageMap.get(image_to_compare_answers_with)

    difference = ImageChops.subtract(B, A)
    # difference2 = ImageChops.subtract(B, A)
    # difference.save('diff.png')

    # temp_image = ImageOps.invert(difference)

    new_image_A = transform(A, difference, False)
    # new_image_A.save('A_new.png')

    similarity = calculate_image_similarity(new_image_A, B)

    if similarity > 0.99:

        transformed_image = transform(C, difference, True)
        # transformed_image.save('transform.png')
        # new_image = transform(transform_image, difference2, False)

        similarity, answer = apply_and_check(transformed_image, imageMap)

        if similarity > 0.98:
            return answer

    return -1


def solve_3x3_exclusive_or(imageMap, groupings, expected_results, group_to_check):

    if len(groupings) != len(expected_results):
        return -1

    for i in range(len(groupings)):
        image_1 = np.array(imageMap.get(groupings[i][0]))
        image_2 = np.array(imageMap.get(groupings[i][1]))
        expected_result = imageMap.get(expected_results[i])

        actual_result, _, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1, image_2])
        # actual_result.save('actual_result.png')

        similarity = calculate_image_similarity(actual_result, expected_result)

        if similarity < 0.95:
            return -1

    image_1 = np.array(imageMap.get(group_to_check[0]))
    image_2 = np.array(imageMap.get(group_to_check[1]))
    final_result, _, _ = ImageTransformUtility.dark_pixel_exclusive_or_transform([image_1, image_2])
    # final_result.save('final_result.png')

    similarity, best_answer = apply_and_check_3x3(final_result, imageMap)

    if similarity > 0.95:
        return best_answer

    return -1


def solve_3x3(imageMap, groupings, expected_results, group_to_check):

    if len(groupings) != len(expected_results):
        return -1

    for i in range(len(groupings)):
        image_1 = imageMap.get(groupings[i][0])
        image_2 = imageMap.get(groupings[i][1])
        expected_result = imageMap.get(expected_results[i])

        actual_result = ImageTransformUtility.dark_pixel_subtraction_transform(image_1, image_2)

        similarity = calculate_image_similarity(actual_result, expected_result)

        if similarity < 0.92:
            return -1

    image_1 = imageMap.get(group_to_check[0])
    image_2 = imageMap.get(group_to_check[1])
    final_result = ImageTransformUtility.dark_pixel_subtraction_transform(image_1, image_2)

    similarity, best_answer = apply_and_check_3x3(final_result, imageMap)

    if similarity > 0.92:
        return best_answer

    return -1


def transform(image_to_transform, difference, ab_add):
    height, width = image_to_transform.size
    transform = image_to_transform.copy()

    for i in range(height):
        for j in range(width):
            if difference.getpixel((i,j)) == 255:
                flip_pixel(i, j, transform)

    return transform


def flip_pixel(i, j, image):
    pixel = image.getpixel((i,j))
    if pixel == 255:
        image.putpixel((i, j), 0)
    elif pixel == 0:
        image.putpixel((i, j), 255)
    else:
        # print("should not be here", image.getpixel((i,j)))
        pass
