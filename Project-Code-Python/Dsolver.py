
from PIL import Image
import NoOp
import MatchDiagonals
import SimilarPixels
import AnswerComparison
from utility import calculate_pixel_ratio, calculate_pixel_ratio_map


def solve(problem):
    if 'Problem D-' not in problem.name:
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

    no_op_answer = NoOp.solve_3x3(imageMap, pixel_ratio_map, group_1, group_2, group_3)
    if no_op_answer is not -1:
        print(problem.name, "1 best answer - ", str(no_op_answer))
        return no_op_answer

    no_op_answer = NoOp.solve_3x3(imageMap, pixel_ratio_map, group_2_1, group_2_2, group_2_3)
    if no_op_answer is not -1:
        print(problem.name, "1 best answer - ", str(no_op_answer))
        return no_op_answer

    match_diagonals_answer = MatchDiagonals.solve_3x3(imageMap)
    if match_diagonals_answer is not -1:
        print(problem.name, "1 best answer - ", str(match_diagonals_answer))
        return match_diagonals_answer

    answer_comparison_answer = AnswerComparison.solve_3x3(imageMap)
    if answer_comparison_answer is not -1:
        print(problem.name, "answer comparison best answer - ", str(answer_comparison_answer))
        return answer_comparison_answer

    similar_pixel_answer = SimilarPixels.solve_3x3(imageMap)
    if similar_pixel_answer is not -1:
        print(problem.name, "similar pixels best answer - ", str(similar_pixel_answer))
        return similar_pixel_answer

    # ----------------------------------------------------------------------

    return -1
