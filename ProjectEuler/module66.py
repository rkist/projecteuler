
from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *


#def SolveForD(D):
#    if (IntSqrt(D) == -1): # not square number
#        x = 2
#        while True:
#            ans = x
#            y = SmallerIntSqrt((x*x - 1)/D)
#            while (ans > 1):
#                ans = x*x - D*y*y
#                if (ans == 1):
#                    return (x,y)
#                y+=1
#            x+=1
#    else:
#        return (-1,-1)


#def SolveForD(D):
#    if (IntSqrt(D) == -1): # not square number
#        x = 2
#        while True:
#            ans = x
#            y = SmallerIntSqrt((x*x - 1)/D)
#            ans = x*x - D*y*y
#            if (ans == 1):
#                return (x,y)
#            x+=1
#    else:
#        return (-1,-1)


def SolveForD(D):
    print str(D) + " start"
    if (IntSqrt(D) == -1): # not square number
        y = 1
        while True:
            ans = y
            x = SmallerIntSqrt(1 + D*y*y)
            ans = x*x - D*y*y
            if (ans == 1):
                print str(D) + ": " + str(x) + "," + str(y)
                return (x,y)
            y+=1
    else:
        return (-1,-1)




def SolveProblem():
    print __name__

    maxX = 0
    maxD = 0
    dArr = range(1,1000)
    solArr = ParalelProcess(SolveForD, dArr)
    D = 1
    for (x,y) in solArr:           
        if (x > maxX):
            maxX = x
            maxD = D
            print "NEW MAX: x:" + str(x) + " D:" + str(D)      
        D += 1

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