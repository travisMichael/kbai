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
from PIL import ImageOps
import numpy as np
from utility import calculate_current_image, apply_and_check
from State import State
import rules as rules

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

        stateQueue = []
        stateQueue.append(State(image='A'))

        # used so that the same state is not calculated twice
        stateMap = {}

        # calculate state
        mostSimilarSoFar = 0.0
        bestAnswerSoFar = '1'
        iterations = 0
        while True:
            iterations += 1
            # todo: Try to make this more efficient
            # pop state from queue, aka stack
            currentState = stateQueue.pop()
            currentImage = calculate_current_image(imageMap, currentState)
            # find sequence of operations that match B
            operationsToApply = rules.calculate(currentImage, targetImage=imageMap.get("B"))

            if len(operationsToApply) == 1 and operationsToApply[0].type == "NoOp":
                # apply that sequence to C and check if there is a match
                actualSimilarity, bestOption = apply_and_check(imageMap, currentState.operationSequence)
                if actualSimilarity > 0.99:
                    return bestOption
            else:
                for i in range(len(operationsToApply)):
                    newState = State(image=currentState.originalImage, sequence=[])

                    stateQueue.append(newState)


            # if not, repeat until time expires
            if iterations > 20:
                print("failed to solve the problem in less than 20 iterations")
                return -1

        return -1
