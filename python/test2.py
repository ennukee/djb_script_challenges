# Python script for CS240 Question 2.3
# Dylan Bowers (28838875)
from math import factorial as f
def choose(i, q):
  return f(i)/(f(q) * f(i-q))

prob_after_i = lambda i: sum(choose(300, x) * (0.01 ** x) * (0.99 ** (300-x)) for x in range(i,301))

for i in range(0,20):
  out = "k = {0}, uptime = {1}%"
  print(out.format(i, (1 - prob_after_i(i))*100))