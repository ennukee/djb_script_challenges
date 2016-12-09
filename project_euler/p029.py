#
#   Project Euler
#   Problem #29
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=29
#

import euler_shared

# INCOMPLETE SOLUTION #

def solve(n):
	# Overlaps will only occur when we have exponents of lower numbers.
	# Example: 2^8 = 4^4 or 6^6 = 6^2^3 = 36^3
	primality = euler_shared.list_primes(100)
	not_primes = [x for x in range(2, 101) if not primality[x]]
	return 0

def p029():
	print(euler_shared.list_factors_of(10))
	return solve(100)

if __name__ == '__main__':
	# Configure this per problem
	project = "PROJECT EULER"
	problem = p029
	# End of configuration

	import time
	start = time.time()
	r = problem()
	end = time.time()
	print("-- {} {} --\nOutput: {}\nCompleted in {}s".format(project, problem.__name__, r, end - start))
