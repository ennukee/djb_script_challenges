#
#   Project Euler
#   Problem #28
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=28
#

def solve(n):
	# Each number scales based on it's "layer"
	# Layer Zero:  1
	# Layer One:   3  5  7  9  (+2)
	# Layer Three: 13 17 21 25 (+4) and so on

	total, last_number, layer = 1, 1, 1
	while layer < n:
		for i in range(4):
			last_number += (layer + 1)
			total += last_number
		layer += 2
	return total

def p028():
	return solve(1001)


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
