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

    # check answers ----------------------------
    image_1 = imageMap.get('1')
    result = is_proper_subset(image_H, image_1)
    if result:
        return 1

    image_2 = imageMap.get('2')
    result = is_proper_subset(image_H, image_2)
    if result:
        return 2

    image_3 = imageMap.get('3')
    result = is_proper_subset(image_H, image_3)
    if result:
        return 3

    image_4 = imageMap.get('4')
    result = is_proper_subset(image_H, image_4)
    if result:
        return 4

    image_5 = imageMap.get('5')
    result = is_proper_subset(image_H, image_5)
    if result:
        return 5

    image_6 = imageMap.get('6')
    result = is_proper_subset(image_H, image_6)
    if result:
        return 6

    image_7 = imageMap.get('7')
    result = is_proper_subset(image_H, image_7)
    if result:
        return 7

    image_8 = imageMap.get('8')
    result = is_proper_subset(image_H, image_8)
    if result:
        return 8

    return -1


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

