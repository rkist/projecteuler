from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def SolveProblem():
    print __name__

    sizeOfArray = 1500001

    numTrianglesWithPerimeter = [0] * sizeOfArray

    for m in range(1, int(sqrt(sizeOfArray))):
        
        start = (m % 2) + 1
        for n in xrange(start, m, 2):

            if (not AreCoprime(m,n)):
                continue

            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            semiperimeter = (m * (m + n))
            perimeter = a + b + c
            #perimeter = semiperimeter * 2

            k = 1
            paux = perimeter * k

            while (paux < sizeOfArray):                    
                numTrianglesWithPerimeter[paux] += 1
                k += 1
                paux = perimeter * k
                
    counter = 0

    for p in range(sizeOfArray):
        n = numTrianglesWithPerimeter[p]

        #triangles = GetSquareTrianglesWithPerimeter(p)
        #trianglesLen = len(triangles)
        #if (trianglesLen != n):
        #    print p, n, trianglesLen, triangles

        if (n == 1):
            counter += 1

    return counter


#1000 112
#2000 222
#3000 332
#4000 446
#5000 556
    
   

