#	
#	Project Euler 
#	Problem #25
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=25
#	

def p025(n):
	values, current_index = [1, 1], 2
	while len(str(values[-1])) != n:
		values.append(values[current_index - 1] + values[current_index - 2])
		current_index += 1

	return current_index

if __name__ == '__main__':
	print(p025(1000))