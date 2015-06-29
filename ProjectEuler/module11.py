
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




