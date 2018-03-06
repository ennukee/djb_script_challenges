####################################################
# 		  WELCOME TO THE BINARY BOMB SOLVER 	   #
# Designed to crack any CS230 Binary Bombs for S16 #
# 												   #
# Instructions:									   #
#  1. Download your binary bomb 				   #
#  2. Run the following command: 				   #
#		objdump -d BOMB_FILE_NAME > assembly.txt   #
#  3. Place the asssembly.txt file in the same	   #
#		directory as the python file 			   #
#  4. Type 'py binary_bomb_solver.py' 			   #
#  5. Voila, your outputs should be printed		   #
####################################################
from __future__ import print_function
import urllib
from subprocess import call
import sys
output = open('output.txt', 'w')

def main():
	intro = """
	###################################################
	#        WELCOME TO THE BINARY BOMB SOLVER        #
	# Designed to crack any CS230 Binary Bomb for S16 #
	###################################################"""

	call("rm -f assembly.txt", shell=True)
	call("rm -f solution.txt", shell=True)
	print(intro)
	print("If you get an 'index of of bounds' exception, you \nlikely entered the wrong ID\n")
	s_id = input("Please enter your student ID: ")

	if(s_id==000):
		call("rm -f output/*", shell=True)
		print("Beginning solving of every ID...")
		f = open('IDs.txt','r')
		#print(f.readlines())
		for i in f.readlines():
			print("%s done" % i.rstrip())
			solve(i.rstrip(), True)
		f.close()
		print("Every ID has been computed. See the output folder.")
	else:
		solve(s_id)
	

def rip_no_conv(i, f):
	return f[i].split()[-1].split(',')[0].replace('$','')
	increment_load()

def rip(i, f):
	return int(f[i].split()[-1].split(',')[0].replace('$',''), 16)

def solve(name, is_all=False):
	global output
	if(is_all):
		output.close()
		output = open("output/%s.txt" % str(name), 'w')
	urllib.urlretrieve("http://www-edlab.cs.umass.edu/cs230/hw/hw6/bombs/" + str(name), str(name))
	try:
		open(name, 'r')
	except IOError:
		return
	call("chmod 777 " + str(name), shell=True)
	call("objdump -d %s > assembly.txt" % name, shell=True)

	output.write("Answers for ID %d\n" % int(name))
	f = open('assembly.txt', 'r').readlines()[6:]
	
	# Phase 1, int arithmetic into char conversion #
	output.write("Phase 1: %c\n" % (rip(283, f) + rip(284, f) - rip(285, f)))

	# Phase 2, checking three char parameters against hex values #
	output.write("Phase 2: %c %c %c\n" % (rip(306, f), rip(308, f), rip(310, f)))

	# Phase 3, loop until a count is reached #
	output.write("Phase 3: %d\n" % (rip(327, f) - 1))

	# Phase 4, double while loop shenanigans 
	a = rip(337, f)
	b = rip(338, f)
	while(b <= rip(352, f)): #400aa3
		c = rip(340, f) #400a7c
		while(c > rip(349, f)):
			eax = a
			edx = b
			edx += eax
			eax = c
			eax += edx
			a = eax
			c -= 1
		b += 1
	output.write("Phase 4: %d\n" % a)

	# Phase 5, ???
	value = int(rip_no_conv(385, f).split('(')[0].replace('-',''), 16)
	ch = 0x64 - (value - 29)
	output.write("Phase 5: %c\n" % ch)
	output.write("\n")

	if(not is_all):
		print("Done, please view output.txt for your answers")
	#call("rm %s" % str(name), shell=True)

if __name__ == '__main__':
	main()
	output.close()