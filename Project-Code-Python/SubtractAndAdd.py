from PIL import Image, ImageChops, ImageOps
from utility import calculate_image_similarity, apply_and_check


def solve(imageMap, compared_to_A, image_to_compare_answers_with):
    A = imageMap.get('A')
    B = imageMap.get(compared_to_A)
    C = imageMap.get(image_to_compare_answers_with)

    difference = ImageChops.subtract(A, B)
    difference2 = ImageChops.subtract(B, A)

    # add the white pixels from ab should be made into black
    transform_image_A = transform(A, difference)
    new_image_A = transform(transform_image_A, difference2)
    # transform_image_A.save('aB.png')
    # new_image_A.save('bA.png')
    # new_image_A.save('A_new.png')

    similarity = calculate_image_similarity(new_image_A, B)

    if similarity > 0.95:

        transform_image = transform(C, difference)
        new_image = transform(transform_image, difference2)

        similarity, answer = apply_and_check(new_image, imageMap)

        if similarity > 0.91:
            return answer

    return -1


def transform(image_to_transform, difference):
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
