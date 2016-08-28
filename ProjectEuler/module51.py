from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *


def FilterCommonTerms(arr1, arr2):
    commArr = []
    length = len(arr1)
    for i in range(length):
        if (arr1[i] == arr2[i]):
            commArr.append(arr1[i])
        else:
            commArr.append(-1)
    return commArr





def SolveProblem():
    print "."   
    primes = GetPrimesInRange(range(10,99+1))

    print "."   
    primeArrays = []
    for item in primes:
        a = ConvertIntToIntArray(item)
        primeArrays.append(a)
    primeArraysLen = len(primeArrays)

    print "." 
    affinityMatrix = [[[] for x in range(primeArraysLen)] for y in range(primeArraysLen)] 
    for i in range(primeArraysLen):
        for j in range(primeArraysLen):
            affinityMatrix[i][j] = FilterCommonTerms(primeArrays[i], primeArrays[j])
    
    print "."   

    dicArr = []
    for i in range(primeArraysLen):
        dic = {}
        for j in range(primeArraysLen):
            kl = affinityMatrix[i][j]
            k = str(kl)
            if k != '[-1, -1]':
                if dic.has_key(k):
                    a,b = dic[k]
                    dic[k] = (a,b+1)
                else:
                    dic.update({k : (kl, 0)})       
        dicArr.append(dic)

    max = 0
    itemMax = (0,0)
    for d in dicArr:
        for k, v in d.items():
            a,b = v
            if (b > max):
                max = b
                itemMax = v

    print itemMax
    



    return -1