
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



def SolveProblem():

    wString = "1428571428571428571428571429"
    subString = "142857"
    print FindNumberOfTimesSubstringRepeatsItselfInsideString(subString, wString)

    numbers = range(2,10)

    for num in numbers:
        numStr = GetStringOfTheDivisionByOneInTenBase(num)
        cleanNumStr = CleanString(numStr)
        result = AAA(cleanNumStr)
        print numStr + " " + cleanNumStr + " " + result

    

