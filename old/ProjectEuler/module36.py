from ArrayHelpers import *
from NumericalHelpers import *





def SolveProblem():
    sum = 0
    for num in range(0,1000000):
            binArr = ConvertIntToIntArray(num, 2)
            decArr = ConvertIntToIntArray(num, 10)

            if (IsPalindrome(decArr) and IsPalindrome(binArr)):
                print str(decArr) + " == " + str(binArr)
                sum += num
    print sum
