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
# from PIL import Image
# import Bsolver
# import Csolver
import Dsolver
import Esolver
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

        # answer = Bsolver.solve(problem)
        # if answer != -1:
        #     return answer
        # if 'Basic Problem C-' not in problem.name:
        #     return -1

        if 'Problem D-' not in problem.name:
            return -1
        # answer = Csolver.solve(problem)
        # if answer != -1:
        #     return answer

        answer = Dsolver.solve(problem)
        if answer != -1:
            return answer

        answer = Esolver.solve(problem)
        if answer != -1:
            return answer



        print("did not find a solution")
        return -1
