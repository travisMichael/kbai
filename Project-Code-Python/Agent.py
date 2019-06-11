# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# invertedImage = ImageOps.invert(convertedImage)

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
from PIL import Image
# from PIL import ImageOps
import numpy as np
import Reflection
import NoOp
import ShapeFiller
import SubtractAndAdd
import Rotation
import SimpleSubtract
import SimilarPixels


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):

        # if 'Basic Problem B-' not in problem.name:
        #     return -1

        imageMap = {}

        imageMap['A'] = Image.open(problem.figures['A'].visualFilename).convert("L")
        imageMap['B'] = Image.open(problem.figures['B'].visualFilename).convert("L")
        imageMap['C'] = Image.open(problem.figures['C'].visualFilename).convert("L")
        imageMap['1'] = Image.open(problem.figures['1'].visualFilename).convert("L")
        imageMap['2'] = Image.open(problem.figures['2'].visualFilename).convert("L")
        imageMap['3'] = Image.open(problem.figures['3'].visualFilename).convert("L")
        imageMap['4'] = Image.open(problem.figures['4'].visualFilename).convert("L")
        imageMap['5'] = Image.open(problem.figures['5'].visualFilename).convert("L")
        imageMap['6'] = Image.open(problem.figures['6'].visualFilename).convert("L")


        simple_subtract_answer = SimpleSubtract.solve(imageMap, 'B', 'C')
        if simple_subtract_answer is not -1:
            print(problem.name, "3 best answer - ", str(simple_subtract_answer))
            return simple_subtract_answer

        simple_subtract_answer = SimpleSubtract.solve(imageMap, 'C', 'B')
        if simple_subtract_answer is not -1:
            print(problem.name, "4 best answer - ", str(simple_subtract_answer))
            return simple_subtract_answer

        similar_pixels_answer = SimilarPixels.solve(imageMap)
        if similar_pixels_answer is not -1:
            print(problem.name, "5 best answer - ", str(similar_pixels_answer))
            return similar_pixels_answer

        reflection_horizontal_answer = Reflection.solve_horizontal(imageMap, 'B', 'C')
        if reflection_horizontal_answer is not -1:
            print(problem.name, "6 best answer - ", str(reflection_horizontal_answer))
            return reflection_horizontal_answer

        reflection_horizontal_answer = Reflection.solve_horizontal(imageMap, 'C', 'B')
        if reflection_horizontal_answer is not -1:
            print(problem.name, "7 best answer - ", str(reflection_horizontal_answer))
            return reflection_horizontal_answer

        no_op_answer = NoOp.solve(imageMap, 'B', 'C')
        if no_op_answer is not -1:
            print(problem.name, "1 best answer - ", str(no_op_answer))
            return no_op_answer

        no_op_answer = NoOp.solve(imageMap, 'C', 'B')
        if no_op_answer is not -1:
            print(problem.name, "2 best answer - ", str(no_op_answer))
            return no_op_answer

        reflection_vertical_answer = Reflection.solve_vertical(imageMap, 'B', 'C')
        if reflection_vertical_answer is not -1:
            print(problem.name, "8 best answer - ", str(reflection_vertical_answer))
            return reflection_horizontal_answer

        reflection_vertical_answer = Reflection.solve_vertical(imageMap, 'C', 'B')
        if reflection_vertical_answer is not -1:
            print(problem.name, "9 best answer - ", str(reflection_vertical_answer))
            return reflection_vertical_answer

        rotation_90_answer = Rotation.solve_rotate_90(imageMap, 'B', 'C')
        if rotation_90_answer is not -1:
            print(problem.name, "10 rotate_90 best answer - ", str(rotation_90_answer))
            return rotation_90_answer

        rotation_90_answer = Rotation.solve_rotate_90(imageMap, 'C', 'B')
        if rotation_90_answer is not -1:
            print(problem.name,"11 rotate_90 best answer - ", str(rotation_90_answer))
            return rotation_90_answer

        rotation_270_answer = Rotation.solve_rotate_270(imageMap, 'B', 'C')
        if rotation_270_answer is not -1:
            print(problem.name, "12 rotate_270 best answer - ", str(rotation_270_answer))
            return rotation_270_answer

        rotation_270_answer = Rotation.solve_rotate_270(imageMap, 'C', 'B')
        if rotation_270_answer is not -1:
            print(problem.name,"13 rotate_270 best answer - ", str(rotation_270_answer))
            return rotation_270_answer

        shape_filler_answer = ShapeFiller.solve(imageMap, 'B', 'C')
        if shape_filler_answer is not -1:
            print(problem.name, "14 best answer - ", str(shape_filler_answer))
            return shape_filler_answer

        substract_and_add_answer = SubtractAndAdd.solve(imageMap, 'B', 'C')
        if substract_and_add_answer is not -1:
            print(problem.name, "15 best answer - ", str(substract_and_add_answer))
            return substract_and_add_answer

        substract_and_add_answer = SubtractAndAdd.solve(imageMap, 'C', 'B')
        if substract_and_add_answer is not -1:
            print(problem.name, "16 best answer - ", str(substract_and_add_answer))
            return substract_and_add_answer



        print("did not find a solution")
        return -1
