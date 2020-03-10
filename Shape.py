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
