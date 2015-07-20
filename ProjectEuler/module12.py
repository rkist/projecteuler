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

    

    print nums
    
    div1 = Set(module3.GetAllDivisorsArray(nums[0]))
    div2 = Set(module3.GetAllDivisorsArray(nums[1]))

    divs = div1 | div2 | Set([GetTriangleNumberByFormula(position)])
    print divs
    return divs