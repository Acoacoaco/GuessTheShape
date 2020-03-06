# modules
import random

# class of shapes
class Shape:
    def __init__(self, name, *lines):
        self.name = name
        self.lines = lines

    def printFullShape(self):
        print("")
        for line in self.lines:
            print(line)
        print("")
    
    def addToShapeList(self):
        game.shape_list.append(self)

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

    # random choose of the shape
    def chooseShape(self):
        return random.choice(game.shape_list)

    # give hint
    def giveHint(self):
        print("\nHere's the hint.\n")
    
        # show more of the shape
        lines_to_print = range(game.counter)
        for line_to_print in lines_to_print:
            print(question.lines[line_to_print])

    # check the answer
    def checkAnswer(self):
        if answer.lower() == question.name:
            game.rightAnswerInfo()
            game.playAgain()
        else:
            game.wrongAnswerInfo()
            game.counter += 1

    # inform about right answer 
    def rightAnswerInfo(self):
        question.printFullShape()
        print("Congratulations! \"" + question.name.capitalize() + "\" was the right answer.\n")

    # inform about wrong answer
    def wrongAnswerInfo(self):
        print("\nSorry, \"" + answer.lower() + "\" is wrong answer!")

    # informa about game over
    def gameOver(self):
        print("Game over! The right answer was: \"" + question.name + "\".\n")

    # ask user to play again
    def playAgain(self):
        restart = input("Do you want to play again? [y/n]: ")
        if restart == "y":
            self.gameRestart()
        elif restart == "n":
            exit()
        else:
            print("Wrong command!")

    # restart the game
    def gameRestart(self):
        import sys
        print("The game will restart now.")
        import os
        os.execv(sys.executable, ['python'] + sys.argv)

# game
game = Game()

# shapes
cat = Shape("cat", 
    "|\\---/|", 
    "| o_o | ", 
    " \\_V_/ ")
cat.addToShapeList()

house = Shape("house",
    "  /\\   ", 
    " /\\-\\ ", 
    "_||\"|_ ")
house.addToShapeList()

car = Shape("car",
    "     ,-----,      ", 
    "  ,--'---:---`--, ", 
    " ==(o)-----(o)==J ")
car.addToShapeList()

dog = Shape("dog",
    " (___()'`;   ",
    " /,    /`    ",
    " \\\"--\\\", ")
dog.addToShapeList()

camel = Shape("camel",
    "              ,,__ ",
    "    ..  ..   / o._)", 
    "   /--'/--\  \-'|| ",
    "  /        \_/ / | ",
    ".'\  \__\  __.'.'  ",
    "  )\ |  )\ |       ",
    " // \\\\ // \\\\   ",
    "||_  \\\\|_  \\\\_ ")
camel.addToShapeList()

# random choice of the shape to guess
question = game.chooseShape()

# start of the game
print(game.double_line)
print(game.instructions)
print(game.double_line)

# check if there is more to show
while game.counter < len(question.lines):
    game.giveHint()

    # user input
    answer = input("\nType in your guess: ")
    print(game.double_line)

    # check the input
    game.checkAnswer()

# if no more to show - end the game
question.printFullShape()
game.gameOver()
game.playAgain()
