#	
#	Project Euler 
#	Problem #16
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=16
#	

def simplify(a):
	for i in range(len(a)):
		if a[i] >= 10:
			if i == len(a) - 1:
				a.append(a[i] // 10)
			else:
				a[i+1] += (a[i] // 10)
			a[i] %= 10
	return a

def p016(ca, n):
	# A recursive approach was overflowing the stack, so have a normal loop

	for c in range(n): ca = simplify([2*x for x in ca])
	return sum(ca)

if __name__ == '__main__':
	print(p016([1], 1000))