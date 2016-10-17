from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *


def Diff(arr1, arr2, expDiff):
    diffArr1 = []
    diffArr2 = []
    length = len(arr1)
    for i in range(length):
        if arr1[i] != arr2[i]:
            diffArr1.append(arr1[i])
            diffArr2.append(arr2[i])
            if (len(diffArr1) <= expDiff):
                for n in diffArr1:
                    if (n != arr1[i]):
                        return False
            else:
                return False
            if (len(diffArr2) <= expDiff):
                for n in diffArr2:
                    if (n != arr2[i]):
                        return False
            else:
                return False

    return (len(diffArr1) == expDiff)

def FilterPerResemblance(arr, primeArrays, expDiff):
    res = []
    for prime in primeArrays:
        if (Diff(arr, prime, expDiff)):
            res.append(prime)
    return [arr] + res

def Classify(alike):
    d = dict()
    alikeLen = len(alike)
    firstArr = alike[0]
    firstArrLen = len(firstArr)

    for i in range(1, alikeLen):
        arr = alike[i]
        diffPos = []
        for j in range(firstArrLen):
            if firstArr[j] != arr[j]:
                diffPos.append(j)
        diffPosInt = ConvertIntArrayToInt(diffPos)
        if (diffPosInt not in d):
            d[diffPosInt] = [firstArr] + [arr]
        else:
            d[diffPosInt] += [arr]             

    return d

def Solve(primeArrays, diff, numOfNum, result):
    primeArraysLen = len(primeArrays)
    for i in range(primeArraysLen):
        alike = FilterPerResemblance(primeArrays[i], primeArrays[i:], diff)
        alikeLen = len(alike)
        if (alikeLen >= numOfNum):
            #print "(" + str(alikeLen) + ") => " + str(alike)
            d = Classify(alike)
            for k, v in d.iteritems():
                vLen = len(v)
                if (vLen >= numOfNum-1):
                    print "(" + str(vLen) + ") => " + str(v)
                    if (vLen >= numOfNum):
                        result.put((ConvertIntArrayToInt(v[0]), vLen, v))




def SolveProblem():
    print "."   

    numOfDigits = 5
    primes = GetPrimesInRange(range(10**(numOfDigits-1),10**numOfDigits))

    print "."   

    primeArrays = []
    for item in primes:
        a = ConvertIntToIntArray(item)
        primeArrays.append(a)
    

    print "." 

    resultQueue = Queue()

    t1 = Process(target=Solve, args=(primeArrays, 2, 7, resultQueue))
    t1.start()

    t2 = Process(target=Solve, args=(primeArrays, 3, 7, resultQueue))
    t2.start()

    t3 = Process(target=Solve, args=(primeArrays, 4, 7, resultQueue))
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    result_list = []
    while not resultQueue.empty():
        result_list.append(resultQueue.get())



    print "." 

    return result_list