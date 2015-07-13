import module3
import module12

index = 1
trinum = 0
while True:
    trinum = module12.GetTriangleNumber(trinum, index-1, index)
    divs = module3.GetAllDivisors(trinum)
    divlen = len(divs)
    print trinum, divlen
    index+=1

    if divlen > 500:
        break;




