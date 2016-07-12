class BinTreeNode:
    row = 0
    col = 0

    def __init__(self):
        self.row = 0
        self.col = 0

    def Print(self):
        print str(self.row) + "," + str(self.col)

    def GetLeftSon(self):
        newNode = BinTreeNode()
        newNode.row = self.row + 1  
        newNode.col = self.col      
        return newNode

    def GetRightSon(self):
        newNode = BinTreeNode()
        newNode.row = self.row + 1  
        newNode.col = self.col + 1  
        return newNode


class BinTriagle:  
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

    def IsNodeBoundaries(self, node):
        return node.row < self.size and node.col < self.size

    def GetValue(self, node):
        if (self.IsNodeBoundaries(node)):
            return self.Arrays[node.row][node.col]
        return 0




def Recursion(bt, node):
    val = bt.GetValue(node)
    if (val == 0):
        return val

    leftNode = node.GetLeftSon()
    rightNode = node.GetRightSon()

    leftVal = Recursion(bt,leftNode)
    rightVal = Recursion(bt,rightNode)

    if (leftVal < rightVal):
        retVal = val + rightVal
    else:        
        retVal = val + leftVal

    #print str(node.row) + "," + str(node.col) + ": " + str(retVal)
    return retVal