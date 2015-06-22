import math

def GetDivisors(value):
    arr = []
    for divisor in range(1,int(math.sqrt(value) + 0.5)):
        if value % divisor == 0:
            arr.append(divisor)

    return arr




def GetPrimeFactors(value):
    primeDivisors = []
    divisors = GetDivisors(value)

    for divisor in divisors:
        divdiv = GetDivisors(divisor)        
        if len(divdiv) == 1:
            primeDivisors.append(divisor)
    return primeDivisors
