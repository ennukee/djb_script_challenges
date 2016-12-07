#
#   Project Euler
#   Problem #29
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=29
#

# INCOMPLETE SOLUTION #

def solve(n):
	# Overlaps will only occur when we have exponents of lower numbers.
	# Example: 2^8 = 4^4 or 6^6 = 36^3

def p028():
	return solve(...)

if __name__ == '__main__':
	# Configure this per problem
	project = "PROJECT EULER"
	problem = p028
	# End of configuration

	import time
	start = time.time()
	r = problem()
	end = time.time()
	print("-- {} {} --\nOutput: {}\nCompleted in {}s".format(project, problem.__name__, r, end - start))
