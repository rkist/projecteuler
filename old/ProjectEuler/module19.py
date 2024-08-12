from datetime import date,timedelta

def SolveEx19():
    #(1 Jan 1901 to 31 Dec 2000)
    fromdate = date(1901,1,1)
    todate = date(2000,12,31)
    daygenerator = (fromdate + timedelta(x + 1) for x in xrange((todate - fromdate).days))

    sum = 0
    for day in daygenerator:
        if day.weekday() == 6 and day.day == 1:
            sum +=1

    print sum