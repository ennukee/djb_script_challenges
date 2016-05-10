#
# /r/dailyprogrammer Challenge #266 [Easy] 
# Basic Graph Statistics: Node Degrees
#                        
# https://www.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/
#   
from collections import defaultdict

inp = """1 2
1 3
2 3
1 4
3 4
1 5
2 5
1 6
2 6
3 6
3 7
5 7
6 7
3 8
4 8
6 8
7 8
2 9
5 9
6 9
2 10
9 10
6 11
7 11
8 11
9 11
10 11
1 12
6 12
7 12
8 12
11 12
6 13
7 13
9 13
10 13
11 13
5 14
8 14
12 14
13 14
1 15
2 15
5 15
9 15
10 15
11 15
12 15
13 15
1 16
2 16
5 16
6 16
11 16
12 16
13 16
14 16
15 16
"""

# - - Main Challenge - - #

# Clean input so it can be used properly

# Some weird syntax error was preventing me from using list comprehensions
# effectively here. Oh well.
input_list = []
for x in inp.split():
  for y in x.strip().split():
    input_list.append(int(y))

# Logic portion of main part
def solve(N, i):
  return dict(zip(range(1, N + 1), [i.count(x) for x in range(1, N + 11)]))

# Printing the result to confirm its correctness
for i,v in sorted(solve(16, input_list).items()):
  print("Node {} has a degree of {}".format(i, v))


# - - Bonus - - #

# Clean input so it can be properly used
clean_input = [[int(y) for y in x.strip().split()] for x in inp.split('\n')]

# Logic portion of main part
def solve_bonus(N, i):
  return [[1 if [row, column] in i or [column, row] in i else 0 for column in range(1, N + 1)] for row in range(1, N + 1)]

# Printing the result to confirm its correctness
for row in solve_bonus(16, clean_input):
  print(row)
