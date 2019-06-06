import Operators as op
from utility import calculate_image_similarity

OPERATION = op.Operation()

# given an image and a target image, return the operations most likely to lead to a match
def calculate(image, targetImage, operationSequence):
    # distanceFromTarget = heuristic(image, targetImage)
    similarity = calculate_image_similarity(image, targetImage)

    if similarity > 0.99:
        return [OPERATION.noOp]

    validOperations = [OPERATION.horizontalReflection, OPERATION.verticalReflection]

    last_operation = -1
    for operation in operationSequence:
        if operation == OPERATION.horizontalReflection and last_operation == OPERATION.horizontalReflection:
            validOperations = list(filter(lambda x: x == OPERATION.horizontalReflection, validOperations))
        if operation == OPERATION.verticalReflection and last_operation == OPERATION.verticalReflection:
            validOperations = list(filter(lambda x: x == OPERATION.verticalReflection, validOperations))
        last_operation = operation

    return validOperations

