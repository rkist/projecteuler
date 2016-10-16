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

def Diff(arr1, arr2, expDiff):
    eq = 0
    diffArr1 = []
    diffArr2 = []
    length = len(arr1)
    for i in range(length):
        if arr1[i] == arr2[i]:
            eq+=1
        else:
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

def Filter(arr, primeArrays, expDiff):
    res = []
    for prime in primeArrays:
        if (Diff(arr, prime, expDiff)):
            res.append(prime)
    return res




def SolveProblem():
    print "."   
    primes = GetPrimesInRange(range(10**4,10**5))

    print "."   
    primeArrays = []
    for item in primes:
        a = ConvertIntToIntArray(item)
        primeArrays.append(a)
    primeArraysLen = len(primeArrays)

    print "." 

    for prime in primeArrays:
        alike = Filter(prime, primeArrays, 2)
        alikeLen = len(alike)
        print alikeLen
        if (alikeLen >= 6):
            print alike
        





    

    
    #affinityMatrix = [[[] for x in range(primeArraysLen)] for y in range(primeArraysLen)] 
    #for i in range(primeArraysLen):
    #    for j in range(primeArraysLen):
                                                                                                                                                                                                                                                                                                          
            #affinityMatrix[i][j] = FilterCommonTerms(primeArrays[i], primeArrays[j])
    
    print "."   

    

    #dicArr = []
    #for i in range(primeArraysLen):
    #    dic = {}
    #    for j in range(primeArraysLen):
    #        kl = affinityMatrix[i][j]
    #        k = str(kl)
    #        if IsValidAffinity(kl):
    #            if dic.has_key(k):
    #                a,b = dic[k]
    #                dic[k] = (a,b+1)
    #            else:
    #                dic.update({k : (kl, 0)})       
    #    dicArr.append(dic)

    #max = 0
    #itemMax = (0,0)
    #for d in dicArr:
    #    for k, v in d.items():
    #        a,b = v
    #        if (b > max):
    #            max = b
    #            itemMax = v

    #print itemMax
    



    return -1