from module03 import *

def SumArray(arr):
    sum = 0
    for n in arr:
        sum += n
    return sum

def DivisorsButLast(n):
    return GetAllDivisorsArray(n)[0:-1]


def GetAmicableNumbersInArray(array):
    amicableNumbersArray = []
    for a in array:
        divsA = DivisorsButLast(a)

        b = SumArray(divsA)

        #print sum01

        divsB = DivisorsButLast(b)

        sumB = SumArray(divsB)

        #print sum02

        if (a == sumB and a != b):
            amicableNumbersArray.append(a)

    return amicableNumbersArray

def SolveEx21():
    amicableNumbersArray = GetAmicableNumbersInArray(range(0, 10000))
    print SumArray(amicableNumbersArray)


