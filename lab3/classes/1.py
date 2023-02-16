class String:
    def __init__(self):
        self.str = ""

    def getStr(self):
        self.str = input()

    def printStr(self):
        print(self.str.upper())

str = String()
str.getStr()
str.printStr()