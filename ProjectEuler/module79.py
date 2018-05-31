from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *
from GraphHelpers import *
from Memoize import *


def GenPassword(passwdsEntries):
    passwords = []

    GenPasswordRecursion(0, passwdsEntries, passwords)

    return passwords


def GenPasswordRecursion(index, passwordsEntries, passwords):
    passwordsEntriesLen = len(passwordsEntries)
    if (index == passwordsEntriesLen):
        return

    currentEntry = passwordsEntries[index]
    if (len(passwords) == 0):
        passwords.append([currentEntry[0], currentEntry[1]])   
        
    newIndex = index + 1
    
    for password in passwords:
        GenPasswordRecursion(i, passwordsEntries, passwords)
        




def SolveProblem():
    print __name__

    pwds = ReadCardsFile("input/input79.txt")
    passwdsEntries = []
    for pwd in pwds:
        passwdsEntries.append((pwd[0], pwd[1]))
        passwdsEntries.append((pwd[1], pwd[2]))
        passwdsEntries.append((pwd[0], pwd[2]))
       
    passwd = GenPassword(passwdsEntries)
    print passwd

    return -1