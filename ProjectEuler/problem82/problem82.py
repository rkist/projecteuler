
def readMatrixFromFile(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append([int(x) for x in line.split(',')])
    return matrix


def minPathSum(matrix) -> int:
    n = len(matrix)
    m = len(matrix[0])
    auxMatrix = [[-1 for _ in range(m)] for _ in range(n)]
    dp = minPathSumRecursive(matrix, auxMatrix, n - 1, m - 1)
    return dp


def minPathSumRecursive(matrix, aux, i, j) -> int:
    if aux[i][j] == -1:
        if i == 0 and j == 0:
            aux[i][j] = matrix[i][j]
        elif i == 0:
            aux[i][j] = matrix[i][j] + minPathSumRecursive(matrix, aux, i, j - 1)
        elif j == 0:
            aux[i][j] = matrix[i][j] + minPathSumRecursive(matrix, aux, i - 1, j)
        else:
            aux[i][j] = matrix[i][j] + min(minPathSumRecursive(matrix, aux, i - 1, j), minPathSumRecursive(matrix, aux, i, j - 1))
    return aux[i][j]


def SolveProblem():
    print(__name__)

    testMatrix03 = [[131, 673, 234, 103, 18],
                [201, 96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524, 37, 331]]
    
    answer03 = 994

    testMatrix02 = [[1, 1, 3],
                    [2, 1, 3],
                    [3, 1, 1]]
    answer02 = 5

    testMatrix01 = [[1, 1],
                    [2, 1]]
    answer01 = 3

    probemMatrix = readMatrixFromFile("problem82/matrix.txt")


    restult01 = minPathSum(testMatrix01)
    restult02 = minPathSum(testMatrix02)
    restult03 = minPathSum(testMatrix03)

    print("Result01: " + str(restult01))
    print("Answer01: " + str(answer01))

    print("Result02: " + str(restult02))
    print("Answer02: " + str(answer02))

    print("Result03: " + str(restult03))
    print("Answer03: " + str(answer03))

    result = minPathSum(probemMatrix)

    return result



if __name__ == "__main__":
    restult = SolveProblem()
    print("Result: " + str(restult))