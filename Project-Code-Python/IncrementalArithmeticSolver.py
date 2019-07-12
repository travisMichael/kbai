from PIL import Image
from utility import calculate_image_similarity, apply_and_check, apply_and_check_3x3


CLOSENESS_THRESHOLD = 200


def is_close(value_1, value_2, epsilon):
    value_1 = abs(value_1)
    value_2 = abs(value_2)

    if epsilon is not None:
        if value_1 - epsilon < value_2 < value_1 + epsilon:
            return True
    else:
        if value_1 - CLOSENESS_THRESHOLD < value_2 < value_1 + CLOSENESS_THRESHOLD:
            return True

    return False


def is_same_sign(value_1, value_2):

    if value_1 < 0 and value_2 < 0:
        return True

    if value_1 > 0 and value_2 > 0:
        return True

    return False


# C-04 and C-12
def solve_3x3(imageMap, pixel_ratio_map):

    pixel_info_A = pixel_ratio_map.get('A')
    pixel_info_B = pixel_ratio_map.get('B')
    pixel_info_C = pixel_ratio_map.get('C')
    pixel_info_D = pixel_ratio_map.get('D')
    pixel_info_E = pixel_ratio_map.get('E')
    pixel_info_G = pixel_ratio_map.get('G')

    pixel_info_F = pixel_ratio_map.get('F')
    pixel_info_H = pixel_ratio_map.get('H')

    a_b_diff = pixel_info_A.get('black_pixels') - pixel_info_B.get('black_pixels')
    b_c_diff = pixel_info_B.get('black_pixels') - pixel_info_C.get('black_pixels')

    a_d_diff = pixel_info_A.get('black_pixels') - pixel_info_D.get('black_pixels')
    d_g_diff = pixel_info_D.get('black_pixels') - pixel_info_G.get('black_pixels')

    if not is_same_sign(a_d_diff, d_g_diff):
        return -1
    if not is_close(a_b_diff, a_d_diff, None):
        return -1
    if not is_close(a_b_diff, b_c_diff, None):
        return -1
    if not is_close(b_c_diff, d_g_diff, None):
        return -1
    if not is_same_sign(a_b_diff, b_c_diff):
        return -1

    vertical_diff = d_g_diff
    horizontal_diff = b_c_diff

    number_of_answers_filtered = 0
    potential_answers = []

    for i in range(1, 9):
        result = filter_answer_based_on_criteria(imageMap, pixel_ratio_map, str(i), vertical_diff, horizontal_diff)
        if result is not None and result:
            potential_answers.append(i)
        elif not None and not result:
            number_of_answers_filtered += 1

    if len(potential_answers) == 1:
        return potential_answers[0]

    potential_answers = []

    for i in range(1, 9):
        # if i == 4:
        #     print()
        result = filter_answer_based_on_criteria_2(imageMap, pixel_ratio_map, str(i), vertical_diff, horizontal_diff)
        if result is not None and result:
            potential_answers.append(i)
        elif not None and not result:
            number_of_answers_filtered += 1

    if len(potential_answers) == 1:
        return potential_answers[0]

    if len(potential_answers) == 2:
        image_1 = imageMap.get(str(potential_answers[0]))
        image_2 = imageMap.get(str(potential_answers[1]))
        similarity_1 = calculate_image_similarity(image_1, imageMap.get('A'))
        similarity_2 = calculate_image_similarity(image_2, imageMap.get('B'))
        if similarity_1 > similarity_2:
            return potential_answers[0]
        return potential_answers[1]
    return -1


def filter_answer_based_on_criteria_2(image_map, pixel_ratio_map, answer_label, vertical_diff, horizontal_diff):
    black_f = pixel_ratio_map.get('F').get('black_pixels')
    black_h = pixel_ratio_map.get('H').get('black_pixels')
    black_answer = pixel_ratio_map.get(answer_label).get('black_pixels')

    f_1_diff = black_f - black_answer
    h_1_diff = black_h - black_answer

    if (is_close(black_f, black_h, 200) or (is_close(black_answer, black_f - vertical_diff, 200) and is_close(black_answer, black_h - horizontal_diff, 200))) \
            and is_close(f_1_diff, h_1_diff, 200) \
            and is_same_sign(horizontal_diff, h_1_diff) \
            and is_same_sign(vertical_diff, f_1_diff):
        return True

    return None


def filter_answer_based_on_criteria(image_map, pixel_ratio_map, answer_label, vertical_diff, horizontal_diff):
    black_f = pixel_ratio_map.get('F').get('black_pixels')
    black_h = pixel_ratio_map.get('H').get('black_pixels')
    black_answer = pixel_ratio_map.get(answer_label).get('black_pixels')

    f_1_diff = black_f - black_answer
    h_1_diff = black_h - black_answer

    if is_same_sign(f_1_diff, vertical_diff) \
            and is_same_sign(h_1_diff, horizontal_diff) \
            and ((is_close(h_1_diff, horizontal_diff, None)
                  and is_close(f_1_diff, vertical_diff, None)) or is_close(horizontal_diff + vertical_diff, h_1_diff, None)):
        return True

    similarity = calculate_image_similarity(image_map.get(answer_label), image_map.get('F'))
    similarity_2 = calculate_image_similarity(image_map.get(answer_label), image_map.get('H'))

    if similarity > 0.97 and similarity_2 > 0.97:
        return True

    return False
