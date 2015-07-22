import module13


inputs = module13.GetInput("input/input13.txt")


sum =  module13.BigNumber("0")
for bn in inputs:
    sum += bn


print sum


bn1 = module13.BigNumber("999")
bn2 = module13.BigNumber("1")

bn3 = bn1 + bn2

print bn3

bn1 += bn2

print bn1






