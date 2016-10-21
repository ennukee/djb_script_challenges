#	
#	Project Euler 
#	Problem #2
#
#	Dylan Bowers
#
#	Elapsed Run-time: 0.000000s
#	Result: 4613732
#	


from math import sqrt

def f(n):
	Phi = (sqrt(5) + 1) / 2
	phi = 1/Phi
	v = pow(Phi, n) - pow((-phi), n)

	return v/sqrt(5)

def main():
	i = 0
	fn = 0
	t = 0
	while fn < 4000000:
		t += fn
		i += 3
		fn = f(i)
	print(t)

if __name__ == '__main__':
	main()
