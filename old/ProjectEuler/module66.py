
from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *

def CalcM(D, a, b, k):
    m = 0
    lastDiff = abs(m*m - D)
    lastM = m
    while (True):
        if ((a+b*m) % (k) == 0):
            diff = abs(m*m - D)
            if (diff > lastDiff):
                return lastM
            else:
                lastDiff = diff
                lastM = m
        m += 1

def CalcK(D, a, b):
    return a*a - D*b*b


def Solve(D, a, b):    
    k = CalcK(D, a, b)
    if (k == 1):
        return (a, b)
    else:
        m = CalcM(D, a, b, k)
        aa = (a*m + D*b)/abs(k)
        bb = (a + b*m)/abs(k)
        #kk = (m*m - D)/k
        return Solve(D, aa, bb)



#def SolveProblem():
#    print __name__

#    b = 1
#    D = 181
#    a = GetClosestIntegerSquareRoot(D * b);
#    #k = a*a - D*b*b

#    aaa = Solve(D, a, b)
#    print aaa


def SolveProblem():
    print __name__

    maxX = 0
    maxD = 0

    solutionsDic = dict()
    dArr = range(1, 1000 + 1)
    
    for D in dArr:
        if (IntSqrt(D) != -1):
            continue

        b = 1
        a = GetClosestIntegerSquareRoot(D * b);

        solutionsDic[D] = Solve(D, a, b)

        print D, solutionsDic[D]

    for D in dArr:
        if (solutionsDic.has_key(D)): 
            (x,y) = solutionsDic[D]
            print str(D) + ": " + str(x) + "," + str(y)
            if (x > maxX):
                maxX = x
                maxD = D
                print "NEW MAX: x:" + str(x) + " D:" + str(D)  

    return maxD




#1: None
#2: (3, 2)
#3: (2, 1)
#4: None
#5: (9, 4)
#6: (5, 2)
#7: (8, 3)
#8: (3, 1)
#9: None
#10: (19, 6)
#11: (10, 3)
#12: (7, 2)
#13: (649, 180)