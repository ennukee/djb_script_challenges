with open('caustic_thing_1.tsv') as f:
	l = [ll.strip('\n').split('\t') for ll in f.readlines() if ll]
	raid_prio_col = [ll[11] for ll in l]
	
	prios = {
		'Mythic Elisande & Gul\'dan (mount)': 0,
		"Mythic ToS": 0,
		"Heroic ToS": 0,
	}

	for line in raid_prio_col:
		s = line.split('>')
		if len(s) != 3:
			print('bad line')
			continue
		prios[s[0].strip()] += 3
		prios[s[1].strip()] += 2
		prios[s[2].strip()] += 1

	print(prios)