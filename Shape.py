import random

class Shape:
    def __init__(self, name, *lines):
        self.name = name
        self.lines = lines

    def printFullAnswer(self):
        for line in self.lines:
            print(line)
        print("")
    
    def addToShapeList(self):
        shape_list.append(self)

shape_list = []

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
    "||_  \\\\|_  \\\\_ ",
    "'--' '--'' '--'    ")
camel.addToShapeList()

question = random.choice(shape_list)

print("")
print(question.lines[0])
print("")

answer1 = input("Try to guess the shape: \n")

if answer1 == question.name:
    print('\nFirst try and You are right!\n')
    question.printFullAnswer()
    exit()
else:
    print("")
    print(question.lines[0])
    print(question.lines[1])
    print("")
    answer2 = input("Try again: \n")

if answer2 == question.name:
    print('\nSecond try and You are right!\n')
    question.printFullAnswer()
    exit()
else:
    print("")
    question.printFullAnswer()
    print("The right answere was: " + question.name + ".")
    print("")
    exit()
