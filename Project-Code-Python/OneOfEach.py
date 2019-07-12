
THRESHOLD = 0.92


# C-02
def solve_3x3(imageMap, pixel_ratio_map, group_1, group_2, group_3):

    dark_pixels_1_1 = pixel_ratio_map.get(group_1[0]).get('black_pixels')
    dark_pixels_1_2 = pixel_ratio_map.get(group_1[1]).get('black_pixels')
    dark_pixels_1_3 = pixel_ratio_map.get(group_1[2]).get('black_pixels')
    dark_pixels_2_1 = pixel_ratio_map.get(group_2[0]).get('black_pixels')
    dark_pixels_2_2 = pixel_ratio_map.get(group_2[1]).get('black_pixels')
    dark_pixels_2_3 = pixel_ratio_map.get(group_2[2]).get('black_pixels')
    dark_pixels_3_1 = pixel_ratio_map.get(group_3[0]).get('black_pixels')
    dark_pixels_3_2 = pixel_ratio_map.get(group_3[1]).get('black_pixels')

    if dark_pixels_1_1 == dark_pixels_1_2 or dark_pixels_1_2 == dark_pixels_1_3 or dark_pixels_1_1 == dark_pixels_1_3:
        return -1

    if dark_pixels_2_1 == dark_pixels_2_2 or dark_pixels_2_2 == dark_pixels_2_3 or dark_pixels_2_1 == dark_pixels_2_3:
        return -1

    if dark_pixels_3_1 == dark_pixels_3_2:
        return -1

    contains_map = {
        str(dark_pixels_1_1): True,
        str(dark_pixels_1_2): True,
        str(dark_pixels_1_3): True
    }

    result_1 = contains_map.get(str(dark_pixels_2_1))
    result_2 = contains_map.get(str(dark_pixels_2_2))
    result_3 = contains_map.get(str(dark_pixels_2_3))
    result_4 = contains_map.get(str(dark_pixels_3_1))
    result_5 = contains_map.get(str(dark_pixels_3_2))

    if result_1 is None or result_2 is None or result_3 is None or result_4 is None or result_5 is None:
        return -1

    del contains_map[str(dark_pixels_3_1)]
    del contains_map[str(dark_pixels_3_2)]

    dark_pixels_to_match = list(contains_map.keys())[0]

    potential_answers = []

    for i in range(1, 9):
        potential_answer = pixel_ratio_map.get(str(i)).get('black_pixels')

        if dark_pixels_to_match == potential_answer:
            potential_answers.append(i)

    if len(potential_answers) == 1:
        return potential_answers[0]
    else:
        print('Found more than one potential answer')

    return -1
