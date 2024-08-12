import math

def GetNumArray(number):
    arr = []  
    while (number > 0):
       rest = number % 10
       arr.append(rest)
       number = number / 10

    arr.reverse()
    return arr
   
def GetSumonPotence(arr,potence):
    sum = 0
    for n in arr:
        sum += n**potence

    return sum


def SolveProblem():
    sumsum = 0

    for n in range(2, 1000000):
        arr = GetNumArray(n)
        sum = GetSumonPotence(arr, 5)

        if (n == sum):
            sumsum += sum
            print n

    print sumsum
        