def ReadAndCleanTextInput(path):
    inputStr = file(path).read()
    names = inputStr.split(",")
    for i in range(0,len(names)):
        name = names[i]
        names[i] = name[1:-1]
    return names

def ReadCardsFile(path):
    inputLines = file(path).readlines()
    lines = []
    for line in inputLines:
        lines.append(line[:-1])
    return lines

def ReadNumbers(path):
    inputStr = file(path).read()
    numStrs = inputStr.split(",")
    nums = []
    for numStr in numStrs:
        nums.append(int(numStr))
    return nums
