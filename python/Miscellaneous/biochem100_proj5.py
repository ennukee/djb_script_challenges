import sys, random
def main(l):
	valid_chars = 'ATCG'
	correct = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	given = ''.join([random.choice(valid_chars) for x in range(l)])
	correct_answer = ''.join([correct[i] for i in given])

	print('\nHere is your strand... {}'.format(given))

	answer = input('What is the corresponding 3\'-5\'? ')
	if len(answer) != l:
		print("That's not the correct length, wrong!")
		return

	num_correct = sum(1 if correct_answer[i] == answer[i] else 0 for i in range(l))
	perc_corr = ((num_correct / l)*10000)//100
	print('You got {}% correct!\nYours: {}\nCorrect: {}'.format(perc_corr, answer, correct_answer))



if __name__ == '__main__':
	print('-- Welcome to BIOCHEM100 Project 5 by Dylan Bowers --')
	print('You will be given a DNA 5\'-3\' and are required to provide the corresponding 3\'-5\'\n')
	
	while True:
		try:
			inp = input('Please specify the length of the DNA strand to guess: ')
			i = int(inp)
			assert i > 0
			main(i)
			break
		except Exception as e:
			print('That is not a positive number!\n\n')