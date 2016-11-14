#	
#	Project Euler 
#	Problem #17
#
#	Dylan Bowers
#
# https://projecteuler.net/problem=17
#	

def numeric_to_alpha_c(n):
	key = {
		'1': {
			0: '',
			1: 'one', 
			2: 'two', 
			3: 'three', 
			4: 'four', 
			5: 'five', 
			6: 'six', 
			7: 'seven', 
			8: 'eight', 
			9: 'nine'
		},
		'10': {
			0: '',
			10: 'ten',
			11: 'eleven',
			12: 'twelve',
			13: 'thirteen',
			14: 'fourteen',
			15: 'fifteen',
			16: 'sixteen',
			17: 'seventeen',
			18: 'eighteen',
			19: 'nineteen',
			20: 'twenty',
			30: 'thirty',
			40: 'forty',
			50: 'fifty',
			60: 'sixty',
			70: 'seventy',
			80: 'eighty',
			90: 'ninety'
		}
	}
	out = []
	assert n in range(1, 1001), 'Problem 17 supports only 1 to 1000'
	if n == 1000: out.append('one thousand')
	if n % 1000 >= 100:	out.append('{} hundred'.format(key['1'][(n % 1000) // 100]))
	if n % 100:
		if n >= 100: out.append('and')

		if n % 100 in range(10, 20):
			out.append(key['10'][n%100])
		else:
			out.append(key['10'][10*((n%100)//10)])
			out.append(key['1'][n%10])
	return ' '.join(out)

def p017(n):
	return sum(len(numeric_to_alpha_c(x).replace(' ','')) for x in range(1, n + 1))

if __name__ == '__main__':
	print(p017(1000))
