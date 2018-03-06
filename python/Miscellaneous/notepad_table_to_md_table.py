i = """VPN  Valid Real page
000 1 01
001 1 10
010 0
011 1 00
100 0
101 0
110 1 11
111 0"""

msg = ""
lines = i.split('\n')
l1 = lines[0].split()
rowf = "|{}|{}|{}|\n"
msg += rowf.format(l1[0], l1[1], ' '.join(l1[2:]))
msg += "|---|---|---|\n"
for i in lines[1:]:
  l = i.split()
  msg += rowf.format(*l, "" if len(l)==2 else l[2])

print(msg)
