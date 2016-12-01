#
#	Project Euler
#	Problem #57
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=57
#

# A quick explanation on the math:
# - The denominator for the next iteration is equal to
#    the current denominator (cd) + current numerator (cn)
# - The numerator for the next iteration is equal to
#    (cd * 2) + cn
def p057(n):
    # Because of recursion limits, this cannot be done recursively in Python
    cn, cd, c = 3, 2, 0

    while n > 0:
        if len(str(cn)) > len(str(cd)): c += 1
        cn, cd, n = cn + (cd * 2), cn + cd, n - 1
    return c

if __name__ == '__main__':
    print(p057(999))
