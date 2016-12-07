#   
#   Project Euler 
#   Problem #26
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=26
#   

def cycle_in_frac(n, d):
	# Two cases for `d`
	#  1. of form 2^a * 5^b, this will terminate thus cycle length 0
	#  2. of form 2^a * 5^b * m for some m > 1, this will have max(a, b) 
	#     non-repeating at start followed by a repeating section of unk
	#     length. Note: a and b and be 0.

	po2, po5, dc = 0, 0, d
	while dc % 2 == 0:
		dc /= 2
		po2 += 1
	while dc % 5 == 0:
		dc /= 5
		po5 += 1
	if dc == 1:
		return 0 # If `d` is of form 2^a * 5^b, it terminates and has no cycle

	skip_amount = max(po2, po5) # Number of pre-period digits

	prev = []
	while (n, d) not in prev:
		prev.append((n, d))
		m_result = n % d
		n = m_result * 10
	prev = prev[skip_amount+1:]
	return len(prev)

def p026():
	return "highest length {} cycle in 1/{}".format(*max((cycle_in_frac(1, i), i) for i in range(2, 1000)))

if __name__ == '__main__':
	print(p026())