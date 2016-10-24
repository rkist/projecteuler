from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *




def SolveProblem():
    print "." 
    
    maxSum = 0

    for a in range(100):
        for b in range(100):
            n = a**b
            nArr = ConvertIntToIntArray(n)
            sum = SumArray(nArr)

            if (sum > maxSum):
                print sum
                maxSum = sum

    

      
    return maxSum