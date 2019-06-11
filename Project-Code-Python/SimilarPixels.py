from utility import calculate_image_similarity, apply_and_check


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
