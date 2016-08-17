from math import *

def GetDivisorsArray(value):
    arr = []
    for divisor in range(2,int(sqrt(value) + 1)+1):
        if (value != divisor) and (value % divisor == 0):
            arr.append(divisor)
    return arr

def IsPrime(value):
    if (value < 2):
        return False
    for divisor in range(2,int(sqrt(value) + 1)+1):
        if (value != divisor) and (value % divisor == 0):
            return False
    return True

def Factorial(num):
    return factorial(num)