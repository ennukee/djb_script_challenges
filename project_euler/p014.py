#	
#	Project Euler 
#	Problem #14
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=14
#	

def collatz_seq(i, l, kl):
	if i == 1: 						return l 							# Base case: 1 = 1
	elif kl.get(i, None): return l + kl[i] - 1  # Base case: known length
	else:
		if i % 2 == 0: 			return collatz_seq(i // 2, l + 1, kl)				# Recursive case: even i, i/2
		else: 				 			return collatz_seq((i * 3) + 1, l + 1, kl)  # Recursive case: odd i, 3i+1

def p014():
	known_lengths = {1: 1, 2: 2}
	longest_seq = (2, 2)

	for i in range(3, 1000000):
		cs = collatz_seq(i, 1, known_lengths)
		
		if cs > longest_seq[1]: 	 	longest_seq = (i, cs)
		if i not in known_lengths: 	known_lengths[i] = cs

	return longest_seq[0]

if __name__ == '__main__':
	print(p014())