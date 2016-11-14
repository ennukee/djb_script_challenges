#	
#	Project Euler 
#	Problem #20
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=20
#	

import math
def p020(n):

	# There's no reason not to just brute-force it since 100! is not an exceedingly large
	# numeric value in Python
	return sum(int(x) for x in str(math.factorial(n)))

if __name__ == '__main__':
	print(p020(100))