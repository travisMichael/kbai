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

def solve(problem):
    if 'Problem C-' not in problem.name:
        return -1

    imageMap = {}

    imageMap['A'] = Image.open(problem.figures['A'].visualFilename).convert("L")
    imageMap['B'] = Image.open(problem.figures['B'].visualFilename).convert("L")
    imageMap['C'] = Image.open(problem.figures['C'].visualFilename).convert("L")
    imageMap['D'] = Image.open(problem.figures['D'].visualFilename).convert("L")
    imageMap['E'] = Image.open(problem.figures['E'].visualFilename).convert("L")
    imageMap['F'] = Image.open(problem.figures['F'].visualFilename).convert("L")
    imageMap['G'] = Image.open(problem.figures['G'].visualFilename).convert("L")
    imageMap['H'] = Image.open(problem.figures['H'].visualFilename).convert("L")
    imageMap['1'] = Image.open(problem.figures['1'].visualFilename).convert("L")
    imageMap['2'] = Image.open(problem.figures['2'].visualFilename).convert("L")
    imageMap['3'] = Image.open(problem.figures['3'].visualFilename).convert("L")
    imageMap['4'] = Image.open(problem.figures['4'].visualFilename).convert("L")
    imageMap['5'] = Image.open(problem.figures['5'].visualFilename).convert("L")
    imageMap['6'] = Image.open(problem.figures['6'].visualFilename).convert("L")
    imageMap['7'] = Image.open(problem.figures['7'].visualFilename).convert("L")
    imageMap['8'] = Image.open(problem.figures['8'].visualFilename).convert("L")

    group_1 = ['A', 'B', 'C']
    group_2 = ['D', 'E', 'F']
    group_3 = ['G', 'H']

    no_op_answer = NoOp.solve_3x3(imageMap, group_1, group_2, group_3)
    if no_op_answer is not -1:
        print(problem.name, "3 best answer - ", str(no_op_answer))
        return no_op_answer

    return -1
