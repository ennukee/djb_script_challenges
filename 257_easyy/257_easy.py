pairs = [x.replace('\n','').split(',') for x in open('input.txt')]
relevant = [( int(x[1].split()[2]), 2014 if len(x[3].split())<2 else int(x[3].split()[2]) ) for x in pairs]
count = dict((el,0) for el in range(1732,2015))
for r in relevant:
	for d in range(r[0], r[1]+1):
		count[d]+=1
print( ' '.join([str(k) for k in count if count[k]==max(count.values())]) )