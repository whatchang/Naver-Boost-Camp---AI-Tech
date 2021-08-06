import requests
import json            #json import하기
import pprint
from bs4 import BeautifulSoup

#custom_header을 통해 아닌 것 처럼 위장하기
custom_header = {
    'referer' : 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
x = '37.5699996948242'
y = '126.9800033569336'
searchWord = "추천맛집"
c = "서울"
g = '중구'
d=""
d2=""

page_num = '1'
padcnt = '0'

url_data = {
    'page' :'1',
    'pdc' : '0',
    "x" : x,
    "y" : y,
    "searchWord" : searchWord,
    "city" : c,
    "gu" : g,
    "dong" : d,
    "addr4" : d2,
    #"x=" + x + "&y=" + y + "&searchWord=" + searchWord + "&page=" + page_num + "&city=" + c + "&gu=" + g + "&dong=" + d + "&addr4=" + d2 + "&pdc=" + padcnt
}

#해당 접속 사이트가 아닌 원본데이터가 오는 url 추적. network에서 가지고 온다.
url = "https://www.isuperpage.co.kr/search.asp"



req = requests.get(url, data=url_data)    #custom_header를 사용하지 않으면 접근 불가

if req.status_code == requests.codes.ok:
    print("접속 성공")
    #req2 = req.get(url, data='poiInfo.tel')

    soup = BeautifulSoup(req.text, "html.parser")
    json_data = req.headers
    print(json_data)
    #a = soup.find_all("span", "phone")
    #print(a)
else:
    print("Error code")




