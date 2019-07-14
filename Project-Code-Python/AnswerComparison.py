from utility import calculate_image_similarity, apply_and_check_with_choices_3x3
import ImageTransformUtility


def solve_3x3(imageMap):

    A = imageMap.get('A')
    B = imageMap.get('B')
    C = imageMap.get('C')
    D = imageMap.get('D')
    E = imageMap.get('E')
    F = imageMap.get('F')
    G = imageMap.get('G')
    H = imageMap.get('H')

    image_list = [A, B, C, D, E, F, G, H]

    potential_answers = {
        '1': True,
        '2': True,
        '3': True,
        '4': True,
        '5': True,
        '6': True,
        '7': True,
        '8': True
    }

    for image in image_list:

        similarity, answer = apply_and_check_with_choices_3x3(image, imageMap, list(potential_answers.keys()))

        if similarity > 0.95:
            del potential_answers[str(answer)]

    if len(potential_answers) == 1:
        return int(list(potential_answers.keys())[0])

    return -1
