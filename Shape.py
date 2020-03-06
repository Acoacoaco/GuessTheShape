# modules
import random

# class of shapes
class Shape:
    def __init__(self, name, *lines):
        self.name = name
        self.lines = lines

    def printFullAnswer(self):
        print("")
        for line in self.lines:
            print(line)
        print("")
    
    def addToShapeList(self):
        shape_list.append(self)

# class of game
class Game:
    def __init__(self):
        # strings
        self.double_line = "\n======================================================="
        self.instructions = "\n\tWelcome to the \"GUESS THE SHAPE\" game!\nTry to guess the shape (in ASCII art), presented below."

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

# list of shapes
shape_list = []

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
question = random.choice(shape_list)

# start of the game
print(game.double_line)
print(game.instructions)
print(game.double_line)

# counter
i = 1

# check if there is more to show
while i < len(question.lines):
    print("\nHere's the hint.\n")
    
    # show more of the shape
    lines_to_print = range(i)
    for line_to_print in lines_to_print:
        print(question.lines[line_to_print])

    # user input
    answer = input("\nType in your guess: ")
    print(game.double_line)

    # check the answer
    if answer.lower() == question.name:
        question.printFullAnswer()
        print("Congratulations! \"" + question.name.capitalize() + "\" was the right answer.\n")
        game.playAgain()
    else:
        print("\nSorry, \"" + answer.lower() + "\" is wrong answer!")
        i += 1

# if no more to show - end the game
question.printFullAnswer()
print("Game over! The right answer was: \"" + question.name + "\".\n")
game.playAgain()

