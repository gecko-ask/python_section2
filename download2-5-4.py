from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#CSS 선택자 selector .. 가장많이 쓰인다!
html = """
<html><body>
<div id = "main">
    <h1>강의목록</h1>
    <ul class = "lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
#h1 = soup.select("div#main > h1")
#print('h1',h1)
#print('h1',type(h1))
h1 = soup.select_one("div#main > h1")
print('h1',h1.string)

list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>", li.string)
