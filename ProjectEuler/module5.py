def FirstDivisibleInArray(array):
    arrayLen = len(array)
    divisorIndex = 0
    current = array[divisorIndex]
    

    while divisorIndex < arrayLen:
        divisor = array[divisorIndex]
        if current % divisor == 0:
            divisorIndex += 1
        else:
            divisorIndex = 0
            current += 1
    return current


def FirstDivisibleInRange(start, end):
    current = end
    divisor = start

    while divisor < end:
        if current % divisor == 0:
            divisor += 1
        else:
            divisor = start
            current += 1
    return current

