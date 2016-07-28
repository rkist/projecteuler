import math

def GetAllDivisorsArray(value):
    arr = []
    for divisor in range(1,value+1):
        if value % divisor == 0:
            arr.append(divisor)
    return arr

def GetDivisorsArrayOpt(value):
    arr = []
    for divisor in range(1,int(math.sqrt(value) + 1)+1):
        if value % divisor == 0:
            arr.append(divisor)

    return arr


def GetPrimeFactorsArray(value):
    primeDivisors = []
    divisors = GetAllDivisorsArray(value)

    for divisor in divisors:
        divdiv = GetAllDivisorsArray(divisor)       
        l = len(divdiv) 
        if l == 2 or l == 1:
            primeDivisors.append(divisor)
    return primeDivisors
