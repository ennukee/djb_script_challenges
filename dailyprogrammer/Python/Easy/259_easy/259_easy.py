#
# /r/dailyprogrammer Challenge #259 [Easy] 
# Clarence the Slow Typist         
#                        
# Short Summary: Best to view full problem 
#                        
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/
#   

import math
keys = "123456789.0"

def solve(i):
  total = 0.0
  for n in range(0, len(i) - 1):
    p1, p2 = keys.index(i[n]), keys.index(i[n+1])
    op = (int(p1/3)-int(p2/3))**2 + (p1%3 - p2%3)**2
    total += math.sqrt(op)
  return total

# Ugly one-liner logic version
# solve = lambda i: sum(math.sqrt((int(keys.index(i[n])/3)-int(keys.index(i[n+1])/3))**2 + (keys.index(i[n])%3 - keys.index(i[n+1])%3)**2) for n in range(0, len(i)-1))

print("%.2fcm" % solve("219.45.143.143"))