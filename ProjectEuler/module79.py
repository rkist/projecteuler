from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def GenPassword(passwdsEntries):
    passwords = []
    
    GenPasswordRecursion(1, passwdsEntries, passwdsEntries[0], passwords)

    return passwords


def GenPasswordRecursion(index, passwordsEntries, password, possiblePasswordsList):
    passwordsEntriesLen = len(passwordsEntries)
    if (index == passwordsEntriesLen):
        possiblePasswordsList.append(password)
        return

    currentEntry = passwordsEntries[index]
    newIndex = index + 1
    
    
    if (currentEntry[0] not in password):
        stopIndex = FindList(currentEntry[1], password)
        if (stopIndex < 0):
            stopIndex = len(password)

        for i in range(0,stopIndex):
            newPassword = password[:i] + [currentEntry[0]] + password[i:]
            GenPasswordRecursion(newIndex, passwordsEntries, newPassword, possiblePasswordsList)

    if (currentEntry[1] not in password):
        startIndex = FindList(currentEntry[0], password) 
        if (startIndex < 0):
            stopIndex = 0

        for i in range(startIndex, len(password)):
            newPassword = password[:i] + [currentEntry[0]] + password[i:]
            GenPasswordRecursion(newIndex, passwordsEntries, newPassword, possiblePasswordsList)

    #exists        




def SolveProblem():
    print __name__

    pwds = ReadCardsFile("input/input79.txt")
    passwdsEntries = []
    for pwd in pwds:
        passwdsEntries.append([pwd[0], pwd[1]])
        passwdsEntries.append([pwd[1], pwd[2]])
        passwdsEntries.append([pwd[0], pwd[2]])
       
    passwd = GenPassword(passwdsEntries)
    print passwd

    return -1