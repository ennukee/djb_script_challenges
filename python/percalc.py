data = """[b]Puncher[/b]: Rank [b]4[/b] of 198
[b]Priestism[/b]: Rank [b]17[/b] of 298 
[b]Telorrius[/b]: Rank [b]24[/b] of 259
[b]Jwalla[/b]: Rank 27 of 300 
[b]Furmak[/b]: Rank 32 of 313 """

data = data.replace('[b]','')
data = data.replace('[i]','')
data = data.replace('[/b]','')
data = data.replace('[/i]','')

print(data)
for line in data.split('\n'):
  d = line.split()
  print('{}: {}'.format(d[0], 100*(1-float(d[2])/float(d[4]))))