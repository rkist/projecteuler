
def readMatrixFromFile(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append([int(x) for x in line.split(',')])
    return matrix


def minPathSum(matrix) -> int:
    n = len(matrix)
    m = len(matrix[0])
    dps = [9999999999 for _ in range(n)]
    for i in range(n):
        auxMatrix = [[-1 for _ in range(m)] for _ in range(n)]
        visited = set()
        dps[i] = minPathSumRecursive(matrix, auxMatrix, i, m - 1, n, m, visited)
        print(auxMatrix)
    printMatrix(len(dps), dps)
    return min(dps)

def toupleSchema(i,j):
    n = 1000*i + j
    return n

def reverseToupleSchema(n):
    i, j = int(n/1000), (n%1000)
    return (i, j) 

def printvisited(visited):
    s = ""
    for n in visited:
        i, j = reverseToupleSchema(n)
        s += f"({i},{j}), "
    print(s)

def printMatrix(m):
    ii = len(m)
    jj = len(m[0])

    for i in range(ii):
        s = ""
        for j in range(jj):
            s += f"{m[i][j]} "
        print(s)


def minPathSumRecursive(matrix, aux, i, j, leni, lenj, visited) -> int:
    print(i,j)
    printvisited(visited)

    if toupleSchema(i, j) in visited:
        return 999999999999999

    if i < 0 or j < 0 or i >= leni or j >= lenj:
        return 999999999999999
    
    visited.add(toupleSchema(i, j))
    new_visited = visited.copy()
    
    if aux[i][j] == -1:
        if j == 0:
            aux[i][j] = matrix[i][j]
        else:
            up = minPathSumRecursive(matrix, aux, i - 1, j, leni, lenj, new_visited)
            down = minPathSumRecursive(matrix, aux, i + 1, j, leni, lenj, new_visited)
            left = minPathSumRecursive(matrix, aux, i, j - 1, leni, lenj, new_visited)
            
            aux[i][j] = matrix[i][j] + min(up, left, down)
    return aux[i][j]


def SolveProblem():
    print(__name__)

    testMatrix04 = [[131, 1, 234, 103, 18],
                [200, 1, 1, 1, 150],
                [630, 1, 746, 1, 1],
                [1, 1, 497, 121, 956],
                [805, 732, 524, 37, 331]]
    
    answer04 = 8

    testMatrix03 = [[131, 673, 234, 103, 18],
                [201, 96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524, 37, 331]]
    
    answer03 = 994

    testMatrix02 = [[9, 1, 6],
                    [1, 1, 3],
                    [8, 1, 1]]
    answer02 = 4

    testMatrix01 = [[1, 1],
                    [5, 1]]
    answer01 = 2

    probemMatrix = readMatrixFromFile("problem82/matrix.txt")


    restult01 = minPathSum(testMatrix01)
    restult02 = minPathSum(testMatrix02)
    # restult03 = minPathSum(testMatrix03)
    # restult04 = minPathSum(testMatrix04)

    print("Result01: " + str(restult01))
    print("Answer01: " + str(answer01))

    print("Result02: " + str(restult02))
    print("Answer02: " + str(answer02))

    # print("Result03: " + str(restult03))
    # print("Answer03: " + str(answer03))

    # print("Result04: " + str(restult04))
    # print("Answer04: " + str(answer04))

    # result = minPathSum(probemMatrix)
    # return result

    return -1


if __name__ == "__main__":
    restult = SolveProblem()
    print("Result: " + str(restult))