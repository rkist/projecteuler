from math import *

def SumArray(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def IsPalindrome(arr):
    for index in range(0,len(arr)/2):
        if arr[index] != arr[-(index+1)]:
            return False
    return True


def IsNumberPalindrome(num, base = 10):
    arr = ConvertIntToIntArray(num, base)
    for index in range(0,len(arr)/2):
        if arr[index] != arr[-(index+1)]:
            return False
    return True

def InvertNumber(num, base = 10):
    numArr = ConvertIntToIntArray(num, base)
    numArrInv = numArr[::-1]
    numInv = ConvertIntArrayToInt(numArrInv, base)
    return numInv


def ConvertIntArrayToInt(numList, base = 10):
    tot = 0
    for num in numList:
        tot *= base
        tot += num
    return tot

def ConvertIntToIntArray(number, base = 10):
    arr = []  
    while (number > 0):
       rest = number % base
       arr.append(rest)
       number = number / base
    arr.reverse()
    return arr



def GetNameValue(name):
    sum = 0
    for ch in name:
        ch = ch.lower()
        sum += ord(ch) - (ord('a') - 1)
    return sum




def IsInArray(array, value):
    return SearchArray(array, value) >= 0

def SearchArray(array, value):
    beg = 0
    end = len(array)
    return SearchArrayRecursion(array, value, beg, end)

def SearchArrayRecursion(array, value, beg, end):
    halfDiff = (end - beg) / 2
    if (halfDiff == 0):
        return -1

    mid = beg + halfDiff
    midVal = array[mid]

    if (value == midVal):
        return mid
    elif (value < midVal):
        return SearchArrayRecursion(array, value, beg, mid)
    else:
        return SearchArrayRecursion(array, value, mid, end)


#TODO: combination
def Combination(array):
    pass



def Permute(array, permutationSize = 0): #Arranjo
    if (permutationSize == 0):
        permutationSize = len(array)
    arrayToAdd = []
    arrayToRemove = array
    permutations = []
    for i in range(0,len(arrayToRemove)):
        _PermuteRecursion_(i, arrayToAdd, arrayToRemove, permutations, permutationSize)

    return permutations


def _PermuteRecursion_(index, arrayToAdd, arrayToRemove, permutations, permutationSize):
    newArrayToAdd = arrayToAdd + [arrayToRemove[index]]
    newArrayToRemove = arrayToRemove[:index] + arrayToRemove[index+1:]

    if (len(newArrayToAdd) == permutationSize):
        permutations.append(newArrayToAdd)
        return

    for i in range(0,len(newArrayToRemove)):
        _PermuteRecursion_(i, newArrayToAdd, newArrayToRemove, permutations, permutationSize)


def RemoveDuplicatedItemsFromArray(array):
    itemsSet = set()
    for item in array:
        itemsSet.add(item)
    itemsList = list(itemsSet)
    return itemsList

