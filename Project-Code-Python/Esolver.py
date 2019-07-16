
from PIL import Image
import InclusiveOr
import SimpleSubtract
import DarkPixelConjunction
from utility import calculate_pixel_ratio, calculate_pixel_ratio_map


def solve(problem):
    if 'Problem E-' not in problem.name:
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

    dark_pixel_conjunction_answer = DarkPixelConjunction.solve_3x3(imageMap, [['A', 'B'], ['D', 'E']], ['C', 'F'], ['G', 'H'])
    if dark_pixel_conjunction_answer is not -1:
        print(problem.name, "1 best answer - ", str(dark_pixel_conjunction_answer))
        return dark_pixel_conjunction_answer

    # dark_pixel_conjunction_answer = DarkPixelConjunction.solve_3x3(imageMap, [['A', 'D'], ['B', 'E']], ['G', 'H'], ['C', 'F'])
    # if dark_pixel_conjunction_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(dark_pixel_conjunction_answer))
    #     return dark_pixel_conjunction_answer

    # inclusive_or_answer = InclusiveOr.solve_3x3_groupings(imageMap, [['A', 'B'], ['D', 'E']], ['C', 'F'], ['G', 'H'])
    # if inclusive_or_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(inclusive_or_answer))
    #     return inclusive_or_answer
    #
    # simple_subtract_answer = SimpleSubtract.solve_3x3_exclusive_or(imageMap, [['A', 'B'], ['D', 'E']], ['C', 'F'], ['G', 'H'])
    # if simple_subtract_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(simple_subtract_answer))
    #     return simple_subtract_answer
    # simple_subtract_answer = SimpleSubtract.solve_3x3_exclusive_or(imageMap, [['A', 'D'], ['B', 'E']], ['G', 'H'], ['C', 'F'])
    # if simple_subtract_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(simple_subtract_answer))
    #     return simple_subtract_answer
    #
    # simple_subtract_answer = SimpleSubtract.solve_3x3(imageMap, [['A', 'B'], ['D', 'E']], ['C', 'F'], ['G', 'H'])
    # if simple_subtract_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(simple_subtract_answer))
    #     return simple_subtract_answer
    #
    # simple_subtract_answer = SimpleSubtract.solve_3x3(imageMap, [['A', 'D'], ['B', 'E']], ['G', 'H'], ['C', 'F'])
    # if simple_subtract_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(simple_subtract_answer))
    #     return simple_subtract_answer

    # no_op_answer = NoOp.solve_3x3(imageMap, pixel_ratio_map, group_1, group_2, group_3)
    # if no_op_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(no_op_answer))
    #     return no_op_answer
    #
    # no_op_answer = NoOp.solve_3x3(imageMap, pixel_ratio_map, group_2_1, group_2_2, group_2_3)
    # if no_op_answer is not -1:
    #     print(problem.name, "1 best answer - ", str(no_op_answer))
    #     return no_op_answer

    # similar_pixel_answer = SimilarPixels.solve_3x3(imageMap)
    # if similar_pixel_answer is not -1:
    #     print(problem.name, "similar pixels best answer - ", str(similar_pixel_answer))
    #     return similar_pixel_answer

    # ----------------------------------------------------------------------

    return -1
