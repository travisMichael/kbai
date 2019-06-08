import Operators as op
from utility import calculate_image_similarity


# given an image and a target image, return the operations most likely to lead to a match
def calculate_operations_to_perform(image, imageMap, operationSequence):
    # distanceFromTarget = heuristic(image, targetImage)
    similarity = calculate_image_similarity(image, imageMap.get('B'))

    if similarity > 0.99:
        return [op.NO_OP], similarity


    validOperations = [op.HORIZONTAL_REFLECTION, op.VERTICAL_REFLECTION]

    last_operation = -1
    for operation in operationSequence:
        if operation == op.HORIZONTAL_REFLECTION and last_operation == op.HORIZONTAL_REFLECTION:
            validOperations = list(filter(lambda x: x == op.HORIZONTAL_REFLECTION, validOperations))
        if operation == op.VERTICAL_REFLECTION and last_operation == op.VERTICAL_REFLECTION:
            validOperations = list(filter(lambda x: x == op.VERTICAL_REFLECTION, validOperations))
        last_operation = operation

    return validOperations, similarity

