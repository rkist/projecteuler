from math import *

def SumArrayValues(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def MultiplyArrayValues(arr):
    mul = 1
    for num in arr:
        mul *= num
    return mul

def Range(sortedArr):
    return sortedArr[len(sortedArr)-1] - sortedArr[0]
    
def Average(arr):
    return SumArrayValues(arr)/float(len(arr))
    
def Median(sortedArr):
    l = len(sortedArr)
    if (l % 2 == 1):
        return sortedArr[l/2]
    return (sortedArr[(l/2)-1] + sortedArr[(l/2)])/float(2)

def FindList(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return -1

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


def ConvertStringToInt(string, base = 10):
    tot = 0
    for char in string:
        tot *= base
        num = int(char)
        tot += num
    return tot

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


#def AreSortedArraysDisjointed(arr1, arr2):
#    for n in arr1:
#        if (IsInArray(arr2, n)):
#            return False
#    return True

def AreSortedArraysDisjointed(set1, set2):
    return set1.isdisjoint(set2)

def IsInArray(array, value):
    return SearchArray(array, value) >= 0

def SearchArray(array, value):
    beg = 0
    end = len(array)
    return SearchArrayRecursion(array, value, beg, end)

def SearchArrayRecursion(array, value, beg, end):
    diff = end - beg
    halfDiff = diff / 2

    mid = beg + halfDiff
    midVal = array[mid]

    if (halfDiff == 0):
        if (value == midVal):
            return mid
        else:
            return -1

    if (value == midVal):
        return mid
    elif (value < midVal):
        return SearchArrayRecursion(array, value, beg, mid)
    else:
        return SearchArrayRecursion(array, value, mid, end)


  

def Combination(array, combinationSize = 0):
    combinations = []
    for i in range(0,len(array)):
        CombinationRecursion(i, array, [], combinations)
    return combinations


def CombinationRecursion(index, items, arrayToAdd, combinations):
    itemsLen = len(items)
    if (index == itemsLen):
        return

    newArrayToAdd = arrayToAdd + [items[index]]
    combinations.append(newArrayToAdd)

    for i in range(index, itemsLen):        
        CombinationRecursion(i+1, items, newArrayToAdd, combinations)




def GenerateSumsCombinations(number):
    result = [[number]]
    for n in range(1,number):
        result += GenerateSumsCombinationRecursion(number, [n], n)
    return result

def GenerateSumsCombinationRecursion(finalSum, partialArray, partialSum):
    if (partialSum == finalSum):
        return [partialArray]

    lastAddedValue = partialArray[-1]

    sums = []
    for n in range(lastAddedValue, finalSum - partialSum + 1):
        sums += GenerateSumsCombinationRecursion(finalSum, partialArray + [n], partialSum + n)
    return sums


def GenerateSumsPermutations(number):
    result = [[number]]
    for n in xrange(1,number):
        result += GenerateSumsPermutationRecursion(number, [n], n)
    return result

def GenerateSumsPermutationRecursion(finalSum, partialArray, partialSum):
    if (partialSum == finalSum):
        return [partialArray]

    sums = []
    for n in xrange(1, finalSum - partialSum + 1):
        sums += GenerateSumsPermutationRecursion(finalSum, partialArray + [n], partialSum + n)
    return sums
        
        


def ArePermutations(nums): #if these numers are permutations of each other
    numsAlgs = []
    for num in nums:
        numsAlgs.append(ConvertIntToIntArray(num))
    
    comparer = sorted(numsAlgs[0])

    for numAlgs in numsAlgs:
        if (comparer != sorted(numAlgs)):
            return False
    return True




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


def Determinant(matrix):
    return det(matrix)   
    
def det(M):
    size = len(M)    
    if (size == 1):
        return M[0][0]    
    if (size == 2):
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    
    sum = 0
    for i in range(size):
        sum += (-1)**(i) * M[0][i] * det(minor(M, 0, i))
    
    return sum
    
def minor(M, ii,jj):
    newM = []
    for i,row in enumerate(M):
        if (i != ii):
            newM.append([cell for j, cell in enumerate(row) if j != jj])
    return newM


def PathFinder(maze): # can go to lower right corner from upper left one
    m = []
    for line in maze.splitlines():
        l = []
        for c in line:
            if (c == '.'):
                l.append(0)
            if (c == 'W'):
                l.append(1)
        m.append(l)
        
#     printMaze(m)
        
    return path_finder_recursion( m, (0,0), (len(m)-1,len(m[0])-1) , 0)
    
def printMaze(maze):
    for line in maze:
        print(line)
    print()
    
def path_finder_recursion(maze, currPos, destiny, recSize):
    len0 = len(maze)
    len1 = len(maze[0])
    i = currPos[0]
    j = currPos[1]
    
    if (recSize > 500):
        return False
    
#     printMaze(maze)
    
    if (currPos == destiny):
        return True
    
    if (i < 0 or j < 0):
        return False
        
    if (i >= len0 or j >= len1):
        return False
        
    if (maze[i][j] == 1):
        return False
        
    maze[i][j] = 1    
    vectors = [(+1,0),(0,+1),(-1,0),(0,-1)]
    
    for vector in vectors:
        newPos = (currPos[0] + vector[0], currPos[1] + vector[1])
        if (path_finder_recursion(maze[:], newPos, destiny, recSize + 1)):
            return True
            
    return False   
    
    
    

