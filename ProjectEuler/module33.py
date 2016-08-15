from module30 import GetNumArray

def WeirdSimplification(nominator, denominator):
    numArr = GetNumArray(nominator)
    denArr = GetNumArray(denominator)

    repeatedNum = -1

    for num in numArr:
        for den in denArr:
            if (num == den):
                repeatedNum = num

    if (repeatedNum > 0):
        numArr.remove(repeatedNum)
        denArr.remove(repeatedNum)








def SolveProblem():
    for nominator in range(10,100):
        for denominator in range(10,100):
            WeirdSimplification(nominator, denominator)