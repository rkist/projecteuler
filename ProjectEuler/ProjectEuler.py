import module1
import module2

fibArray = module2.BuildFibonacciSequenceMaximumBased(4000000)

sum1 = module2.GetSumOfNonMultiplesInArray(1,fibArray)
sum2 = module2.GetSumOfNonMultiplesInArray(2,fibArray)

sum3 = module2.GetSumOfMultiplesInArray(1,fibArray)
sum4 = module2.GetSumOfMultiplesInArray(2,fibArray)


print fibArray
print sum1
print sum2
print sum3
print sum4