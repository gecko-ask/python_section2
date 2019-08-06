from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("")
url = base + quote

res = req.urlopen(url)
savePath = "C:\\Workspace\\imageDown\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
        #os.makedirs(savePath)
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res,"html.parser")
#css 선택자 입력!
img_list = soup.select("#main > section:nth-child(5) > div > div.slider_container > div > div:nth-child(5) > div > a > div.card-image > figure > img")
print("test",img_list)

#for i, e in enumerate(img_list,1):
    #test = e.select_one("div.card.course")
    #print(i,"test",test)
#    with open(savePath)

    #안되네
    #print(img_list[data-source])
    #파일 이름 만들기
    #fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg' )
    #print(fullFileName)
    #req.urlretrieve(img_list['data-source'],fullFileName)

#print("파일 ", i ,"개 생성\n다운로드 완료!")
