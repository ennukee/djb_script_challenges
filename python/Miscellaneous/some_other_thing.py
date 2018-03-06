import numpy as np
import itertools, math, time

def calculate(n, ex):
  nums = [x/262.0 for x in range(1, n)]
  perms = itertools.permutations(nums, ex)
  probability = 0.0
  base_value = 6.656E-113 # Python cannot calculate 262!/262^262

  for perm in perms:
    p = base_value
    for i in perm:
      p *= i
    probability += p 
  return probability

if __name__ == '__main__':
  for n in range(1, 50):
    start = time.time()
    calc = calculate(262, n)
    print("{}: {} (runtime: {})".format(n, calc, time.time() - start))
    if calc >= 0.99:
      print("DONE")
      break