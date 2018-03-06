import math
def log(i):
  return math.log(i, 10)

def solve1(v1, M1, v2, M2, f):
  m1 = v1/1000 * M1
  m2 = v2/1000 * M2 * f
  print(m1)
  print(m2)
  if m2 > m1:
    mf = m2 - m1
    Mf = mf/((v1 + v2)/1000)
    r = -log(Mf)
    print('pH: {}\n pOH: {}'.format(14 - r, r))
  if m1 > m2:
    mf = m1 - m2
    ka = eval(input('Required pKa for acid: '))
    r = -log(ka) + log(m2/mf)
    print('pH: {}\n pOH: {}'.format(r, 14 - r))

def solve2(v1, M1, v2, M2, f):
  m1 = v1/1000 * M1
  m2 = v2/1000 * M2 * f
  print(m1)
  print(m2)
  if m2 > m1:
    mf = m2 - m1
    Mf = mf/((v1 + v2)/1000)
    r = -log(Mf)
    print('pH: {}\n pOH: {}'.format(r, 14 - r))
  if m1 > m2:
    mf = m1 - m2
    kb = eval(input('Required pKb for base: '))
    r = (-log(kb) + log(m2/mf))
    print('pH: {}\n pOH: {}'.format(14-r, r))

r = solve2(25.1, 0.366, 14.7, 0.224, 1)
print(r)
