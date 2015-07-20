import module13


inputs = module13.GetInput("input/input13.txt")

#print len(inputs)
#print inputs[0]

bn1 = module13.BigNumber("193")
bn2 = module13.BigNumber("12")

bn3 = bn1 + bn2

print bn3

bn1 += bn2

print bn1






