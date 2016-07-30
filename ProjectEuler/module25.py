
fibonacciArray = [1,1,2,3]
def Fibonacci(n): 
    index = n-1
    if (index < len(fibonacciArray)):
        return fibonacciArray[index]

    fibonacciArray.append(Fibonacci(n-1) + Fibonacci(n-2))
    return fibonacciArray[index]


def SolveEx25():
    n = 1
    while(True):
        f = Fibonacci(n)
        if (len(str(f)) == 1000):
            print n
        n+=1

