#	
#	Project Euler 
#	Problem #7
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=7
#	

from math import sqrt

def isprime(x):
	return not any(x % i == 0 for i in range(3, int(sqrt(x) + 1), 2))

def p010(n):
	assert n > 2, 'p010 solution only accepts nth prime where n > 2'

	# Starting at 3 for the sake of incrementing by 2
	i = 3
	n -= 1

	while n:
		i += 2
		if isprime(i):
			n -= 1
	return i

if __name__ == '__main__':
	print(p010(10000))