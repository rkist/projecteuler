class BigNumber(object):
    """a very big number"""
    def __init__(self, value):
        self.number = []
        self.base = 10
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

        valueAux = value
        if (value > 0):
            while valueAux > 0:
                if (index == len(self.number)):
                    self.number.append(0)
                v = valueAux % self.base
                valueAux /= self.base

                currVal = self.number[index] + v

                valueAux += currVal / self.base
                self.number[index] = (currVal) % self.base
                index += 1

    def IsZero(self):
        for num in self.number:
            if (num != 0):
                return False
        return True


    def DecreaseOne(self):
        index = 0

        while True:
            currVal = self.number[index] - 1
            if (currVal < 0):
                if (self.IsZero()):
                    break;
                self.number[index] = 9
                index += 1
            else:
                self.number[index] = currVal
                break





    @property
    def Number(self):
        rvcp = self.number[:]
        rvcp.reverse()
        return rvcp

    @property
    def Base(self):
        return self.base

    #@Base.setter
    #def Base(self, value):
    #    self.base = value


    def __add__(self, other):
        otherNumberReversed = other.Number
        otherNumberReversed.reverse()

        thisNumber = self.number[:]

        index = 0
        while True:
            if thisNumber[-1] == 0 and otherNumberReversed[-1] == 0:
                break
            if (index == len(thisNumber)):
                thisNumber.append(0)
            if (index+1 == len(otherNumberReversed)):
                otherNumberReversed.append(0)

            currVal = thisNumber[index] + otherNumberReversed[index]
            otherNumberReversed[index+1] += (currVal) / self.base
            thisNumber[index] = (currVal) % self.base
            
            index += 1

        thisNumber.reverse()
        return BigNumber(thisNumber)

    def __iadd__(self, other):
        otherNumberReversed = other.Number
        otherNumberReversed.reverse()

        index = 0
        while True:
            if self.number[-1] == 0 and otherNumberReversed[-1] == 0:
                break
            if (index == len(self.number)):
                self.number.append(0)
            if (index+1 == len(otherNumberReversed)):
                otherNumberReversed.append(0)

            currVal = self.number[index] + otherNumberReversed[index]
            otherNumberReversed[index+1] += (currVal) / self.base
            self.number[index] = (currVal) % self.base
            
            index += 1

        return self

    def __mul__(self, other):

        while (not other.IsZero()):
            self += self
            other.DecreaseOne()

        return self
            


    #def __mul__(self, other):
    #    otherNumberReversed = other.Number
    #    otherNumberReversed.reverse()

    #    thisNumber = self.number[:]

    #    index1 = 0
    #    index2 = 0
    #    while True:
    #        while True:
    #            if thisNumber[-1] == 0 and otherNumberReversed[-1] == 0:
    #                break
    #            if (index == len(thisNumber)):
    #                thisNumber.append(0)
    #            if (index+1 == len(otherNumberReversed)):
    #                otherNumberReversed.append(0)

    #            currVal = thisNumber[index1] * otherNumberReversed[index2]
    #            otherNumberReversed[index+1] += (currVal) / self.base
    #            thisNumber[index] = (currVal) % self.base
            
    #            index2 += 1
    #        index1 += 1



    #    thisNumber.reverse()
    #    return BigNumber(thisNumber)

