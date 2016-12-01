#	
#	Project Euler 
#	Problem #52
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=52
#	

def p052():
	vl = 3 # Start at 3 because there's no way this occurs in anything lower than 1000

	while True:
		for i in range(pow(10, vl), pow(10, vl+1) // 6):
			if all(all(x in y for y in [str(z*i) for z in range(2, 7)]) for x in str(i)):
				return i
		vl += 1

if __name__ == '__main__':
	print(p052())