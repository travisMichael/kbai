from PIL import Image, ImageChops, ImageOps
from utility import calculate_image_similarity, apply_and_check

# ImageOps.invert(convertedImage)
# todo Make this more generic by also accounting for subtracting first
def solve(imageMap, compared_to_A, image_to_compare_answers_with):
    A = imageMap.get('A')
    B = imageMap.get('B')
    C = imageMap.get('C')

    difference = ImageChops.subtract(A, B)
    difference2 = ImageChops.subtract(B, A)
    # difference.save('aB.png')
    # difference2.save('bA.png')
    temp_image = ImageOps.invert(difference)

    # add the white pixels from ab should be made into black
    transform_image_A = transform(A, difference, True)
    new_image_A = transform(transform_image_A, difference2, False)
    # new_image_A.save('A_new.png')

    similarity = calculate_image_similarity(new_image_A, B)

    if similarity > 0.95:

        transform_image = transform(C, difference, True)
        new_image = transform(transform_image, difference2, False)

        similarity, answer = apply_and_check(new_image, imageMap)

        if similarity > 0.91:
            return answer

    return -1


def transform(image_to_transform, image_2, ab_add):
    height, width = image_to_transform.size
    transform = image_to_transform.copy()

    for i in range(height):
        for j in range(width):
            if image_2.getpixel((i,j)) == 255:
                if ab_add:
                    transform.putpixel((i, j), 0)
                else:
                    transform.putpixel((i, j), 255)

    return transform

