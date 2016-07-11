class BinTriagle:
    row = 0
    col = 0
    size = 0

    def __init__(self, path):
        self.Arrays = self.GetInput(path)
        self.size = len(self.Arrays)

    #[linha][coluna]
    def GetInput(self, path):
        numArr = []
        inputStr = file(path).read()
        lines = inputStr.splitlines()        
        for line in lines:
            numsStr = line.split(" ")
            tempArr = []
            for numStr in numsStr:
                tempArr.append(int(numStr))
            numArr.append(tempArr)
        return numArr

    def Print(self):
        for line in self.Arrays:
            printArray = ""
            for element in line:
                printArray += str(element) + " "
            print printArray

    def InsideBoundaries(self):
        return self.row < self.size and self.col < self.size

    def getSelf(self):
        if (self.InsideBoundaries()):
            return self.Arrays[self.row][self.col]
        return 0

    def GetLeft(self):
        self.row += 1        
        if (self.InsideBoundaries()):
            return self.Arrays[self.row][self.col]
        return 0      

    def GetRight(self):
        self.row += 1
        self.col += 1
        if (self.InsideBoundaries()):
            return self.Arrays[self.row][self.col]
        return 0






bt = BinTriagle("input/input18.1.txt")
bt.Print()

print bt.getSelf()
print bt.GetLeft()
print bt.GetRight()
print bt.GetRight()
print bt.GetRight()
print bt.GetRight()



#numberOfLines = len(inputArrays)

#for lineNumber in xrange(0,numberOfLines):
#    print inputArrays[lineNumber]

























