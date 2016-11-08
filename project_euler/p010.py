#	
#	Project Euler 
#	Problem #10
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=10
#	

import euler_shared

def p010():
	primes = euler_shared.list_primes(2000000)
	return sum(x for x in range(2, 2000000) if primes[x])

if __name__ == '__main__':
	print(p010())