# coding: UTF-8
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

# アクセスするURL
#url = "http://www.nikkei.com/"
url = "http://kinyarwanda.net/index.php?q=cook&start=0"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")
# span = soup.find_all("")
ul = soup.find("ul", {"id": "results"})
# li = soup.find("li", {"class": "entry"})

for tag in ul:
	# li = ul.find("li", {"class": "entry"})
	prefix = ul.find("span", {"class": "prefix"}).text
	lemma = ul.find("span", {"class": "lemma"}).text
	try:
		print(prefix+lemma)
		# print(li)
	except:
		pass