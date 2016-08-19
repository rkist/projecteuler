def ReadAndCleanTextInput(path):
    inputStr = file(path).read()
    names = inputStr.split(",")
    for i in range(0,len(names)):
        name = names[i]
        names[i] = name[1:-1]
    return names
