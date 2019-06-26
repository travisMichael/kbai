from PIL import Image
from utility import calculate_image_similarity, apply_and_check_3x3

THRESHOLD = 0.97


def solve_3x3(imageMap):

    image_A = imageMap.get('A')
    image_B = imageMap.get('B')
    image_C = imageMap.get('C')
    image_D = imageMap.get('D')
    image_F = imageMap.get('F')
    image_G = imageMap.get('G')
    image_H = imageMap.get('H')

    # row 1
    result = is_proper_subset(image_B, image_C)
    if not result:
        return -1
    result = is_proper_subset(image_A, image_B)
    if not result:
        return -1
    result = is_proper_subset(image_C, image_F)
    if not result:
        return -1
    # row 2
    result = is_proper_subset(image_D, image_G)
    if not result:
        return -1
    result = is_proper_subset(image_A, image_D)
    if not result:
        return -1

    return 4


def is_proper_subset(image_1, image_2):
    height, width = image_1.size

    number_of_pixels = 0

    new = Image.new("L", (height, width), color=255)

    for i in range(height):
        for j in range(width):
            if image_1.getpixel((i, j)) == 0 and image_2.getpixel((i,j)) == 255:
                number_of_pixels += 1
                new.putpixel((i, j), 0)

    # new.save("new.png")
    if number_of_pixels > 2:
        return False

    return True

