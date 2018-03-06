import sys

def progress(s, l):
    new_l = []
    for i in l:
        if i[1] + 1 >= len(s):
            new_l.append((i[0], i[1] + 1))
        else:
            ns = i[0] + s[i[1] + 1]
            new_l.append((ns, i[1] + 1))

    just_strings = [i[0] for i in new_l]
    if all(just_strings.count(x) < 2 for x in just_strings):
        return new_l[0][0][:-1]
    else:
        new_l = [x for x in new_l if just_strings.count(x[0]) >= 2]
        return progress(s, new_l)
    print('---')

# This function runs in O(n) time
def get_indices_hash(s):
	base = {}
	for ci in range(len(s)):
		if s[ci] in base.keys():
			base[s[ci]].append(ci)
		else:
			base[s[ci]] = [ci]
	return base

def main(s):
    max_substring = ""
    indices_hash = get_indices_hash(s) # O(n)

    for c in list(set(s)): # O(n) loop
        indices =  indices_hash[c] # O(1) action
        result_for_c = progress(s, zip([c] * len(indices), indices)) # zip() is O(n) action, recursion is O(...) action
        if len(result_for_c) > len(max_substring):
            max_substring = result_for_c # O(1) action
    return max_substring

if __name__ == '__main__':
    for l in sys.stdin:
        print(l)
        main(l)
