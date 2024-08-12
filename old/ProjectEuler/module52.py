from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *

def GenSortedArray(n):
    nArr = ConvertIntToIntArray(n)
    nArr.sort()
    return nArr



def SolveProblem():
   
    print "."   

    for n in xrange(1,10**9):
        n1Arr = GenSortedArray(1*n)
        n2Arr = GenSortedArray(2*n)
        n3Arr = GenSortedArray(3*n)
        n4Arr = GenSortedArray(4*n)
        n5Arr = GenSortedArray(5*n)
        n6Arr = GenSortedArray(6*n)

        if (n1Arr == n2Arr == n3Arr == n4Arr == n5Arr == n6Arr):
            return n


    print "."   

    return -1