import cgi, cgitb

def main(inp):
	return {'a': 1, 'b': 2, 'c': 3}

if __name__ == '__main__':
	data = cgi.FieldStorage()
	return main(data)