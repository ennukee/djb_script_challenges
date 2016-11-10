#	
#	Project Euler 
#	Problem #13
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=13
#	

# There is another approach to mass-merge everything together and repeatedly "carry" numbers 
# until every field is a single-digit number, but I chose this approach instead, which does a
# fixed length-based carrying every time a new set is appended

def fuse_numarrays(a1, a2):
	# Assumes two arrays that are in 'reverse syntax' (i.e. the ones place is index 0)
	# We assume `a1` is always going to be the master `init` array

	for n in range(len(a2)):
		a1[n] += a2[n]
	return correct_numarray(a1)

def correct_numarray(arr):
	for n in range(len(arr)):
		if arr[n] >= 10:
			if n == len(arr) - 1:
				arr.append(arr[n]//10)
				arr[n] %= 10
			else:
				arr[n + 1] += arr[n]//10
				arr[n] %= 10
			return correct_numarray(arr)
	return arr

def p013(init, inp):
	for sset in inp:
		# Because the length of `init` and `sset` and be different, we don't want
		# to try and zip them together and sum that way

		init = fuse_numarrays(init, sset)
	return init[-10:][::-1] # Last ten indices, then reverse them


if __name__ == '__main__':

	# Input parsing
	with open('p013_input.txt', 'r') as f:

		# I reverse the order of indices for the sake of simplicity of adding
		# so that I can do a[0] for ones, instead of a[-1] or a[len-1], etc
		f = [x.strip()[::-1] for x in f.readlines()]
		f = [[int(x) for x in y] for y in f]
		print(p013(f[0], f[1:]))