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
        return (not (self == other))

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

    def __eq__(self, other):
        return (self.Cards == other.Cards)            

    def __ne__(self, other):
        return (not (self == other))

    def __gt__(self, other):
        selfRank = self.Rank()
        otherRank = other.Rank()
        if (selfRank > otherRank):
            return True
        elif (selfRank == otherRank):
            if (selfRank == Ranks.RoyalFlush):
                print "2 RoyalFlush???"
            elif (selfRank == Ranks.StraightFlush):
                return self.Cards[-1].Value > other.Cards[-1].Value
            elif (selfRank == Ranks.FourOfKind):
                pass

            elif (selfRank == Ranks.FullHouse):
                pass
            elif (selfRank == Ranks.Flush):
                pass
            elif (selfRank == Ranks.Straight):
                pass
            elif (selfRank == Ranks.ThreeOfKind):
                pass
            elif (selfRank == Ranks.TwoPairs):
                pass
            elif (selfRank == Ranks.OnePair):
                selfFirstValue = 0
                for card, count in self.valueCounters.iteritems():
                    if (count == 2):
                        selfFirstValue = card
                otherFirstValue = 0
                for card, count in other.valueCounters.iteritems():
                    if (count == 2):
                        otherFirstValue = card
                if (selfFirstValue == otherFirstValue):
                    self.Cards[-1] > other.Cards[-1]
                return selfFirstValue > otherFirstValue                              
            elif (selfRank == Ranks.HighCard):
                return self.Cards[-1] > other.Cards[-1]
            else:
                print "Error: invalid something"


        else:
           return False


    def __lt__(self, other):
        return (not (self > other))


    @classmethod
    def Parse(cls, s):    
        cardsStr = s.split(" ")
        cards = []
        for cStr in cardsStr:
            c = Card.Parse(cStr)
            cards.append(c)
        return cls(cards)

    def _countSuits(self):
        self.suitCounters = {'H' : 0, 'C' : 0, 'D' : 0, 'S' : 0}

        for c in self.Cards:
            self.suitCounters[c.Suit] += 1

    def _countValues(self):
        self.valueCounters = {}
        for v in range(2,14+1):
            self.valueCounters[v] = 0

        for c in self.Cards:
            self.valueCounters[c.Value] += 1

    def _countValuesAndSuits(self):
        self._countSuits()
        self._countValues()

    def _isSequence(self):
        for i in range(len(self.Cards)-1):
            if (self.Cards[i].Value + 1 != self.Cards[i+1].Value):
                return False
        return True

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

    def _rankFullHouse(self):
        self._countValues()

        trinca = False
        dupla = False
        for k, v in self.valueCounters.iteritems():
            if (v == 3):
                trinca = True
            if (v == 2):
                dupla = True
        return dupla and trinca

    def _rankFourOfKind(self):
        self._countValues()

        for k, v in self.valueCounters.iteritems():
            if (v == 4):
                return True
        return False

    def _rankFlush(self):
        self._countSuits()

        for k, v in self.suitCounters.iteritems():
            if (v == 5):
                return True
        return False

    def _rankStraight(self):
        return self._isSequence()

    def _rankThreeOfKind(self):
        self._countValues()

        for k, v in self.valueCounters.iteritems():
            if (v == 3):
                return True
        return False

    def _rankTwoPairs(self):
        self._countValues()
        pairs = 0

        for k, v in self.valueCounters.iteritems():
            if (v == 2):
                pairs += 1
        return pairs == 2

    def _rankOnePair(self):
        self._countValues()

        for k, v in self.valueCounters.iteritems():
            if (v == 2):
                return True
        return False


    def Rank(self): 
        if (self._rankRoyalFlush()):
            return Ranks.RoyalFlush
        if (self._rankStraightFlush()):
            return Ranks.StraightFlush
        if (self._rankFourOfKind()):
            return Ranks.FourOfKind
        if (self._rankFullHouse()):
            return Ranks.FullHouse
        if (self._rankFlush()):
            return Ranks.Flush
        if (self._rankStraight()):
            return Ranks.Straight
        if (self._rankThreeOfKind()):
            return Ranks.ThreeOfKind
        if (self._rankTwoPairs()):
            return Ranks.TwoPairs
        if (self._rankOnePair()):
            return Ranks.OnePair
        else:
            return Ranks.HighCard
        


def CompareHands(string):
    sLen = len(string)

    h0Str = string[:sLen/2]
    h1Str = string[sLen/2 + 1:]
    
    h0 =  Hand.Parse(h0Str)
    h1 =  Hand.Parse(h1Str)
    
    #print h0
    #print h1

    if (h0 > h1):
        return 1
    else:
        return 2





def SolveProblem():
    print "."   

    cardHands = ReadCardsFile("input/input54.txt")

    p1 = 0
    p2 = 0

    for cHand in cardHands:
        w = CompareHands(cHand)
        if (w == 1):
            p1 += 1
        else:
            p2 += 1

    print p1 
    print p2


    return p1