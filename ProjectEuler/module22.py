def GetInput(path):
    inputStr = file(path).read()
    names = inputStr.split(",")
    for i in range(0,len(names)):
        name = names[i]
        names[i] = name[1:-1]
    return names

def GetNameValue(name):
    sum = 0
    for ch in name:
        ch = ch.lower()
        sum += ord(ch) - (ord('a') - 1)
    return sum

def GetNameScore(i, name):
    nameVal = GetNameValue(name)
    score = nameVal * i
    return score



def SolveEx22():
    names = GetInput("input/input22.txt")

    names.sort(key=str.lower)

    sum = 0
    for i in range(0,len(names)):
        name = names[i]
        score = GetNameScore(i+1, name)
        sum += score

    print sum