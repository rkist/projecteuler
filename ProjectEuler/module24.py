
def Permute(string):
    stringToAdd = ""
    stringToRemove = string
    permutations = []
    for i in range(0,len(stringToRemove)):
        PermuteRecursion(i, stringToAdd, stringToRemove, permutations)

    return permutations


def PermuteRecursion(index, stringToAdd, stringToRemove, permutations):

    newStringToAdd = stringToAdd + stringToRemove[index]
    newStringToRemove = stringToRemove[:index] + stringToRemove[index+1:]

    if (len(newStringToRemove) == 0):
        permutations.append(newStringToAdd)
        return

    for i in range(0,len(newStringToRemove)):
        PermuteRecursion(i, newStringToAdd, newStringToRemove, permutations)


def SolveEx24():

    str = "0123456789"

    perms = Permute(str)

    print perms[1000000-1]


