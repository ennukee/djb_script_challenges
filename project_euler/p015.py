#	
#	Project Euler 
#	Problem #15
#
#	Dylan Bowers
#
#   https://projecteuler.net/problem=15
#	


import math
def p015(n):
	"""
	How many strings can I made of 20 downs and 20 rights?

	2n choose n
	(2n)! / (n! + n!)
	"""
	return math.factorial(n * 2) // (math.factorial(n) ** 2)

if __name__ == '__main__':
	print(p015(20))
