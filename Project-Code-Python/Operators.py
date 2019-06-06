from PIL import Image

# FLIP_TOP_BOTTOM, ROTATE_90, ROTATE_180, or ROTATE_270

class Operation:

    def __init__(self):
        self.noOp = 0
        self.horizontalReflection = 1
        self.verticalReflection = 2

    def apply(self, image, operators):
        for operation in operators:
            if operation == self.horizontalReflection:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif operation == self.verticalReflection:
                image = image.transpose(Image.FLIP_TOP_BOTTOM)

        return image
