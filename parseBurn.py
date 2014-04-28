from BeautifulSoup import BeautifulSoup
import KillData
import urllib
import datetime

def parseBurn(url):
	html = urllib.urlopen(url)

	return parseHTML(html)

def parseHTML(html):
	parsed_html = BeautifulSoup(html)
	killlist = []
	for div in parsed_html.findAll('div','col-4'):
		kill = KillData.KillData()

		kill.link = div.find('a')['href']
		kill.name = div.findAll('a')[-1].renderContents().strip()

		#2014-04-25 13:38:00
		date = div.find('p').renderContents()[:19]
		kill.date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

		#render amount tag and remove "ISK"
		amount = div.find('h3').renderContents()[:-4]
		kill.amount = int(amount.replace(',', ''))

		killlist.append(kill)

	return killlist
