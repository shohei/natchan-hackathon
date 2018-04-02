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
# soup.find("ul", {"id": "results"})
li = soup.find("li", {"class": "entry"})

for tag in li:
	try:
		print(tag)
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        # string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        # if string_ in "mkc-stock_prices":
        #     # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
        #     nikkei_heikin = tag.string
        #     # 摘出が完了したのでfor分を抜けます
            # break
    except:
    	# パス→何も処理を行わない
    	pass


