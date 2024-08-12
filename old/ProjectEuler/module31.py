import math

#possible coins: 1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).
#AllPossibleCoins = [200, 100, 50, 20, 10, 5, 2, 1]
AllPossibleCoins = [1, 2, 5, 10, 20, 50, 100, 200]

CoinsCombinationsArray = []

def CalculateAmount(coins):
  amount = 0
  for coin in coins:
    amount += coin   

  return amount

def CombinateCoins(remainingCoins, remainingAmount):
  chosenCoins = []
  return CombinateCoinsRecursion(chosenCoins, remainingCoins, remainingAmount)



def CombinateCoinsRecursion(chosenCoins, remainingCoins, remainingAmount):
  if (remainingAmount == 0):
    CoinsCombinationsArray.append(chosenCoins)
    return
  if (remainingAmount < 0):
    return
  if (len(remainingCoins) == 0):
    return

  currentCoin = remainingCoins[-1]
  newRemainingCoins = remainingCoins[:-1]
  amountOfCurrentCoin = 0
  while (currentCoin * amountOfCurrentCoin <= remainingAmount):
    newChosenCoins = chosenCoins + [currentCoin] * amountOfCurrentCoin
    newRemainingAmount = remainingAmount - currentCoin * amountOfCurrentCoin    
    CombinateCoinsRecursion(newChosenCoins, newRemainingCoins, newRemainingAmount)
    amountOfCurrentCoin += 1
  


def SolveProblem():
  remainingAmount = 200
  possibleCoins = AllPossibleCoins[:]

  CombinateCoins(possibleCoins, remainingAmount)

  print CoinsCombinationsArray
  print len(CoinsCombinationsArray)