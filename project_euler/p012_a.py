#	
#	Project Euler 
#	Problem #12
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=12
#
# Approach A: One-liner, not as elegant
#	

import euler_shared
from math import sqrt, ceil

def num_factors(n):
	return 2 + sum([2 if n % i == 0 else 0 for i in range(2, ceil(sqrt(n)))])

def p012():
	cur_val = 1
	incr = 2
	while num_factors(cur_val) < 500:
		cur_val += incr
		incr += 1
	return cur_val

if __name__ == '__main__':
	print(p012())