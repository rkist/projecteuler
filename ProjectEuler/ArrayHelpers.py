from math import *

def IsPalindrome(arr):
    for index in range(0,len(arr)/2):
        if arr[index] != arr[-(index+1)]:
            return False
    return True

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

def Permute(array):
    arrayToAdd = []
    arrayToRemove = array
    permutations = []
    for i in range(0,len(arrayToRemove)):
        _PermuteRecursion_(i, arrayToAdd, arrayToRemove, permutations)

    return permutations


def _PermuteRecursion_(index, arrayToAdd, arrayToRemove, permutations):
    newArrayToAdd = arrayToAdd + [arrayToRemove[index]]
    newArrayToRemove = arrayToRemove[:index] + arrayToRemove[index+1:]

    if (len(newArrayToRemove) == 0):
        permutations.append(newArrayToAdd)
        return

    for i in range(0,len(newArrayToRemove)):
        _PermuteRecursion_(i, newArrayToAdd, newArrayToRemove, permutations)