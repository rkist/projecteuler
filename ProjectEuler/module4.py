


def IsPalindrome(number):
    numStr = str(number)
    for index in range(0,len(numStr)/2):
        if numStr[index] != numStr[-(index+1)]:
            return False
    return True