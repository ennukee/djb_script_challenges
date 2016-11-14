#	
#	Project Euler 
#	Problem #19
#
#	Dylan Bowers
#
# https://projecteuler.net/problem=19
#	

def p019():
	output = 0
	month, first_day, year = 1, 2, 1901 # Jan 1 1901 is a Tuesday
	
	# Distance from 28. These will cause offsets as the months change. 31 days will cause 
	# a +3 move in the day of the week of the first day (as the extra 3 days over a smooth
	# 4 weeks will push it forward), and so on.
	fd_jumps = {
		0: 3,
		1: 0,
		2: 3,
		3: 2,
		4: 3,
		5: 2,
		6: 3, 
		7: 3,
		8: 2,
		9: 2,
		10: 3,
		11: 2
	}

	while year != 2000 and month != 12:
		if first_day == 0: output += 1

		# Normally, we'd test for the century case (non-%100 unless %400), but since our given
		# year set is 1901 to 2000, all year%4 in this case are proper, so we ignore the century case.
		if year % 4 == 0 and month == 1: 
			first_day = (first_day + 1) % 7	
		else: 
			first_day = (first_day + fd_jumps[month]) % 7
		
		year += (month + 1) // 12
		month = (month + 1) % 12
	return output

if __name__ == '__main__':
	print(p019())