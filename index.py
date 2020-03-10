# modules
from Shape import Shape
from Game import Game

# game
game = Game()

# shapes
cat = Shape("cat", 
    "|\---/|", 
    "| o_o |", 
    " \_V_/ ")
game.addToShapeList(cat)

house = Shape("house",
    "  /\   ", 
    " /\-\  ", 
    "_||\"|_")
game.addToShapeList(house)

car = Shape("car",
    "     ,-----,      ", 
    "  ,--'---:---`--, ", 
    " ==(o)-----(o)==J ")
game.addToShapeList(car)

dog = Shape("dog",
    "       _=,_           ",
    "    o_/6 /#\          ",
    "   \__ |##/           ",
    "    =\'|--\           ",
    "      /    #'-.       ",
    "      \\#|_   _\'-. / ",
    "       |/ \_( # |\"   ",
    "      C/ ,--___/      ")
game.addToShapeList(dog)

camel = Shape("camel",
    "              ,,__ ",
    "    ..  ..   / o._)", 
    "   /--'/--\  \-'|| ",
    "  /        \_/ / | ",
    ".'\  \__\  __.'.'  ",
    "  )\ |  )\ |       ",
    " // \\\ // \\\       ",
    "||_  \\\|_  \\\_     ")
game.addToShapeList(camel)

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
game.addToShapeList(bicycle)

game.question = game.chooseShape()
game.points = game.getPoints()

# start of the game
print(game.double_line)
print(game.instructions)
print(game.double_line)

# check if there is more to show
while game.counter < len(game.question.lines):
    game.giveHint()
    print("\nPoints to earn: "+ str(game.points))
    
    # user input
    game.answer = input("Type in your guess: ")
    print(game.double_line)

    # check the input
    game.checkAnswer()
    game.points -= 1

# if no more to show - end the game
game.question.printFullShape()
# inform about game over
print("Game over! The right answer was: \"" + game.question.name + "\".\n")
game.playAgain()
