import numpy as np

# returns a value from 0-1. 0 = no similarity, 1 = exactly similar
def calculate_image_similarity(image_1, image_2):
    image_1 = np.array(image_1)
    image_2 = np.array(image_2)
    number_of_pixels_different = 0
    for i in range(184):
        for j in range(184):
            if image_1[i][j] != image_2[i][j]:
                number_of_pixels_different += 1

    x, y = image_1.shape
    total = x * y
    return (total - number_of_pixels_different) / total


def copy_sequence(list):
    return list


def calculate_current_image(imageMap, state):
    print("calculating state")
    return imageMap.get(state.originalImage)


# return the similarity between C and D after C has been calculated by the operators
def apply_and_check(imageMap, operationSequence):
    C = imageMap.get('C')
    convertedImage = C
    for operation in operationSequence:
        convertedImage = operation.operator(convertedImage)

    similarity = 0.0
    bestImageChoice = -1
    for i in range(6):
        temp_similarity = calculate_image_similarity(convertedImage, imageMap.get(str(i+1)))
        if temp_similarity > similarity:
            similarity = temp_similarity
            bestImageChoice = i+1

    return similarity, bestImageChoice
