from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *


from joblib import Parallel, delayed
import multiprocessing


def SatisfyWeirdProperty(num1, num2):
    pent1 = PentagonNumber(num1)
    pent2 = PentagonNumber(num2)
    diff = abs(pent2-pent1)
    sum = pent1 + pent2

    satsDiff = False
    satsSum = False
    i = 1
    while (True):
        pn = PentagonNumber(i)
        if (pn == diff):
            satsDiff = True
        if (pn == sum):
            satsSum = True
        if (pn > diff and pn > sum):
            break
        i += 1
    return satsDiff and satsSum

def ParallelProcess(j):
    for k in range(j,200 + 2*j):
        #print str(j) + "," + str(k)
        if (SatisfyWeirdProperty(j, k)):
            pj = PentagonNumber(j)
            pk = PentagonNumber(k)
            return abs(pk - pj)
    return 0


def SolveProblem():

    num_cores = multiprocessing.cpu_count()   
    results = Parallel(n_jobs=num_cores)(delayed(ParallelProcess)(j) for j in range(1,2000))

    for res in results:
        if (res != 0):
            return res

    return -1



    #pj = 0
    #pk = 0

    #for j in range(1, 2000):
    #    for k in range(j, 2000):
    #        #print str(j) + "," + str(k)
    #        if (SatisfyWeirdProperty(j, k)):
    #            pj = PentagonNumber(j)
    #            pk = PentagonNumber(k)
    #            return abs(pk - pj)
    #return 0