from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *

matrix_size = 10
   
def from_index_to_matrix(index):
    return int(index / 10), int(index % 10)
    
def from_matrix_to_index(matrixPos):
    return matrixPos[0] * 10 + matrixPos[1]  
    
def calc_vector(lastPos, destiny):
    xDiff = destiny[0] - lastPos[0]
    yDiff = destiny[1] - lastPos[1]
    if (xDiff == 0):
        x = 0
    else:
        x = int((xDiff) / abs(xDiff))
        
    if (yDiff == 0):
        y = 0
    else:
        y = int((yDiff) / abs(yDiff))   
    
    return (x, y)

def four_pass(stations):
    print(stations)
#     print(from_matrix_to_index(from_index_to_matrix(56)))
    
#     lastPos = (6,1)
#     destiny = (1,1)
#     print(calc_vector(lastPos, destiny))
    
    stationsPos = [from_index_to_matrix(i) for i in stations]
    posPaths = []    
    for i, pos in enumerate(stationsPos):
        remainingPos = set(stationsPos[i+1:])
        print(posPaths, pos, remainingPos)
        posPaths = calcPath(posPaths, pos, remainingPos, 0)   

        
    path = [from_matrix_to_index(p) for p in posPaths]   
    print(path)
    
    return path
         
    
    
def calcPath(path, destiny, remainingStations, stackSize):
    if (path == None or stackSize > 15):
        return None

    pathSize = len(path)
    if (pathSize == 0):
        return [destiny]

    lastPosition = path[pathSize-1]

    if (lastPosition == destiny):
        return path

    if (lastPosition in remainingStations):
        return None
        
    vector = calc_vector(lastPosition, destiny)    
        
    position0 = (lastPosition[0] + vector[0], lastPosition[1])
    position1 = (lastPosition[0], lastPosition[1] + vector[1])
    position2 = (lastPosition[0] - vector[0], lastPosition[1])
    position3 = (lastPosition[0], lastPosition[1] - vector[1])
    
    positions = [position1, position0, position2, position3]    
    
    paths = []

    for position in positions:
        if (position[0] >= 0 and position[0] < matrix_size and position[1] >= 0 and  position[1] < matrix_size):
            if (position not in path):  
                p = calcPath(path[:] + [position], destiny, remainingStations, stackSize + 1)
                if (p != None):
                    paths.append(p)

    if (len(paths) == 0):
        return None

    sortedPaths = sorted(paths, key = lambda x: len(x))
            
    return sortedPaths[0]


def SolveProblem():
    print __name__


    return 0

