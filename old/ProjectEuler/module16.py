
numberBase = 10
def SumDigits(number):
    sum = 0
    while (number > 0):
        partNum = number % numberBase
        number = number / numberBase
        sum += partNum

    return sum