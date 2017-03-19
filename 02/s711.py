"""
This program solves the 711 problem. It tries a bruteforce approach but also
checks for math like properties e.g. if a number divides 711000000.

Oliver Reid - 2569385
"""

#Data fields
numAdd = 711
numTimes = 711000000

#Rules are that each value must be positive and an integer number of cents
def findNumber(numAdd, numTimes):
    d = 1
    while(d < (numAdd - 3)):
        if(numTimes % d == 0):
            c = 1
            while((d + c <= (numAdd - 2)) and c <= d):
                if(numTimes % c == 0):
                    b = 1
                    while(((d + c + b) <= (numAdd - 1)) and b <= c):
                        a = numAdd - (d + c + b)
                        if(a <= b):
                            if((a*b*c*d) == numTimes):
                                return("$%.2f" % float(numAdd/100.0) + " = " + "$%.2f" % float(a/100.0) + " + " + "$%.2f" % float(b/100.0) + " + " + "$%.2f" % float(c/100.0) + " + " + "$%.2f" % float(d/100.0))
                        b+= 1
                c += 1
        d += 1


##
# Main routine
##
print(findNumber(numAdd, numTimes))


