from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *

def HasWeirdProperty(arr):
    if (len(arr) != 10):
        return False

    d234 = ConvertIntArrayToInt([arr[1], arr[2], arr[3]])
    d345 = ConvertIntArrayToInt([arr[2], arr[3], arr[4]])
    d456 = ConvertIntArrayToInt([arr[3], arr[4], arr[5]])
    d567 = ConvertIntArrayToInt([arr[4], arr[5], arr[6]])
    d678 = ConvertIntArrayToInt([arr[5], arr[6], arr[7]])
    d789 = ConvertIntArrayToInt([arr[6], arr[7], arr[8]])
    d8910 = ConvertIntArrayToInt([arr[7], arr[8], arr[9]])

    if (d234 % 2 != 0):
        return False

    if (d345 % 3 != 0):
        return False

    if (d456 % 5 != 0):
        return False

    if (d567 % 7 != 0):
        return False

    if (d678 % 11 != 0):
        return False

    if (d789 % 13 != 0):
        return False

    if (d8910 % 17 != 0):
        return False

    return True


def SolveProblem():
    arr = ConvertIntToIntArray(1234567890)
    perms = Permute(arr)

    sum = 0
    for perm in perms:
        if (HasWeirdProperty(perm)):
            n = ConvertIntArrayToInt(perm)
            sum += n
            print n

    return sum