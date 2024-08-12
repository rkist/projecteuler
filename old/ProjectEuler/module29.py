import math

def SolveProblem():

  numbersSet = set()
  numbersList = []

  for a in range(2,101):
    for b in range(2,101):
      res = a**b
      numbersSet.add(res)
      numbersList.append(res)


  #print sorted(numbersSet)
  #print sorted(numbersList)

  print len(sorted(numbersSet))
  #print len(sorted(numbersList))