import time
WEIGHTS = {
  '1': 0.430,
  '2': 3.0,
  '3': 3.65,
  '4': 9.32
}
def calculate(tolerance, step, **kwargs):
  desired = kwargs.get('desired', 2)
  skip = kwargs.get('skip', 1)

  for i in range(0,step,skip):
    if (i / step * WEIGHTS['1'] >= desired):
      continue

    for j in range(i,step - i,skip):
      if (j / step * WEIGHTS['2'] >= desired):
        continue

      for k in range(j,step - (i+j),skip):
        if (k / step * WEIGHTS['3'] >= desired):
          continue

        for n in range(k,step - (i+j+k),skip):
          if (i+j+k+n != step*0.99):
            continue

          nw = kwargs.get('n', n)
          kw = kwargs.get('k', k)
          jw = kwargs.get('j', j)
          iw = kwargs.get('i', i)

          res = WEIGHTS['1'] * nw/step + \
                WEIGHTS['2'] * kw/step + \
                WEIGHTS['3'] * jw/step + \
                WEIGHTS['4'] * iw/step + \
                16.5 * 0.01

          if round(res, tolerance) == desired:
            print("{} {} {} {}: {}".format(nw / step, kw / step, jw / step, iw / step, res))

if __name__ == "__main__":
  start = time.clock()
  calculate(5, 100, desired = 2)
  runtime = time.clock() - start
  print("runtime: {}s".format(round(runtime, 5)))
