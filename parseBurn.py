from BeautifulSoup import BeautifulSoup

def parseBurn(url):
	parsed_html = BeautifulSoup(open('burnjitalist.html'))
	list = []
	for div in parsed_html.findAll('div','col-4'):
		list.append(div)
	return list[0]
	
