from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.naver.com/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

# 네이버 실시간 검색순위 받아오기
#top10 = soup.select("div.PM_CL_realtimeKeyword_list_base>ul.ah_l>li>a.ah_a>.ah_k")
top20 = soup.select("div.PM_CL_realtimeKeyword_list_base>ul.ah_l>li")
#print(top10[1])

for i,e in enumerate(top20,1):
    print(i,e.select_one("span.ah_k").string,"\t URL >>",e.select_one("a").attrs["href"])
