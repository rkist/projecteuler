


def IsPalindrome(number):
    numStr = str(number)
    for index in range(0,len(numStr)/2):
        if numStr[index] != numStr[-(index+1)]:
            return False
    return True

def GetMaxPalindromeFromMultiplOfNumInRange(start,end):
    maxPal = 0
    for i0 in range(start,end):
        for i1 in range(start,end):
            num = i0*i1
            isPal = IsPalindrome(num)
            if isPal:
                if num > maxPal:
                    maxPal = num
                    #print maxPal
    return maxPal