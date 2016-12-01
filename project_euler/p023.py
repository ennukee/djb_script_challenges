#	
#	Project Euler 
#	Problem #23
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=23
#	

from math import sqrt

def type_of_num(n):
	print(n)
	factor_sum = 1 + sum([x for x in range(2,n) if n%x==0])

	if factor_sum < n: 		return -1 # Deficient number
	elif factor_sum == n: 	return 0  # Perfect number
	else: 					return 1  # Abundant number

def calculate_abundant_nums(m):
	# Calculate the "sums of all factors" for every number up to `m`
	# Designed based on the Sieve of Eratosthenes

	nums = range(0, m + 1)
	sums = [1] * (m + 1)
	for n in range(2, m//2 + 1):
		for np in range(2 * n, m + 1, n):
			sums[np] += n
	return [x for x in nums if sums[x] > x][1:] # filter out 0

def p023(limit):
	abundant_nums = calculate_abundant_nums(limit)
	filter_abuns = lambda n: [i for i in abundant_nums if i <= (limit - n)]

	valid_numbers = list(range(0, limit + 1))
	sum_state = [True] * (limit + 1)
	for x in abundant_nums:
		for y in filter_abuns(x):
			sum_state[x+y] = False
	
	return sum(i if sum_state[i] else 0 for i in range(limit + 1))

if __name__ == '__main__':
	print(p023(28123))