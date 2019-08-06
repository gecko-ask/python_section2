from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</html>
"""
soup = BeautifulSoup(html,'html.parser')
#print('soup',type(soup))
#print('prettify',soup.prettify())

h1 = soup.html.body.h1
#print('h1',h1)
#print('h1',type(h1))
#print(h1.string)

p1 = soup.html.body.p
print('p1',p1)
p2 = p1.next_sibling.next_sibling               #한번만 하면 \n을 읽어온다.. 위에서 엔터를 쳤기 때문
print('p2',p2)
p3 = p1.previous_sibling.previous_sibling
print('p3',p3)

print('h1 >>',h1.string)
print('p1 >>',p1.string)
print('p2 >>',p2.string)
