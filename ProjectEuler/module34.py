from ArrayHelpers import *
from math import factorial




def SolveProblem():
    
    sumsum = 0

    for num in range(3,100000):
        arr = ConvertIntToIntArray(num)

        sum = 0
        for n in arr:
            sum += factorial(n)

        if (sum == num):
            print num
            sumsum += sum
    
    print sumsum


