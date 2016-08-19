from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *


def GetNameValue(name):
    sum = 0
    for ch in name:
        ch = ch.lower()
        sum += ord(ch) - (ord('a') - 1)
    return sum

def TriangleNumber(n):
    res = (n * (n + 1)) / 2
    return res


def SolveProblem():
    names = ReadAndCleanTextInput("input/input42.txt")

    triangleNameCounter = 0
    for name in names:
        nameVal = GetNameValue(name)
        i = 0
        while (True):
            tn = TriangleNumber(i)
            if (tn == nameVal):
                triangleNameCounter += 1
                print triangleNameCounter
            if (tn > nameVal):
                break
            i += 1

    return triangleNameCounter