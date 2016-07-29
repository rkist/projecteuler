from module21 import *

#abundantNumbers = []
#notAbundandNumbers = []

#def IsAbundantNumber(num):
#    if (num in abundantNumbers):
#        return True
#    if (num in notAbundandNumbers):
#        return False

#    divs = DivisorsButLast(num)
#    sum = SumArray(divs)

#    if(sum > num):
#        abundantNumbers.append(num)
#        return True

#    notAbundandNumbers.append(num)
#    return False

abundanceArray = []
def IsAbundantNumber(num):
    if (num < len(abundanceArray)):
        return abundanceArray[num]

    divs = DivisorsButLast(num)
    sum = SumArray(divs)

    isAbundant = False
    if(sum > num):
        isAbundant = True

    abundanceArray.append(isAbundant)
    return isAbundant

def CanBeWrittenBtTheSumOfAbundantNumbers(num):
    for a in range(0,num/2+1):
        b = num - a
        if (IsAbundantNumber(a) and IsAbundantNumber(b)):
            return True
    return False

def SolveEx23():
    nums = range(0,28123+1)
    #nums = range(0,100)

    numbersThatCantBeWrittenByTheSumOfTwoAbundantNumbers = []

    for num in nums:
        if (not CanBeWrittenBtTheSumOfAbundantNumbers(num)):            
            numbersThatCantBeWrittenByTheSumOfTwoAbundantNumbers.append(num)
            print str(num) + " " + str(len(numbersThatCantBeWrittenByTheSumOfTwoAbundantNumbers))

    print numbersThatCantBeWrittenByTheSumOfTwoAbundantNumbers
    print SumArray(numbersThatCantBeWrittenByTheSumOfTwoAbundantNumbers)
