
import module7


priArr = module7.GetPrimeNumbersUpTo(2000000)

#print priArr
sum = 0
for num in priArr:
    sum += num
print sum
