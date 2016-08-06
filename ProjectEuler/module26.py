
from decimal import *


def GetStringOfTheDivisionByOneInTenBase(d):
    x = Decimal(1.0)/Decimal(d)
    return "{:2.30f}".format(x)

def CleanString(str):
    str = str[2:]
    str = str.replace("0", "")
    return str

def HasSubString(subString, string):
    subStringIndex = 0
    for stringIndex in range(0,len(string)):
        if (string[stringIndex] == subString[subStringIndex]):             
            subStringIndex += 1
        else:
            subStringIndex = 0          
        
        if (subStringIndex == len(subString)):
            return True
    return False

def FindNumberOfTimesSubstringRepeatsItselfInsideString(subString, string):
    repetitionsCounter = 0
    wString = string
    stringIndex = 0
    subStringIndex = 0
    while (stringIndex < len(wString)):
        if (wString[stringIndex] == subString[subStringIndex]):             
            subStringIndex += 1
        else:
            subStringIndex = 0          
        
        stringIndex += 1  
        if (subStringIndex == len(subString)):
            repetitionsCounter += 1
            #wString = wString[:stringIndex-len(subString)] + wString[stringIndex:]
            #stringIndex = 0
            subStringIndex = 0                    
            
    return repetitionsCounter


def FindBiggestRepeatedSubString(str): #not working
    result = ""
    for i in range(0,len(str)):
        for j in range(i+1,len(str)):
            subStr = str[i:j]
            if(HasSubString(subStr, str)):
                if (len(subStr) > len(result)):
                    result = subStr
    return result

def AAA(str): #not working
    result = ""
    biggestSubStrSize = 0
    biggestNumberOfRepetitionsOfSubStr = 0
    for i in range(0,len(str)):
        for j in range(i+1,len(str)):
            subStr = str[i:j]
            numRep = FindNumberOfTimesSubstringRepeatsItselfInsideString(subStr, str)
            resLen = len(subStr)
            if (numRep > 2  and biggestSubStrSize <= resLen):
                biggestNumberOfRepetitionsOfSubStr = numRep
                biggestSubStrSize = resLen
                result = subStr
    return result




def YieldDivisionResult(denominator):    
    rest = 1
    while (rest != 0):
        rest *= 10
        result = rest / denominator
        rest = rest % denominator
        yield result


def GetDivisionResultArray(denominator, size):
    resultArray = []
    for i in YieldDivisionResult(denominator):
        resultArray.append(i)
        resultArraySize = len(resultArray)

        if (resultArraySize == size):
            break
    return resultArray

    
def Repeats(arr, start1, start2):
    k = 0
    limit = start2 - start1

    if (start2 + limit > len(arr)):
        return False
    
    while(k < limit):
        pos1 = start1 + k
        pos2 = start2 + k
        if (arr[pos1] != arr[pos2]):
            return False
        k += 1
    return True


def GetSmallestSequence(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            size = j-i

            if (Repeats(arr, i, j) and Repeats(arr, i, j + size)):
               return size
    return 0


def SolveProblem():

    numbers = range(2,1000)

    biggestSize = 0
    biggestNum = 0

    for num in numbers:
        arr = GetDivisionResultArray(num,10000)
        size = GetSmallestSequence(arr)
        
        if (size > biggestSize):
            biggestSize = size
            biggestNum = num
            
        print str(num) + " " + str(size)

    print str(biggestNum) + " " + str(biggestSize)



    

