import math

def GetDivisors(value):
    arr = []
    for divisor in range(2,int(math.sqrt(value) + 0.5)+1):
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
