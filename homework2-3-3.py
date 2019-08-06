import sys
import io
import urllib. request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1237/1237423/303972a0c4376a49a9f7_20190715155149096.jpg"
htmlURL = "https://ssl.pstatic.net/tveta/libs/1245/1245751/574928e5438423b3c0c9_20190628145213365.jpg"

savePath1 = "C:/test1.jpg"
savePath2 = "c:/test2.jpg"

f = req.urlopen(imgUrl).read()
f2 = req.urlopen(htmlURL).read()

# w : write , r : read , a : add , b : binary
with open(savePath1,'wb') as saveFile1:
    saveFile1.write(f)
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
