#
# /r/dailyprogrammer Challenge #265 [Easy] 
# Permutations and combinations part 1                  
#                        
# https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/
#   

# I decided to go raw with this one. No external libraries allowed. 
# Was a fun challenge!

# NOTE: Not yet completed

def chunkify(array, le):
  # due to flatten overly-flattening (as expected), we need to re-chunk the data
  return [array[s:s+le] for s in range(0, len(array), le)]

def flatten(array):
  for element in array:
    if type(element) == type([[]]): # avoid isinstance and collections.Iterable compare
      for subelement in flatten(element):
        yield subelement
    else:
      yield element

def attach(base, i, left, max_length, of):
  # The beef of the combination generation logic
  if len(base) == max_length - 1:
    yield(base + [i])
  else:
    for q in left:
      yield list(attach(base + [i], q, range(q + 1, of), max_length, of))

def combinations(max_length, of):
  result = chunkify(
              list(
                flatten(
                  [
                    list(attach([], num, range(num + 1, of), max_length, of)) for num in range(0, of)
                  ]
                )
              ), max_length
            )
  return result
a = combinations(3, 8)
for i in a:
  print(i)
print(combinations(3, 8)[23 - 1])
print(combinations(4, 9)[111 - 1])

