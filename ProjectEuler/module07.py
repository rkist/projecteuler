import math

def GetDivisorsArrayOpt(value):
    arr = []
    for divisor in range(2,int(math.sqrt(value) + 1)+1):
        if value % divisor == 0:
            arr.append(divisor)

    return arr

def IsPrime(value):
    if (value < 0):
        return False

    divisors = GetDivisorsArrayOpt(value)
    if len(divisors) == 0:
        return True
    return False

def GetFirstPrimeNumbersUpTo(value):
    arr = []
    currValue = 2
    while len(arr) < value:
        if IsPrime(currValue):
            arr.append(currValue)
        currValue+=1
    return arr

def GetPrimeNumbersUpTo(value):
    arr = []
    currValue = 2
    while currValue < value:
        if IsPrime(currValue):
            arr.append(currValue)
        currValue+=1
    return arr
