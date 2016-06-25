
class BinTree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def __init__(self, startValue):
        self.value = startValue
        self.left = None
        self.right = None

    def __str__(self):
        retVal = str(self.value)
        l = self.GetLeft()
        r = self.GetRight()

        if (l):
            retVal += str(l)
        else:
            retVal += "0"

        retVal += " "

        if (r):
            retVal += str(r)
        else:
            retVal += "0"

        retVal += "\n"

        return retVal


    def GetValue(self):
        return self.value

    def SetValue(self, newValue):
        self.value = newValue

    def SetLeft(self, newLeft):
        self.left = newLeft

    def SetRight(self, newRight):
        self.right = newRight

    def GetLeft(self):
        return self.left 

    def GetRight(self):
        return self.right 






aaa = BinTree(3)
bbb = BinTree(5)
ccc = BinTree(6)
aaa.SetLeft(bbb)
aaa.SetRight(ccc)




print aaa























