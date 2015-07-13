import module3

def GetTriangleNumber(position):
    number = 0
    for a in xrange(1,position+1):
        number+=a
    return number

def GetTriangleNumber(lastNumber, lastPosition, position):
    number = lastNumber
    for a in xrange(lastPosition+1,position+1):
        number+=a
    return number

def GetDivisorsOfTriangleNumber(position):
    tn = GetTriangleNumber(position)
    divs = module3.GetAllDivisors(tn)
    return divs