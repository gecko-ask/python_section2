from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
print('soup',soup.prettify())

#top = soup.select("div.rankingB")
#top = soup.select("ul")
print(top)
