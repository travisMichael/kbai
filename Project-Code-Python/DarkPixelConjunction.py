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
