def ConvertIntArrayToInt(numList):       # [1,2,3]
    s = map(str, numList)                # ['1','2','3']
    s = ''.join(s)                       # '123'
    s = int(s)                           # 123
    return s

def ConvertIntToIntArray(number):
    arr = []  
    while (number > 0):
       rest = number % 10
       arr.append(rest)
       number = number / 10

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