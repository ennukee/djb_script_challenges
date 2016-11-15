#	
#	Project Euler 
#	Problem #22
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=22
#	

def p022(i):
	return sum(sum(ord(x) - 64 for x in i[n]) * (n + 1) for n in range(len(i)))

if __name__ == '__main__':
	with open('p022_names.txt') as f:
		data = sorted([name.strip('"') for name in f.read().split(',')])
		print(p022(data))