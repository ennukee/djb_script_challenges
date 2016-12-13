#
#   Project Euler
#   Problem #29
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=29
#

# Solves in about 0.53s
def cpp_way():
    fifth_pows = [0 for i in range(10)]
    for i in range(10):
        fifth_pows[i] = i*i*i*i*i

    total_s = 0
    for i in range(2, 200000):
        indiv_s, original_i = 0, i
        while i > 0:
            digit = i % 10
            indiv_s += fifth_pows[digit]
            i //= 10
        if indiv_s == original_i:
            total_s += indiv_s
    return total_s

# Solves in about 1.05s
def python_way():
    fifth_pows = [pow(x, 5) for x in range(0,10)]
    calc_sum = lambda x: sum(fifth_pows[int(i)] for i in str(x))
    return sum(x if (calc_sum(x) == x) else 0 for x in range(2, 200000))

def p030():
	return cpp_way()

if __name__ == '__main__':
	# Configure this per problem
	project = "PROJECT EULER"
	problem = p030
	# End of configuration

	import time
	start = time.time()
	r = problem()
	end = time.time()
	print("-- {} {} --\nOutput: {}\nCompleted in {}s".format(project, problem.__name__, r, end - start))
