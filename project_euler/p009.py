#	
#	Project Euler 
#	Problem #9
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=9
#	

def p009():
	for i in range(1, 1001):
		for q in range(1, 1001 - (500 - i)):
			r = 1000 - (i + q)
			if pow(i, 2) + pow(q, 2) == pow(r, 2):
				return i * q * r

if __name__ == '__main__':
	print(p009())