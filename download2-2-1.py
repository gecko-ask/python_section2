import sys
import io
import urllib. request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140413_184%2Fmoisophiaj_1397389104586LN5Bi_JPEG%2F%25B1%25CD%25BF%25A9%25BF%25EE_%25B5%25BF%25B9%25B0_%25BB%25E7%25C1%25F8_%252810%2529.jpg&type=b400"
htmlURL = "http://google.com"

savePath1 = "C:/test1.jpg"
savePath2 = "c:/index.html"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(htmlURL, savePath2)


print("다운로드 완료!")
