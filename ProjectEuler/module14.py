def GetCollatzSequence(n):
    seq = [n]
    __GetCollatzSequenceRecursion__(seq)
    return seq

def GetCollatzSequenceSize(n):
    if n == 1:
        return 1
    elif n % 2 == 0: 
        return 1 + GetCollatzSequenceSize(n/2)
    else:
        return 1 + GetCollatzSequenceSize(3*n+1)


def __GetCollatzSequenceRecursion__(seq):
    last = seq[-1]
    if last == 1:
        return seq
    elif last % 2 == 0: 
        seq.append(last/2)
    else:
        seq.append(3*last+1)
    return __GetCollatzSequenceRecursion__(seq)
