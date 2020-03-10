#modules
import random

# class of game
class Game:
    def __init__(self):
        # counter
        self.counter = 1

        # list of shapes
        self.shape_list = []

        # strings
        self.double_line = "\n======================================================="
        self.instructions = "\n\tWelcome to the \"GUESS THE SHAPE\" game!\nTry to guess the shape (in ASCII art), presented below."

        # question
        self.question = ""

        # points to earn
        self.points = 0

        # answer
        self.answer = ""

    # add to list
    def addToShapeList(self, shape):
        self.shape_list.append(shape)

    # random choose of the shape
    def chooseShape(self):
        return random.choice(self.shape_list)

    # Get points to earn
    def getPoints(self):
        return len(self.question.lines)-1

    # give hint
    def giveHint(self):
        print("\nHere's the hint.\n")
    
        # show more of the shape
        lines_to_print = range(self.counter)
        for line_to_print in lines_to_print:
            print(self.question.lines[line_to_print])

    # check the answer
    def checkAnswer(self):
        if self.answer.lower() == self.question.name:
            # inform about right answer 
            self.question.printFullShape()
            print("Congratulations! \"" + self.question.name.capitalize() + "\" was the right answer.\n")
            if self.points == 1:
                print("You earned 1 point!")
            else:
                print("You earned " + str(self.points) + " points!")
            self.playAgain()
        else:
            # inform about wrong answer
            print("\nSorry, \"" + self.answer.lower() + "\" is wrong answer!")
            self.counter += 1

    # ask user to play again
    def playAgain(self):
        more_play = input("Do you want to play again? [y/n]: ")
        if more_play == "y":
            self.gameRestart()
        elif more_play == "n":
            exit()
        else:
            print("Wrong command!")
            self.playAgain()

    # restart the game
    def gameRestart(self):
        import sys
        print("The game will restart now.")
        import os
        os.execl(sys.executable, sys.executable, *sys.argv)
