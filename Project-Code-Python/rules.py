import Operators as op
from utility import calculate_image_similarity

NO_OP = op.NoOp()
HORIZONTAL_REFLECTION = op.HorizontalReflection()
VERTICAL_REFLECTION = op.HorizontalReflection()

# given an image and a target image, return the operations most likely to lead to a match
def calculate(image, targetImage):
    # distanceFromTarget = heuristic(image, targetImage)
    similarity = calculate_image_similarity(image, targetImage)

    if similarity > 0.99:
        return [NO_OP]

    return [HORIZONTAL_REFLECTION, VERTICAL_REFLECTION]

