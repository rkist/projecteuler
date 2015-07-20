
def GetInput(path):
    numArr = []
    inputStr = file(path).read()
    lines = inputStr.splitlines()
    for line in lines:
        bn = BigNumber(line)
        numArr.append(bn)
    return numArr

class BigNumber:
    def __init__(self, value = ""):
        self.number = []
        for ch in reversed(value):
            self.number.append(int(ch))

    def __str__(self):
        retstr = ""
        for n in reversed(self.number):
            retstr += str(n)
        return retstr

    def AddInt(self, value):
        index = 0
        carry = 0
        while value > 0:
            if (index == len(self.number)):
                self.number.append(0)
            v = value % 10
            value /= 10
            currVal = self.number[index] + v
            if currVal > 9:
                value += 1
            self.number[index] = (currVal) % 10
            index += 1



    #def __add__(self, other):


        