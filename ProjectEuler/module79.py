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

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]        

    return memoized_func



arr = [89, 271, 325, 328, 890, 1025, 1055, 1081, 1129, 1169]
def sq_cub_rev_prime(n):
    global arr
    i = arr[-1] + 1
       
    primeTest = (IsPrime)       

    while(len(arr) < n):        
        if (TestSquare(i, primeTest) and TestCube(i, primeTest)):
            arr.append(i)
        i+=1
    return arr[n-1] 


def TestSquare(n, primeTest):    
    n2 = n*n
    n2r = Reverse(n2)

    return primeTest(n2r)
        

def TestCube(n, primeTest):         
    n3 = n*n*n
    n3r = Reverse(n3)
       
    return primeTest(n3r)


def SolveProblem():
    print __name__
    global arr

    #stations = [37,61,92,36]
    #path = four_pass(stations)

    #print(len(path))
    #print([37,27,26,25,24,23,22,21,31,41,51,61,71,81,91,92,93,94,95,96,86,76,66,56,46,36])             
    #print(path)


    sq_cub_rev_prime(50)
    sq_cub_rev_prime(90)
    aaa = sq_cub_rev_prime(250)


    print arr
    


    return aaa


     