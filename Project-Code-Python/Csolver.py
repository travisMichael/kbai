from PIL import Image
import NoOp
import InclusiveOr
import ProgressiveAddition
import HorizontalTranslation
import RadialReflectionSolver
import Contains
import DoubleImageSolver
import IncrementalArithmeticSolver
from utility import calculate_pixel_ratio, calculate_pixel_ratio_map


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

    pixel_ratio_map = calculate_pixel_ratio_map(imageMap)

    group_1 = ['A', 'B', 'C']
    group_2 = ['D', 'E', 'F']
    group_3 = ['G', 'H']

    group_2_1 = ['A', 'D', 'G']
    group_2_2 = ['B', 'E', 'H']
    group_2_3 = ['C', 'F']

    double_image_answer = DoubleImageSolver.solve_3x3(imageMap)
    if double_image_answer is not -1:
        print(problem.name, "7 best answer - ", str(double_image_answer))
        return double_image_answer

    contains_answer = Contains.solve_3x3(imageMap)
    if contains_answer is not -1:
        print(problem.name, "6 best answer - ", str(contains_answer))
        return contains_answer

    radial_reflection_answer = RadialReflectionSolver.solve_3x3(imageMap)
    if radial_reflection_answer is not -1:
        print(problem.name, "5 best answer - ", str(radial_reflection_answer))
        return radial_reflection_answer

    no_op_answer = NoOp.solve_3x3(imageMap, pixel_ratio_map, group_1, group_2, group_3)
    if no_op_answer is not -1:
        print(problem.name, "1 best answer - ", str(no_op_answer))
        return no_op_answer

    no_op_answer = NoOp.solve_3x3(imageMap, pixel_ratio_map, group_2_1, group_2_2, group_2_3)
    if no_op_answer is not -1:
        print(problem.name, "1 best answer - ", str(no_op_answer))
        return no_op_answer

    progressive_addition_answer = ProgressiveAddition.solve_3x3(imageMap)
    if progressive_addition_answer is not -1:
        print(problem.name, "3 best answer - ", str(progressive_addition_answer))
        return progressive_addition_answer

    horizontal_translate_answer = HorizontalTranslation.solve_3x3(imageMap)
    if horizontal_translate_answer is not -1:
        print(problem.name, "4 best answer - ", str(horizontal_translate_answer))
        return horizontal_translate_answer

    # inclusive_or_answer = InclusiveOr.solve_3x3(imageMap)
    # if inclusive_or_answer is not -1:
    #     print(problem.name, "2 best answer - ", str(inclusive_or_answer))
    #     return inclusive_or_answer

    incremental_arithmetic_answer = IncrementalArithmeticSolver.solve_3x3(imageMap, pixel_ratio_map)
    if incremental_arithmetic_answer is not -1:
        print(problem.name, "8 best answer - ", str(incremental_arithmetic_answer))
        return incremental_arithmetic_answer

    return -1


