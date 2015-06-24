import module3

def IsPrime(value):
    divisors = module3.GetDivisors(value)
    if len(divisors) == 0:
        return True
    return False

def GetPrimeNumbersUpTo(value):
    arr = []
    currValue = 2
    while len(arr) < value:
        if IsPrime(currValue):
            arr.append(currValue)
        currValue+=1
    return arr


