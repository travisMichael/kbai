from utility import calculate_image_similarity, apply_and_check, apply_and_check_3x3
import ImageTransformUtility


def solve(imageMap):
    A = imageMap.get('A')
    B = imageMap.get('B')
    C = imageMap.get('C')

    new_image = transform(A, B)
    new_image2 = transform(new_image, C)

    similarity, answer = apply_and_check(new_image2, imageMap)

    if similarity > 0.97:
        return answer

    return -1


# only keep similar pixels
def transform(image_1, image_2):
    height, width = image_1.size
    transform = image_1.copy()

    for i in range(height):
        for j in range(width):
            if image_1.getpixel((i,j)) != image_2.getpixel((i,j)) :
                transform.putpixel((i,j), 255)

    return transform


def solve_3x3(imageMap):

    A = imageMap.get('A')
    B = imageMap.get('B')
    C = imageMap.get('C')
    D = imageMap.get('D')
    F = imageMap.get('F')
    G = imageMap.get('G')
    H = imageMap.get('H')

    result_a_b = ImageTransformUtility.similar_dark_pixels_transform(A, B)
    result_b_c = ImageTransformUtility.similar_dark_pixels_transform(A, B)

    similarity = calculate_image_similarity(result_a_b, result_b_c)

    if similarity < 0.98:
        return -1

    result_a_d = ImageTransformUtility.similar_dark_pixels_transform(A, D)
    result_d_g = ImageTransformUtility.similar_dark_pixels_transform(D, G)

    similarity = calculate_image_similarity(result_a_d, result_d_g)

    if similarity < 0.98:
        return -1

    temp = ImageTransformUtility.subtract_dark_pixels(result_a_b, C)
    result_g_h = ImageTransformUtility.similar_dark_pixels_transform(G, H)

    transformation = ImageTransformUtility.combine_dark_pixel_transform(result_g_h, temp)

    similarity, answer = apply_and_check_3x3(transformation, imageMap)

    if similarity > 0.94:
        return answer

    return -1
