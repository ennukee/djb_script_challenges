#
#   Project Euler
#   Problem #26
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=26
#   

from math import pow
import euler_shared

def helper(n):
	primality_list = euler_shared.list_primes(n)
	b_vals = [x for x in range(0, n - 1) if primality_list[x]]
	a_vals = list(range(-1 * (n-1), n))
	a_b = [(x, y) for x in a_vals for y in b_vals if y > abs(x)]

	mx, am, bm = 0, 0, 0
	for comb in a_b:
		a, b = comb[0], comb[1]
		i, prime_combo = 0, 0
		while True:
			if euler_shared.isprime(i*i + a*i + b):
				prime_combo += 1
				i += 1
			else:
				break
		if prime_combo > mx:
			mx, am, bm = prime_combo, a, b
	return mx, am, bm

def p027():
	return helper(1000)

if __name__ == '__main__':
	# Configure this per problem
	project = "PROJECT EULER"
	problem = p027
	# End of configuration

	import time
	start = time.time()
	r = problem()
	end = time.time()
	print("-- {} {} --\nOutput: {}\nCompleted in {}s".format(project, problem.__name__, r, end - start))
