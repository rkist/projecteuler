
#[linha][coluna]
def GetInput(path):
    numArr = []
    inputStr = file(path).read()
    lines = inputStr.splitlines()
    for line in lines:
        numsStr = line.split(" ")
        tempArr = []
        for numStr in numsStr:
            tempArr.append(int(numStr))
        numArr.append(tempArr)
    return numArr


def GetMaxMultInMatrix(matrix, arraysize):
    lenX = len(matrix)
    lenY = len(matrix[0])

    maxMult = 0
    #vertical
    for x in xrange(0,lenX-(arraysize-1)):
        for y in xrange(0,lenY):
            mult = 1
            for i in xrange(0,arraysize):
                mult *= matrix[x+i][y]
            if mult > maxMult:
                maxMult = mult


    #horizontal
    for x in xrange(0,lenX):
        for y in xrange(0,lenY-(arraysize-1)):
            mult = 1
            for i in xrange(0,arraysize):
                mult *= matrix[x][y+i]
            if mult > maxMult:
                maxMult = mult

    #diagonal
    for x in xrange(0,lenX-(arraysize-1)):
        for y in xrange(0,lenY-(arraysize-1)):
            mult = 1
            for i in xrange(0,arraysize):
                mult *= matrix[x+i][y+i]
            if mult > maxMult:
                maxMult = mult

    #rev diagonal
    for x in xrange(arraysize-1,lenX):
        for y in xrange(0,lenY-(arraysize-1)):
            mult = 1
            for i in xrange(0,arraysize):
                mult *= matrix[x-i][y+i]
            if mult > maxMult:
                maxMult = mult

    return maxMult




