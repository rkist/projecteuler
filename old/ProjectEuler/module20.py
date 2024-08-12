import math


def SolveEx20():
    value = math.factorial(100)

    valueStr = str(value)

    sum = 0
    for char in valueStr:
        print char
        sum += int(char)

    print valueStr
    print sum