#   
#   Project Euler 
#   Problem #24
#
#   Dylan Bowers
#
#   https://projecteuler.net/problem=24
#   

import math
def p024(n, fm):
    # So this one was a fun one to solve
    #
    # The idea is to narrow down a range based on a factorial range
    # monitoring the used values.
    #
    # If I wanted the third value of the example, I'd do..
    # p024(2, 3)
    # which would do...
    # remaining = [0,1,2]
    # out = []
    # c_range_max = 6
    #
    # It would then iterate...
    #   - c_range_max down to 2. We pick the `1` from the remaining
    #   list because index = 2 // 2 = 1, remaining[1] = 1, n = 2 % 2 = 0
    #   then append it to output, remove 1 from remaining, and repeat
    #   - c_range_max down to 1. We pick the `0` form the remaining
    #   list because index = 0 // 1 = 0. remaining[0] = 0
    #   - Same applies to the next iteration, remaining[0] = 2
    #   thus we get [1, 0, 2] as our answer.
    #
    # Really hard to explain in words well. Just try to understand the flow
    # of the code below. Think of it as subsetting the potential ranges because
    # we know that the answers are in a specific order



    remaining = range(0, fm)
    out = []
    c_range_max = math.factorial(fm)

    # We don't want input like "the 200th lexicographic order of 0, 1, 2"
    assert n < c_range_max, 'the `n`th order must be < `fm`!'

    while fm > 0:
        c_range_max = c_range_max / fm
        fm -= 1
        index = n // c_range_max

        out.append(remaining[index])
        remaining = remaining[0:index] + remaining[index+1:]
        n %= c_range_max

    return out

if __name__ == '__main__':
    # This treats the first as the 0th, so the 1,000,000th is
    # actually the 999,999th in my code
    print(p024(999999, 10))
