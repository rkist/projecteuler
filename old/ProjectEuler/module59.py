from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *



def FormatMsg(msg):
    s = ''
    for n in msg:
        c = str(unichr(n))
        s += c
    return s

def CheckMsg(msg):
    lmsg = msg.lower()

    okCounter = 0

    if 'the ' in lmsg:
        okCounter += 1
    if ' of ' in lmsg:
        okCounter += 1
    if ' is ' in lmsg:
        okCounter += 1

    return okCounter > 2



def SolveProblem():
    print "."   
    input = ReadNumbers('input/input59.txt')
    inputLen = len(input)

    passInp = []
    for ch in 'abcdefghijklmnopqrstuvxyz':
        passInp.append(ord(ch))

    pwLen = 3
    pwCandidates = Permute(passInp, pwLen)
    
    for pwCandidate in pwCandidates:
        i = 0

        translationCandidate = []

        while (i < inputLen):
            j = i % pwLen
            ch = input[i] ^ pwCandidate[j]

            translationCandidate.append(ch)

            i += 1

        msgCandidate = FormatMsg(translationCandidate)
        if (CheckMsg(msgCandidate)):
            print  msgCandidate
            print pwCandidate

            sum = SumArray(translationCandidate)
            return sum


    return -1