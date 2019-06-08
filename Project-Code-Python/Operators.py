from PIL import Image

# FLIP_TOP_BOTTOM, ROTATE_90, ROTATE_180, or ROTATE_270
NO_OP = 0
HORIZONTAL_REFLECTION = 1
VERTICAL_REFLECTION = 2



def image_transform(image, operators):
    for operation in operators:
        if operation == HORIZONTAL_REFLECTION:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif operation == VERTICAL_REFLECTION:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)

    return image
