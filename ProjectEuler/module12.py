import module3
from sets import Set

def GetTriangleNumber(position):
    number = 0
    for a in xrange(1,position+1):
        number+=a
    return number

def GetTriangleNumberWithLast(lastNumber, lastPosition, position):
    number = lastNumber
    for a in xrange(lastPosition+1,position+1):
        number+=a
    return number

def GetTriangleNumberByFormula(position):
    tn = (position * (position + 1)) / 2
    return tn

def GetDivisorsOfTriangleNumber(position):
    tn = GetTriangleNumberByFormula(position)
    divs = module3.GetAllDivisorsArray(tn)
    print divs
    return divs

def GetDivisorsOfTriangleNumberFaster(position):
    #nums = [position,position+1]

    #if position % 2 == 0:
    #    nums[0] = position/2
    #else:
    #    nums[1] = (position+1)/2

    
    #prim1 = Set(module3.GetPrimeFactorsArray(nums[0]))
    #prim2 = Set(module3.GetPrimeFactorsArray(nums[1]))

    #primes = prim1 | prim2 | Set(nums)
    

    tn = GetTriangleNumberByFormula(position)
    primes = module3.GetPrimeFactorsArray(tn)
    print primes

    return primes