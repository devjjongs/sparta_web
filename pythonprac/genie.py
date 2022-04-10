# pymongoDB 사용을 위한 명령
from pymongo import MongoClient

# 로컬에서 돌아가는 mongoDB에 연결
client = MongoClient('localhost', 27017)
# dbsparta 이름을 가진 DB에 접속
db = client.dbsparta

# 웹스크래핑(크롤링 기초)
import requests  # 요청 명령 불러오기
from bs4 import BeautifulSoup  # bs4의 BeautifulSoup 불러오기

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)
#                       기본적인 요청을 막아둔 사이트를 우회하기 위해 브라우저 요청 효과를 주기 위해서 headers=headers 사용

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# 순위 : body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# 제목 : body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수 : body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
	# 순위
	# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
	rank = tr.select_one('td.number').text[0:2].strip()
	# print(rank)
	
	# 제목
	# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
	title = tr.select_one('td.info > a.title.ellipsis').text.strip()
	# print(title)
	
	# 가수
	# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
	artist = tr.select_one('td.info > a.artist.ellipsis').text
	# print(artist)

	print(rank, title, artist)

	# # DB에 크롤링한 지니뮤직 데이터 저장하기
	# doc = {
	# 	'rank': rank,
	# 	'title': title,
	# 	'artist': artist
	# }
	# db.genie.insert_one(doc)
