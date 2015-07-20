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
    return divs

def GetDivisorsOfTriangleNumberFaster(position):
    nums = [position,position+1]

    if position % 2 == 0:
        nums[0] = position/2
    else:
        nums[1] = (position+1)/2

    divs1 = module3.GetAllDivisorsArray(nums[0])
    divs2 = module3.GetAllDivisorsArray(nums[1])

    divisors = Set(divs1) | Set(divs2)

    for d1 in divs1:
        for d2 in divs2:
            divisors.add(d1*d2)

    #print divisors
    return divisors