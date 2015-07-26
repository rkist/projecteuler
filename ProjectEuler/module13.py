from bignumber import *

def GetInput(path):
    numArr = []
    inputStr = file(path).read()
    lines = inputStr.splitlines()
    for line in lines:
        bn = BigNumber(line)
        numArr.append(bn)
    return numArr






        