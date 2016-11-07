#	
#	Project Euler 
#	Problem #18
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=18
#	

import math

def p018(inp, cur_data, row):
	print(cur_data)
	if row == len(inp) - 1:
		return max(cur_data)

	items_in_row = row + 1
	new_data = [0] * (items_in_row + 1)
	for i in range(0, len(cur_data)):
		new_data[i] = max(new_data[i], cur_data[i] + inp[row + 1][i])
		new_data[i + 1] = max(new_data[i + 1], cur_data[i] + inp[row + 1][i + 1])

	return p018(inp, new_data, row + 1)

if __name__ == '__main__':
	with open('p018_input.txt') as f:
		data = [[int(x) for x in line.strip().split()] for line in f.readlines()]
		print(p018(data, data[0], 0))