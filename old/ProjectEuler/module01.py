def GetSumOfMultiplesInRange(multipleOf, startRange, endRange):
    sum = 0
    for x in range(startRange,endRange):
        if x % multipleOf == 0:
            sum += x

    return sum