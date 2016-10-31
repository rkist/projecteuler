from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *



def TestProperty(num0, num1):
    num0Arr = ConvertIntToIntArray(num0)
    num1Arr = ConvertIntToIntArray(num1)

    return (num0Arr[-2] == num1Arr[0] and num0Arr[-1] == num1Arr[1])



def SolveProblem():
   
    print "."  

    triangleNumbers = []
    for i in range(500):
        n = TriangleNumber(i)
        nArr = ConvertIntToIntArray(n)
        if (len(nArr) == 4):
            triangleNumbers.append(n)


    print "."   

    squareNumbers = []
    for i in range(500):
        n = SquareNumber(i)
        nArr = ConvertIntToIntArray(n)
        if (len(nArr) == 4):
            squareNumbers.append(n)

    print "."  

    pentagonalNumbers = []
    for i in range(500):
        n = PentagonalNumber(i)
        nArr = ConvertIntToIntArray(n)
        if (len(nArr) == 4):
            pentagonalNumbers.append(n)

    print "."  

    hexagonalNumbers = []
    for i in range(500):
        n = HexagonalNumber(i)
        nArr = ConvertIntToIntArray(n)
        if (len(nArr) == 4):
            hexagonalNumbers.append(n)


    print "."  

    heptagonalNumbers = []
    for i in range(500):
        n = HeptagonalNumber(i)
        nArr = ConvertIntToIntArray(n)
        if (len(nArr) == 4):
            heptagonalNumbers.append(n)

    print "."  

    octogonalNumbers = []
    for i in range(500):
        n = OctagonalNumber(i)
        nArr = ConvertIntToIntArray(n)
        if (len(nArr) == 4):
            octogonalNumbers.append(n)

    print "."  

    nodes = triangleNumbers + squareNumbers + pentagonalNumbers + hexagonalNumbers + heptagonalNumbers + octogonalNumbers

    vertices = []

    for n in nodes:
        for m in nodes:
            if (TestProperty(n, m)):
                vertices.append((n,m))

    print len(nodes)
    print len(vertices)

    graph = CreateDirectedGraph(nodes, vertices)

    cicles = DetectCicles(graph)

    for cicle in cicles:
        print cicle

    return -1