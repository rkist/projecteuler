import time
from module75 import SolveProblem


if __name__ == "__main__":    
    start = time.time()
    result = SolveProblem()
    finish = time.time()


    print("Time:   %ss" % (finish - start))
    print("Result: " + str(result))

    







