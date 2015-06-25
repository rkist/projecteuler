
def GetProductOfNumbersInArray(arr):
    mult = 1
    for numStr in arr:
        num = int (numStr)
        mult *= num
    return mult

def GetAdjacentProductsofNumbersInArray(arr, numOfAdjNum):
    if (len(arr) < numOfAdjNum):
        return GetProductOfNumbersInArray(arr)
    start = 0
    end = numOfAdjNum
    results = []

    while end <= len(arr):
        num = GetProductOfNumbersInArray(arr[start:end])
        results.append(num)
        start += 1
        end += 1
    return results


def GetBiggestNumberInArray(arr):
    max = 0
    for num in arr:
        if num > max:
            max = num
    return max



