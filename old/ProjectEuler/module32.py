
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


def ConvertArrayOfIntToInt(numList):     # [1,2,3]
    s = map(str, numList)                # ['1','2','3']
    s = ''.join(s)                       # '123'
    s = int(s)                           # 123
    return s

def GeneratePossibleMultiplicationsWithGivenArray(numberArray):
    numberArrayLen = len(numberArray)

    possibleMultsArray = []

    for multCutIndex in range(1,numberArrayLen-1):
        for equalCutIndex in range(multCutIndex+1,numberArrayLen):
            mult0Arr = numberArray[:multCutIndex]
            mult1Arr = numberArray[multCutIndex:equalCutIndex]
            resArr = numberArray[equalCutIndex:]

            mult0 = ConvertArrayOfIntToInt(mult0Arr)
            mult1 = ConvertArrayOfIntToInt(mult1Arr)
            res = ConvertArrayOfIntToInt(resArr)

            combination = [mult0, mult1, res]
            possibleMultsArray.append(combination)
    
    return possibleMultsArray
            


def SolveProblem():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   
    perms = Permute(arr)

    pandigitalMultiplications = set()
    for perm in perms:
        possMults = GeneratePossibleMultiplicationsWithGivenArray(perm)
        for mult in possMults:
            if (mult[0] * mult[1] == mult[2]):
                print str(mult[0]) + " * " + str(mult[1]) + " == " + str(mult[2])
                pandigitalMultiplications.add(mult[2])

    print pandigitalMultiplications

    sum = 0
    for num in pandigitalMultiplications:
        sum += num

    print sum


