#	
#	Project Euler 
#	Problem #21
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=21
#	

from math import sqrt
def d(n):
	return 1 + sum(i + n//i if n%i==0 else 0 for i in range(2, int(sqrt(n) + 1)))

def p021(n):
	values = [None] * n
	is_amicable = [False] * n

	for i in range(1, n):
		v = d(i)
		values[i] = v
		if v < i and values[v] == i:
			is_amicable[i] = True
			is_amicable[v] = True

	return sum(i if is_amicable[i] else 0 for i in range(1, n))

if __name__ == '__main__':
	print(p021(10000))