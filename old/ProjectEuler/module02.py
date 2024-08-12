def GetSumOfMultiplesInArray(multipleOf, values):
    sum = 0
    for x in values:
        if x % multipleOf == 0:
            sum += x
    return sum

def GetSumOfNonMultiplesInArray(multipleOf, array):
    sum = 0
    for x in array:
        if x % multipleOf != 0:
            sum += x
    return sum

def FibonacciRecursion(index):
    if index == 0:
        return 1
    if index == 1:
        return 2
    return FibonacciRecursion(index-1) + FibonacciRecursion(index-2)

def BuildFibonacciSequenceIndexBased(maxIndex):
    arr = []
    for index in range(0,maxIndex):
        arr.append(FibonacciRecursion(index))

    return arr

def BuildFibonacciSequenceMaximumBased(maxValue):
    arr = []
    currVal = 0
    index = 0
    while True:
        currVal = FibonacciRecursion(index)
        index+=1
        if currVal < maxValue:
            arr.append(currVal)
        else:
            return arr

        

    