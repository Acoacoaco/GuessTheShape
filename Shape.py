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
        if points == 1:
            print("You earned 1 point!")
        else:
            print("You earned " + str(points) + " points!")

    # inform about wrong answer
    def wrongAnswerInfo(self):
        print("\nSorry, \"" + answer.lower() + "\" is wrong answer!")

    # inform about game over
    def gameOver(self):
        print("Game over! The right answer was: \"" + question.name + "\".\n")

    # ask user to play again
    def playAgain(self):
        more_play = input("Do you want to play again? [y/n]: ")
        if more_play == "y":
            self.gameRestart()
        elif more_play == "n":
            exit()
        else:
            print("Wrong command!")

    # restart the game
    def gameRestart(self):
        import sys
        print("The game will restart now.")
        import os
        os.execl(sys.executable, sys.executable, *sys.argv)

# game
game = Game()

# shapes
cat = Shape("cat", 
    "|\---/|", 
    "| o_o |", 
    " \_V_/ ")
cat.addToShapeList()

house = Shape("house",
    "  /\   ", 
    " /\-\  ", 
    "_||\"|_")
house.addToShapeList()

car = Shape("car",
    "     ,-----,      ", 
    "  ,--'---:---`--, ", 
    " ==(o)-----(o)==J ")
car.addToShapeList()

dog = Shape("dog",
    "       _=,_           ",
    "    o_/6 /#\          ",
    "   \__ |##/           ",
    "    =\'|--\           ",
    "      /    #'-.       ",
    "      \\#|_   _\'-. / ",
    "       |/ \_( # |\"   ",
    "      C/ ,--___/      ")
dog.addToShapeList()

camel = Shape("camel",
    "              ,,__ ",
    "    ..  ..   / o._)", 
    "   /--'/--\  \-'|| ",
    "  /        \_/ / | ",
    ".'\  \__\  __.'.'  ",
    "  )\ |  )\ |       ",
    " // \\\ // \\\       ",
    "||_  \\\|_  \\\_     ")
camel.addToShapeList()

bicycle = Shape("bicycle",     
    "              d$$$$$$$P\"                  $    J              ",
    "                  ^$.                     4r  \"               ",
    "                  d\"b                    .db                  ",
    "                 P   $                  e\" $                  ",
    "        ..ec.. .\"     *.              zP   $.zec..            ",
    "     .^        3*b.     *.           .P\" .@\"4F      \"4      ",
    "   .\"         d\"  ^b.    *c        .$\"  d\"   $         %   ",
    "  /          P      $.    \"c      d\"   @     3r         3    ",
    " 4        .eE........$r===e$$$$eeP    J       *..        b     ",
    " $       $$$$$       $   4$$$$$$$     F       d$$$.      4     ",
    " $       $$$$$       $   4$$$$$$$     L       *$$$\"      4    ",
    " 4         \"      \"\"3P ===$$$$$$\"     3                  P ",
    "  *                 $       \"\"\"        b                J   ",
    "   \".             .P                    %.             @      ",
    "     %.         z*\"                      ^%.        .r\"      ",
    "       \"*==*\"\"                             ^\"*==*\"\"      ")
bicycle.addToShapeList()

# random choice of the shape to guess
question = game.chooseShape()

# points to earn
points = len(question.lines)-1

# start of the game
print(game.double_line)
print(game.instructions)
print(game.double_line)

# check if there is more to show
while game.counter < len(question.lines):
    game.giveHint()
    print("\nPoints to earn: "+ str(points))
    
    # user input
    answer = input("Type in your guess: ")
    print(game.double_line)

    # check the input
    game.checkAnswer()
    points -= 1

# if no more to show - end the game
question.printFullShape()
game.gameOver()
game.playAgain()
