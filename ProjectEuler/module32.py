
def Permute(array):
    arrayToAdd = []
    arrayToRemove = array
    permutations = []
    for i in range(0,len(arrayToRemove)):
        PermuteRecursion(i, arrayToAdd, arrayToRemove, permutations)

    return permutations


def PermuteRecursion(index, arrayToAdd, arrayToRemove, permutations):
    newArrayToAdd = arrayToAdd + [arrayToRemove[index]]
    newArrayToRemove = arrayToRemove[:index] + arrayToRemove[index+1:]

    if (len(newArrayToRemove) == 0):
        permutations.append(newArrayToAdd)
        return

    for i in range(0,len(newArrayToRemove)):
        PermuteRecursion(i, newArrayToAdd, newArrayToRemove, permutations)


def SolveProblem():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    perms = Permute(arr)
    print perms