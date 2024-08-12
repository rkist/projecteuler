from ArrayHelpers import *
from NumericalHelpers import *

def FindRightAngleTriangleWithPerimeter(perimeter):
    triangles = set()
    for a in range(1, perimeter/2):
        for b in range(a, perimeter/2):
            c1 = sqrt(a*a + b*b)
            c2 = perimeter - (a + b)
            if (c1 == c2):
                triangles.add((a, b, c2))
    return triangles



def SolveProblem():

    maxTriagles = 0
    perimeterMaximizesTriangles = 0
    for per in range(3, 1001):
        triangles = FindRightAngleTriangleWithPerimeter(per)
        lenTriang = len(triangles)
        if (lenTriang > maxTriagles):
            maxTriagles = lenTriang
            perimeterMaximizesTriangles = per
        print per


    return perimeterMaximizesTriangles