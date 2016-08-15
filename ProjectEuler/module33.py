from module30 import GetNumArray
from module32 import ConvertArrayOfIntToInt

def WeirdSimplification(nominator, denominator):
    nomArr = GetNumArray(nominator)
    denArr = GetNumArray(denominator)

    repeatedNum = -1

    for nom in nomArr:
        for den in denArr:
            if (nom == den):
                repeatedNum = nom

    if (repeatedNum > 0 and nomArr.index(repeatedNum) != denArr.index(repeatedNum)):
        nomArr.remove(repeatedNum)
        denArr.remove(repeatedNum)

    simplNom = ConvertArrayOfIntToInt(nomArr)
    simplDen = ConvertArrayOfIntToInt(denArr)

    return simplNom, simplDen








def SolveProblem():
    for nominator in range(10,100):
        for denominator in range(nominator,100):
            simplNom, simplDen = WeirdSimplification(nominator, denominator)

            if (simplDen == 0):
                continue
            if (nominator == simplNom):
                continue
            if (denominator == simplDen):
                continue

            if (float(nominator)/float(denominator) == float(simplNom)/float(simplDen)):
                print str(nominator) + "/" + str(denominator) + " == " + str(simplNom) + "/" + str(simplDen)
