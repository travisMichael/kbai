from utility import calculate_image_similarity, apply_and_check_3x3
import ImageTransformUtility

THRESHOLD = 0.97


def solve_3x3_groupings(imageMap, groupings, expected_results, group_to_check):

    if len(groupings) != len(expected_results):
        return -1

    for i in range(len(groupings)):
        image_1 = imageMap.get(groupings[i][0])
        image_2 = imageMap.get(groupings[i][1])
        expected_result = imageMap.get(expected_results[i])

        actual_result = ImageTransformUtility.dark_pixel_inclusive_or_transform(image_1, image_2)

        similarity = calculate_image_similarity(actual_result, expected_result)

        if similarity < 0.95:
            return -1

    image_1 = imageMap.get(group_to_check[0])
    image_2 = imageMap.get(group_to_check[1])
    actual_result = ImageTransformUtility.dark_pixel_inclusive_or_transform(image_1, image_2)

    similarity, best_answer = apply_and_check_3x3(actual_result, imageMap)

    if similarity > 0.95:
        return best_answer

    return -1


# def solve_3x3(imageMap):
#
#     image_A = imageMap.get('A')
#     image_B = imageMap.get('B')
#     image_C = imageMap.get('C')
#     image_D = imageMap.get('D')
#     image_F = imageMap.get('F')
#     image_G = imageMap.get('G')
#     image_H = imageMap.get('H')
#
#     a_b_inclusion = inclusive_or_transform(image_A, image_B)
#     a_b_c_inclusion = inclusive_or_transform(a_b_inclusion, image_C)
#
#     d_g_inclusion = inclusive_or_transform(image_G, image_D)
#     a_b_c_d_g_inclusion = inclusive_or_transform(a_b_c_inclusion, d_g_inclusion)
#     # a_b_c_d_g_inclusion.save('abcdg.png')
#     result = inclusive_or_transform(image_F, image_H)
#     # result.save('result.png')
#
#     similarity = calculate_image_similarity(a_b_c_d_g_inclusion, result)
#
#     if similarity < THRESHOLD:
#         return -1
#
#     similarity, best_answer = apply_and_check_3x3(result, imageMap)
#
#     similarity_2, best_answer_2 = apply_and_check_3x3(a_b_c_d_g_inclusion, imageMap)
#
#     if similarity > THRESHOLD:
#         if similarity_2 > similarity:
#             return best_answer_2
#         return best_answer


# def inclusive_or_transform(image_1, image_2):
#     height, width = image_1.size
#     transform = image_1.copy()
#
#     for i in range(height):
#         for j in range(width):
#             if image_1.getpixel((i, j)) == 0 or image_2.getpixel((i, j)) == 0:
#                 transform.putpixel((i, j), 0)
#
#     return transform

