#
#	Project Euler
#	Problem #53
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=53
# 	
#

import math
fac = math.factorial

def p053():
	count = 0

	for i in range(1, 101):
		for q in range(0, i):
			if fac(i) / (fac(q) * fac(i - q)) > 1000000: count += 1
	return count

if __name__ == '__main__':
	print(p053())
