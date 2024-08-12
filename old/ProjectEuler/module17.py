
import sys
sys.path.insert(0, 'D:\\kist\Documents\\GitHub\\projecteuler\\ProjectEuler\\pynum2word')

from num2word_EN import to_card

def SumChars(words):
    sum = 0
    for char in words:
        if (not(char == ' ' or char == '-' or char == ',')):
            sum += 1
    return sum


def SumRange():
    sum = 0
    for num in range(1,1001):
        words = to_card(num)
        numChars = SumChars(words)
        print words + " [" + str(numChars) + "] "
    
        sum += numChars
    return sum


