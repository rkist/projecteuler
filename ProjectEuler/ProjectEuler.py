import module3
import module12

index = 1
trinum = 0
while True:
    divs = module12.GetDivisorsOfTriangleNumberFaster(index)
    divs = module12.GetDivisorsOfTriangleNumber(index)
    
    divlen = len(divs)

    trinum = module12.GetTriangleNumberByFormula(index)
    print trinum, divlen
    index+=1

    if divlen > 5:
        break;




