#
# /r/dailyprogrammer Challenge #267 [Easy] 
# All the places your dog didn't win
#                        
# https://www.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/
#   

import re
def easy_267(x, max_range = 100):
  r = [num for num in range(1, max_range + 1) if x != num]
  parse = lambda num: {'1': 'st', '2': 'nd', '3': 'rd'}[str(num)[-1]] if re.findall('^(^1?)[123]$',str(num)) else 'th'
  return ["{}{}".format(x, parse(x)) for x in r]

def easy_267_short(x, max_range = 100):
  return ["{}{}".format(x, {'1': 'st', '2': 'nd', '3': 'rd'}[str(x)[-1]] if re.findall('^(^1?)[123]$',str(x)) else 'th') for x in [num for num in range(1, max_range + 1) if x != num]]