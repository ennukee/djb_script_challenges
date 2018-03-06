data = [1, 1, 0, 1, 0, 0, 0, 1, 0, 1]
import numpy as np

def AP(rels):
	return np.mean( [sum(rels[:l+1])/(l+1) for l in range(len(rels))] )

print(AP(data))

def precision_at_k(r, k):
    assert k >= 1
    r = np.asarray(r)[:k] != 0
    if r.size != k:
        raise ValueError('Relevance score length < k')
    return np.mean(r)

def average_precision(r):
    r = np.asarray(r) != 0
    out = [precision_at_k(r, k + 1) for k in range(r.size) if r[k]]
    print(r)
    print(out)
    if not out:
        return 0.
    return np.mean(out)

print(average_precision(data))

for i in range(1,11):
	print(precision_at_k(data, i))