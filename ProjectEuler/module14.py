def GetCollatzSequence(n):
    seq = [n]
    GetCollatzSequenceRecursion(seq)
    return seq

def GetCollatzSequenceRecursion(seq):
    last = seq[-1]
    if last == 1:
        return seq
    elif last % 2 == 0: 
        seq.append(last/2)
    else:
        seq.append(3*last+1)
    return GetCollatzSequenceRecursion(seq)
