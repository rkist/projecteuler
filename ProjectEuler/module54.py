from ArrayHelpers import *
from NumericalHelpers import *
from FileHelpers import *
from Parallel import *
from PrimesCache import *

class Card:
    def __init__(self, value, suit):
        self.Value = value
        self.Suit = suit

    def __str__(self):
        return str(self.Value) + str(self.Suit)   

    def __eq__(self, other):
        return self.Value == other.Value and self.Suit == other.Suit

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.Value > other.Value

    def __ge__(self, other):
        return self.Value >= other.Value

    def __lt__(self, other):
        return self.Value < other.Value

    def __le__(self, other):
        return self.Value <= other.Value

    @classmethod
    def Parse(cls, s):    
        val = s[:-1]
        value = 0
        if (val == 'T'):
            value = 10
        elif (val == 'J'):
            value = 11
        elif (val == 'Q'):
            value = 12
        elif (val == 'K'):
            value = 13
        elif (val == 'A'):
            value = 14
        else:
            value = int(val)
        suite = s[-1]
        return cls(value, suite)


class Ranks:
    HighCard = 0 #Highest value card.
    OnePair = 1 #Two cards of the same value.
    TwoPairs = 2 #Two different pairs.
    ThreeOfKind = 3 #Three cards of the same value.
    Straight = 4 #All cards are consecutive values.
    Flush = 5 #All cards of the same suit.
    FullHouse = 6 #Three of a kind and a pair.
    FourOfKind = 7 #Four cards of the same value.
    StraightFlush = 8 #All cards are consecutive values of same suit.
    RoyalFlush = 9 #Ten, Jack, Queen, King, Ace, in same suit.


class Hand:
    def __init__(self, cards):
        self.Cards = cards
        self.Cards.sort()

    def __str__(self):
        s = ""
        for c in self.Cards:
             s += str(c) + " "
        return s

    @classmethod
    def Parse(cls, s):    
        cardsStr = s.split(" ")
        cards = []
        for cStr in cardsStr:
            c = Card.Parse(cStr)
            cards.append(c)
        return cls(cards)

    def _sameSuit(self, cards):        
        for i in range(len(cards)-1):
            if (cards[i].Suit != cards[i+1].Suit):
                return False
        return True

    def _rankRoyalFlush(self):
        if (not self._sameSuit(self.Cards)):
            return False
        for i in range(len(self.Cards)):
            card = self.Cards[i]
            if (i + 10 != card.Value):
                return False
        return True

    def _rankStraightFlush(self):
        if (not self._sameSuit(self.Cards)):
            return False
        for i in range(len(self.Cards)-1):
            if (self.Cards[i].Value + 1 != self.Cards[i+1].Value):
                return False
        return True

    def _rankFourOfKind(self):
        return False


    def Rank(self): #todo
        if (self._rankRoyalFlush()):
            return Ranks.RoyalFlush
        if (self._rankStraightFlush()):
            return Ranks.StraightFlush
        if (self._rankFourOfKind()):
            return Ranks.FourOfKind
        else:
            return Ranks.HighCard
        






def SolveProblem():
    print "."   

    h1 = Hand.Parse("5H 5C 6S 7S KD")
    h2 = Hand.Parse("2C 3S 8S 8D TD")

    print h1
    print h2

    print h1.Rank()
    print h2.Rank()

    ht = Hand.Parse("TC JC KC AC QC") #9
    print ht.Rank()

    ht = Hand.Parse("5C 6C 7C 9C 8C") #8
    print ht.Rank()

    ht = Hand.Parse("6C 5C 7C 9C 8C") #8
    print ht.Rank()

    ht = Hand.Parse("6C 5C 7S 9C 8C") #0
    print ht.Rank()

    return -1