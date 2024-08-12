
def SumOfSquaresOfArray(values):
    sum = 0
    for val in values:
        sum += val*val
    
    return sum

def SquareOfSumOfArray(values):
    sum = 0
    for val in values:
        sum += val

    sum = sum*sum
    return sum