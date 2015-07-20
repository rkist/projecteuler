
def GetInput(path):
    numArr = []
    inputStr = file(path).read()
    lines = inputStr.splitlines()
    for line in lines:
        bn = BigNumber(line)
        numArr.append(bn)
    return numArr

class BigNumber(object ):
    def __init__(self, value):
        self.number = []
        if isinstance(value, basestring):
            for ch in reversed(value):
                self.number.append(int(ch))
        elif isinstance(value, list):
            for i in reversed(value):
                self.number.append(i)


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

    @property
    def Number(self):
        rvcp = self.number[:]
        rvcp.reverse()
        return rvcp


    def __add__(self, other):
        otherNumberReversed = other.Number
        otherNumberReversed.reverse()
        otherNumberReversed.append(0)

        thisNumber = self.number[:]

        for index in range(0,len(otherNumberReversed)):
            if (index == len(thisNumber)):
                thisNumber.append(0)
            currVal = thisNumber[index] + otherNumberReversed[index]
            if currVal > 9:
                otherNumberReversed[index+1] += 1
            thisNumber[index] = (currVal) % 10

        thisNumber.reverse()
        return BigNumber(thisNumber)


    def __iadd__(self, other):
        otherNumberReversed = other.Number
        otherNumberReversed.reverse()
        otherNumberReversed.append(0)

        for index in range(0,len(otherNumberReversed)):
            if (index == len(self.number)):
                self.number.append(0)
            currVal = self.number[index] + otherNumberReversed[index]
            if currVal > 9:
                otherNumberReversed[index+1] += 1
            self.number[index] = (currVal) % 10
        return self




        