from module07 import IsPrime

class Formula:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def GetResult(self, n):
        result = n*n + self.a * n + self.b
        return result

def MaxConsecutiveN(formula):
    n = 0
    while(True):
        res = formula.GetResult(n)
        if (not IsPrime(res)):
            return n
        n += 1
    return -1





def SolveProblem():
    formula = Formula(1,41)
    n = MaxConsecutiveN(formula)
    print n

    formula = Formula(-79,1601)
    n = MaxConsecutiveN(formula)
    print n

    maxN = 0
    aForMaxN = 0
    bForMaxN = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            formula = Formula(a,b)
            n = MaxConsecutiveN(formula)

            if (n > maxN):
                maxN = n
                aForMaxN = a
                bForMaxN = b

                print str(a) + "*" + str(b)+ " " + str(n)
    print str(aForMaxN*bForMaxN)
                





