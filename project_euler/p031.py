#
#   Project Euler
#   Problem #31
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=31
#	Completes in approximately 6.51s
#

import euler_shared
import itertools, functools, operator, math

# cv = current value of recursive call
# coins = remaining coins to be considered
def r(cv, coins):
	if cv >= 200 or len(coins) == 0: return cv == 200

	# two cases: 
	# - add the front coin, continue
	# - don't add, remove coin forever
	return r(cv + coins[0], coins) + r(cv, coins[1:])

def p031():
	return r(0, [200, 100, 50, 20, 10, 5, 2, 1])

if __name__ == '__main__':
	# Configure this per problem
	project = "PROJECT EULER"
	problem = p031
	# End of configuration

	import time
	start = time.time()
	r = problem()
	end = time.time()
	print("-- {} {} --\nOutput: {}\nCompleted in {}s".format(project, problem.__name__, r, end - start))
