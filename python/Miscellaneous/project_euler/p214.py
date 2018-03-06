from fractions import gcd
from math import log

def is_prime(i):
	return all(gcd(i,x)==1 for x in range(1,int(i/2)+1))

# def euler(i):
	# if is_prime(i):
	# 	return i - 1
	# global cur
	# cur = i

	# p = filter(prime_and_divisible, range(2, int(i)))
	# v = i
	# for n in p:
	# 	v *= (1 - 1/n)
	# return int(v)
	# return sum(1 if gcd(i,n)==1 else 0 for n in range(1,i))

# def euler_chain_len(i):
# 	#if known.get(i):
# 	#	return known.get(i)
# 	l = 1
# 	c = i
# 	er = euler(c)
# 	while er != 1:
# 		l += 1
# 		er = euler(er)
# 		if l > 25:
# 			return 0
# 	return l + 1

# def euler_chain(i):
# 	c = i
# 	ch = [str(c)]
# 	er = euler(c)
# 	while er != 1:
# 		ch.append(str(er))
# 		er = euler(er)
# 	return ', '.join(ch + ['1'])

def main(n):
	# Primes and the greatest prime factors (gpf) per number
	greatest_prime_factors = [0] * (n + 1)
	primes = [False] + [is_prime(x) for x in range(1,n+1)]
	print('Primes done')

	for i in range(4, n + 1):
		if primes[i]:
			continue
		for q in range(2, n):
			if i%q==0 and gcd(i/q,q)==1:
				greatest_prime_factors[i] = q
				break
	# print('\n'.join(["{}: {}".format(i, greatest_prime_factors[i]) for i in range(0,n+1)]))
	# return
	print('Greatest Prime Factors done')

	# Prime powers for tot(p^k) = p^k - p^(k-1)
	prime_powers = [0] * (n + 1)
	for i in range(1, len(primes) + 1):
		max_power = int(log(i, 2))
		# print('{}, {}'.format(i, max_power))
		for q in range(2, max_power + 1):
			p = round(pow(i, 1/q), 10) # because python is inept at accurate fraction math
			print("{}, {}, {}".format(i, max_power, p))
			if p.is_integer() and primes[int(p)]:
				print('ding')
				prime_powers[i] = int(p)
	print('Prime powers done')

	# print(primes)
	# print('\n'.join(["{}: {}".format(i, prime_powers[i]) for i in range(0,n+1)]))

	# Calculate totients
	tots = [0, 1] + [0] * (n - 1)
	for i in range(2, n + 1):
		print(i)
		if primes[i]:
			tots[i] = i - 1
		elif prime_powers[i] != 0: 
			tots[i] = int(i - (i / prime_powers[i]))
		else:
			gpf = greatest_prime_factors[i]
			tots[i] = tots[gpf] * tots[int(i/gpf)]
	print('Totients done')

	# print('\n'.join(["{}: {}".format(i, tots[i]) for i in range(0,n+1)]))
	# return

	twenty_five_count = 0
	for i in range(2, n + 1):
		cur = i
		l = 1
		while cur != 1:
			l += 1
			# print(cur)
			cur = tots[cur]
		# print("{}: {}".format(i, l))
		twenty_five_count += (1 if cur == 25 else 0)

	return twenty_five_count

	# s = 0
	# for n in filter(is_prime, range(1000000, 40000000)):
	# 	ecl = euler_chain_len(n - 1)
	# 	print("{}: {}".format(n, 1 + ecl))
	# 	if (1 + ecl) == 25: # all prime euler chain lengths are equal to n - 1
	# 		print('{} has euler chain of len 25'.format(n))
	# 		s += n

if __name__ == "__main__":
	import sys
	main(int(sys.argv[1]))

# if __name__ == '__main__':
# 	import sys
# 	for i in sys.argv[1:]:
# 		print(euler_chain(int(i)))

# if is_prime(i):
# 	return i - 1

# valid = i - 1
# for n in filter(prime_and_divisible, zip([i]*(i-3), range(3, i))):
# 	valid -= (i/n - 2)

# def prime_and_divisible(i):
# 	return cur%i==0 and is_prime(i)