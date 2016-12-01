from math import sqrt, ceil

# Uses the Sieve of Eratosthenes to provide a list of prime values up to a max value `m`
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def list_primes(m):
	# Assume everything is a prime at first
	prime_v = [False, False] + [True] * (m - 1)

	# Max bound while sieving is sqrt(upper bound)
	for n in range(2, int(sqrt(m)) + 1):

		# If we consider some `n` to be prime, then we need to consider all future multiples to be not prime
		if prime_v[n]:

			# However, the values between `n` and `n*n` would be marked 'not prime' by other prime values,
			# so we do not need to consider those values and we start at n * n
			for np in range(n * n, m, n):
				prime_v[np] = False
	return prime_v

# We choose this approach of a simple range(2, int(sqrt(x) + 1)) because
# this overall method is much faster for large `x` even if the code is slightly
# uglier
def isprime(x):
	return x % 2 == 1 and not any(x % i == 0 for i in range(3, int(sqrt(x) + 1), 2))

def array_equivalent(a1, a2):
	if len(a1) != len(a2): return False
	for i in range(len(a1)):
		if a1[i] not in a2: return False
		else:
			a2 = a2[:a2.index(a1[i])] + a2[a2.index(a1[i]) + 1:]
	return True

def array_all_same(a1):
	assert len(a1) > 0, 'Array must not be empty'
	return all(x == a1[0] for x in a1)

def is_palindrome(n):
	assert str(n).isdigit(), 'is_palindrome parameter must be an integer'

	n = str(n)
	return all(n[i] == n[len(n)-i-1] for i in range(0, ceil(len(n) / 2)))
