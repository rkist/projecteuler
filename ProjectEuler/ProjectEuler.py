import module14


#seq = module14.GetCollatzSequence(13)
#print len(seq)
#print seq




maxSize = -1
maxN = 1

for n in xrange(1,1000000):
    size = module14.GetCollatzSequenceSize(n)
    if size > maxSize:
        maxSize = size
        maxN = n
        print maxN, maxSize







