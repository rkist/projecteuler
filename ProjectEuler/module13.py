class BigNumber:
    number = []
    def __init__(self, value = 0):
        while value > 0:
            self.number.append(value%10)
            value/=10

    def __str__(self):
        retstr = ""
        revnumber = self.number[:]
        revnumber.reverse()
        for n in revnumber:
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


        