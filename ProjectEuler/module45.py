from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *


from joblib import Parallel, delayed
import multiprocessing

def ParalelProcess(i):
    if (IsInArray(pentagArr, x) and IsInArray(hexagArr, x)):
        return x
    return 0


def SolveProblem():

    triangleArr = []
    for i in range(286, 100000):
        x = TriangleNumber(i)
        triangleArr.append(x)

    pentagArr = []
    for j in range(166, 100000):
        y = PentagonNumber(j)
        pentagArr.append(y)

    hexagArr = []
    for k in range(144, 100000):
        z = HexagonNumber(k)
        hexagArr.append(z)

    #num_cores = multiprocessing.cpu_count()   
    #results = Parallel(n_jobs=num_cores)(delayed(ParalelProcess)(i) for i in triangleArr)

    #for res in results:
    #    if (res != 0):
    #        return res

    #return -1



    for x in triangleArr:
        if (IsInArray(pentagArr, x) and IsInArray(hexagArr, x)):
            return x
    return 0