#
#	Project Euler
#	Problem #56
#
#	Dylan Bowers
#
#	https://projecteuler.net/problem=56
#

def digit_sum(n): return sum(int(x) for x in str(n))
def p056(n):
    return max(digit_sum(pow(i, q)) for i in range(100) for q in range(100))

if __name__ == '__main__':
    print(p056(100))
