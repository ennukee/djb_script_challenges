#
# /r/dailyprogrammer Challenge #257 [Easy] 
# In what year were most presidents alive?           
# 										   
# Short Summary: Take in a CSV file (in this case, it is as .txt) containing PRESIDENT,
# BIRTH DATE, BIRTH PLACE, DEATH DATE, LOCATION OF DEATH and parse to output the year
# in which the most presidents (active, former, or to be) were alive	   
# 										   
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/49aatn/20160307_challenge_257_easy_in_what_year_were/
#  										   

pairs = [x.replace('\n','').split(',') for x in open('input.txt')]
relevant = [( int(x[1].split()[2]), 2014 if len(x[3].split())<2 else int(x[3].split()[2]) ) for x in pairs]
count = dict((el,0) for el in range(1732,2015))
for r in relevant:
	for d in range(r[0], r[1]+1):
		count[d]+=1
print( ' '.join([str(k) for k in count if count[k]==max(count.values())]) )