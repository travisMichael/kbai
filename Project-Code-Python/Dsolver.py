
from PIL import Image
import ExclusiveOr
import AnswerComparison
import DarkPixelConjunction
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

    if "Basic" in problem.name:
        answer_comparison_answer = AnswerComparison.solve_3x3(imageMap)
        if answer_comparison_answer is not -1:
            print(problem.name, "answer comparison best answer - ", str(answer_comparison_answer))
            return answer_comparison_answer
        dp_answer = DarkPixelConjunction.solve_3x3_dark_pixel_counter(pixel_ratio_map)
        if dp_answer is not -1:
            print(problem.name, "dp best answer - ", str(dp_answer))
            return dp_answer

    exclusive_or_answer = ExclusiveOr.solve_3x3(imageMap, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H']])
    if exclusive_or_answer is not -1:
        print(problem.name, "1 xor best answer - ", str(exclusive_or_answer))
        return exclusive_or_answer

    exclusive_or_answer = ExclusiveOr.solve_3x3(imageMap, [['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F']])
    if exclusive_or_answer is not -1:
        print(problem.name, "2 xor best answer - ", str(exclusive_or_answer))
        return exclusive_or_answer

    exclusive_or_answer = ExclusiveOr.solve_3x3_match_only(imageMap, [['H', 'F', 'A'], ['G', 'E', 'C'], ['D', 'B']])
    if exclusive_or_answer is not -1:
        print(problem.name, "3 best answer - ", str(exclusive_or_answer))
        return exclusive_or_answer

    return -1
