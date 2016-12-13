#
#   Project Euler
#   Problem #29
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=29
#

import euler_shared
import itertools, functools, operator, math

# Solves in about 0.07s
def solve(n):
	valid = (n-1)*(n-1)
	factors_of_b = euler_shared.list_factors_of(n)
	c_o_f_o_b = [[],[]]
	for i in range(2, n+1):
		f_o_b = factors_of_b[i]
		c_o_f_o_b.append(list(set(euler_shared.flatten([itertools.combinations(f_o_b, i) for i in range(1, len(f_o_b))]))))

	for a in range(2, n+1):
		for b in range(2, n+1):
			perms = c_o_f_o_b[b]
			multiplied = [functools.reduce(operator.mul, i) for i in perms]
			for combo in multiplied:
				if pow(a, combo) <= n:
					valid -= 1
	return valid + 1

# Alternate brute force approach
# Solves in about 1.35s
def brute_force(n):
	known = []
	corresponding = []
	n_v = [0 for i in range(n+1)]
	for a in range(2, n+1):
		for b in range(2, n+1):
			res = pow(a, b)
			if res in known:
				known.append('Known')
				what_has_it = known.index(res)
				(a_t, b_t) = corresponding[what_has_it]
				n_v[a_t] += 1
			else:
				known.append(res)
			corresponding.append((a, b))
	return sum(1 if i != 'Known' else 0 for i in known)

def p029():
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
