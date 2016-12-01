#
#	Project Euler
#	Problem #55
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=55
#

import euler_shared
def lychrel_iter(n, cur_iter):
    if cur_iter == 50: return True
    else:
        n += int(str(n)[::-1])
        if euler_shared.is_palindrome(n):
            return False
        else: return lychrel_iter(n, cur_iter + 1)

def p055(n):
    return sum(1 if lychrel_iter(i, 0) else 0 for i in range(0, n))

if __name__ == '__main__':
    print(p055(10000))
