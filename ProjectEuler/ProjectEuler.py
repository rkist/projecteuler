
import module9



for a in xrange(1,1000):
    for b in xrange(1,1000 - a):
        c = 1000 - a - b
        if module9.IsPythagoreanTriplet(a, b, c):
            print a*b*c
