"""
This program finds the set of all harmonious numbers for given numbers.

To find the set of factors from a number I used the following article:
http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

To reduce the times we need to call sumFactors I have used the following article to reduce my search space:
https://sech.me/ap/articles.html#a1

Oliver Reid - 2569385
"""

from math import sqrt
from collections import OrderedDict

##
# Returns the sum of the factors of a number n.
#
# @param n The number to factor and sum.
# @return The sum of the factors of n.
##
def sumFactors(n, cache={}):
	if cache.get(n) is not None:
		return cache[n]
	cache[n] = sum(set(sum([[i, n//i] for i in xrange(2, int(sqrt(n)) + 1) if not n%i], [])))
	return cache[n]

##
# Checks to see if two numbers are harmonious to each other.
#
# @param first The first number to check.
# @param second The second number to check.
# @return True if the numbers are harmonious, false otherwise.
##
def harmonious(first, second):
	if sumFactors(second) == first:
		return True
	return False

##
# Main method
##
harmoniousNumbers = OrderedDict()
first = 1
while first < 2000000:
	second = sumFactors(first)
	if second > first and harmonious(first, second):
		harmoniousNumbers[min(first, second)] = max(first, second)
	first += 1

#Print out the pairs
for i in range(len(harmoniousNumbers)):
    print harmoniousNumbers.keys()[i],
    print harmoniousNumbers.values()[i]