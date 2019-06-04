
def horizontal_reflection(image):
    return image


def vertical_reflection(image):
    return image


class NoOp:

    def __init__(self):
        self.type = "NoOp"
        self.apply = None


class HorizontalReflection:

    def __init__(self):
        self.type = "Reflection"
        self.apply = horizontal_reflection


class VerticalReflection:

    def __init__(self):
        self.type = "Reflection"
        self.apply = vertical_reflection
