from BeautifulSoup import BeautifulSoup
import KillData

def parseBurn(url):
    parsed_html = BeautifulSoup(url)
    killlist = []
    for div in parsed_html.findAll('div','col-4'):
        kill = KillData.KillData()
        kill.link = div.find('a')['href']
        killlist.append(kill)

    return killlist

