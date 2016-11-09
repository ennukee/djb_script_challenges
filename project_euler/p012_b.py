#	
#	Project Euler 
#	Problem #12
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=12
#
#	Approach B: A more readable, but less concise code
#	

import euler_shared
from math import sqrt, ceil

def num_factors(n):
	c = 2
	for i in range(2, ceil(sqrt(n))):
		if n % i == 0:
			c += 2
	return c

def p012():
	cur_val = 1
	incr = 2
	while num_factors(cur_val) < 500:
		cur_val += incr
		incr += 1
	return cur_val

if __name__ == '__main__':
	print(p012())