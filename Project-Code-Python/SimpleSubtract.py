from PIL import Image, ImageChops, ImageOps
from utility import calculate_image_similarity, apply_and_check

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
