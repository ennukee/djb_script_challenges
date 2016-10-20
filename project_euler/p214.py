#
# Project Euler 
# Problem 214
#
# by Dylan Bowers (shoutout to Phi for introducing me to Euler with this problem!)
#
# https://github.com/enragednuke/djb_script_challenges
#
# Approximate Run-time: 
#	Totients ->  63s
#	TCLs     ->  84s
#   Total    -> ~84s
#

# Faster memory access data structure alternative since we're working with massive arrays here
from array import array as bigarray

def p214(limit):
	# Pre-calculate all the totients for every value from 1 to limit
	answer = 0
	all_totients = bigarray('l', range(limit + 1))
	for n in range(2, limit + 1):
		# Anything that remains as its value is a number not affected by any multiple of a previous number
		# thus, it must have been a prime number and we will use it to divide more factors from future
		# values

		if n == all_totients[n]:
			for m in range(n, limit + 1, n):
				# See this: https://en.wikipedia.org/wiki/Euler%27s_totient_function

				all_totients[m] //= n
				all_totients[m] *= (n - 1) 		

	print('-> All totients calculated')

	# Starter array for the totient chain lengths. Will be used in a backwards referential manner
	# as totient chain lengths can be calculated by looking at previous values
	#
	# Specifically, a chain length for some `i` is the chain length of the totient of `i` plus 1 to account
	# for the value of `i`
	# So for example, TCL(8) => TCL(tot(8)) + 1 => TCL(4) + 1 => TCL(tot(4)) + 2 => TCL(2) + 2
	#                        => TCL(2) + 2 => TCL(tot(2)) + 3 => TCL(1) + 3 => 1 + 3 => 4
	# But because we'd know TCL(4), we'd stop at the first step
	tot_chain_lengths = bigarray('l', [0, 1])  # We precalculate the ezpz 1-3 values
	for n in range(2, limit):
		TCL = tot_chain_lengths[all_totients[n]] + 1
		tot_chain_lengths.append(TCL)

		# Now we just need to check if it satisfies our condition before we move on
		def is_prime(i):
			# A prime `i` totient will be i - 1, as all numbers will not divide into it except itself
			return all_totients[i] == i - 1
		if TCL == 25 and is_prime(n):
			answer += n

	print('-> All TCLs calculated')

	return answer

if __name__ == "__main__":
	import sys
	UPPER_BOUND = int(sys.argv[1])
	print(p214(UPPER_BOUND - 1))