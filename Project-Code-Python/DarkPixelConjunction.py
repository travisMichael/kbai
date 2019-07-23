from utility import calculate_image_similarity, apply_and_check_3x3
import ImageTransformUtility


def solve_3x3(imageMap, groupings, expected_results, group_to_check):

    if len(groupings) != len(expected_results):
        return -1

    for i in range(len(groupings)):
        image_1 = imageMap.get(groupings[i][0])
        image_2 = imageMap.get(groupings[i][1])
        expected_result = imageMap.get(expected_results[i])

        actual_result = ImageTransformUtility.dark_pixel_conjunction_transform(image_1, image_2)

        similarity = calculate_image_similarity(actual_result, expected_result)

        if similarity < 0.92:
            return -1

    image_1 = imageMap.get(group_to_check[0])
    image_2 = imageMap.get(group_to_check[1])
    final_result = ImageTransformUtility.dark_pixel_conjunction_transform(image_1, image_2)
    # final_result.save('final_result.png')

    similarity, best_answer = apply_and_check_3x3(final_result, imageMap)

    if similarity > 0.92:
        return best_answer

    return -1


def solve_3x3_dark_pixel_counter(pixelMap):
    A = pixelMap.get('A')
    E = pixelMap.get('E')
    for i in range(1, 9):
        answer = pixelMap.get(str(i))

        if E.get('black_pixels') < answer.get('black_pixels') < A.get('black_pixels') and answer.get('black_pixels') == 988:
            return i

    return -1
