#
# /r/dailyprogrammer Challenge #259 [Easy] 
# Clarence the Slow Typist         
#                        
# Short Summary: Best to view full problem 
#                        
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/
#   

import os, time
from itertools import permutations

# - - FILE PARSER METHOD - - #
def parse(inp):
  r = []
  with open("./grids/{}.grid".format(inp)) as f:
    lines = f.readlines()
    for l in lines:
      r.append([int(x) for x in l.strip().split()])
  return r

# - - MAIN LOGIC METHOD - - #
def solve(grid):
  M = len(grid) * (len(grid) ** 2 + 1) / 2
  for perm in permutations(grid):
    if all(sum([perm[i][abs(x-i)] for i in range(0, len(perm))]) == M for x in [0,len(grid)-1]):
      return [grid.index(perm[i]) for i in range(0,len(grid))]

# - - VERSION OF MAIN THAT RUNS BONUS - - #
def solve_bonus(grid):
  c = 0
  M = len(grid) * (len(grid) ** 2 + 1) / 2
  for perm in permutations(grid):
    if all(sum([perm[i][abs(x-i)] for i in range(0, len(perm))]) == M for x in [0,len(grid)-1]):
      c += 1
  return c

if __name__ == "__main__":
  for name in os.listdir('./grids'):
    start = time.time()
    result = solve_bonus(parse(name[:-5]))
    print("{} result: {} (runtime {}s)".format(name[:-5], result, round(time.time() - start, 3)))