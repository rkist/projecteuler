from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *



#def HasJustOneSquareTriangle(perimeter):
#    counter = 0
#    limit = perimeter / 2
#    for a in range(1, limit):
#        for b in range(a, (perimeter - a)):
#            c = perimeter - (a + b)

#            if (IsSquareTriangle(a, b, c)):
#                counter += 1

#            if (counter > 1):
#                return False
                
#    return counter == 1


def SolveProblem():
    print __name__

    print GetSquareTrianglesWithPerimeter(240)

    for m in range(100):
        for n in range(100):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            perimeter = 2 * (m * (m + n))
            print perimeter



    counter = 0

    #for perimeter in range(12, 1500000 + 1):
    #    #triangles = GetSquareTrianglesWithPerimeter(perimeter)
    #    #numberOfTriangles = len(triangles)

    #    if (HasJustOneSquareTriangle(perimeter)):
    #        counter += 1

    #    if (perimeter % 1000 == 0):
    #        print perimeter, counter
   

    return counter


#1000 112
#2000 222
#3000 332
#4000 446
#5000 556
    
   

