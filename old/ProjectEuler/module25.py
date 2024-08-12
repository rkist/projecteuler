
fibonacciArray = [1,1,2,3]
def Fibonacci(n): 
    nMinusOne = n-1
    if (nMinusOne < len(fibonacciArray)):
        return fibonacciArray[nMinusOne]

    fibonacciArray.append(Fibonacci(nMinusOne) + Fibonacci(nMinusOne-1))
    return fibonacciArray[nMinusOne]


def SolveProblem():
    n = 1
    while(True):
        f = Fibonacci(n)
        if (len(str(f)) == 1000):
            print n
            return
        n+=1

