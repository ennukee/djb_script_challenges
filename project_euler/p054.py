import euler_shared

# INCOMPLETE SOLUTION #

def hand_value(hand):
	card_convert = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
	cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	numerics = [x[0] for x in hand]
	suits = [x[1] for x in hand]

	highest_card_in_hand = 14 if 'A' in hand else card_convert[max(cards.index(i) for i in hand)]

	# Royal Flush check
	if euler_shared.array_equivalent(numerics, ['10', 'J', 'Q', 'K', 'A']) and euler_shared.array_all_same(suits):
		return [10, 13, 13]

	# Straight Flush
	lowest = min(cards.index(x) for x in numerics)
	if all(cards[lowest+q] in numerics for q in range(0, 5)) and euler_shared.array_all_same(suits):
		return [9, ]

def is_win(p1, p2):
	# Form: [hand_type, highest_card_in_type, high_card_in_hand]
	return hand_value(p1) > hand_value(p2)

def p054(pairs):
	return sum(1 if is_win(*pair) else 0 for pair in pairs)

if __name__ == '__main__':
	with open('p054_poker.txt').readlines() as f:
		data = [x.strip().split() for x in f]
		data = [[x[:5], x[5:]] for x in data]
		print(p054(data))
