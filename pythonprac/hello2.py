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
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)
#                       기본적인 요청을 막아둔 사이트를 우회하기 위해 브라우저 요청 효과를 주기 위해서 headers=headers 사용

soup = BeautifulSoup(data.text, 'html.parser')
# BeautifulSoup의 사용 방법 2가지
#   select_one : 한 개의 데이터 값을 불러오는 것
#   select : 여러개의 데이터를 List 형식으로 불러오는 것

# 코딩 시작
# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title)  # 태그 호출
# print(title.text)  # 태그 사이의 텍스트만 불러오고 싶을 경우 .text를 사용하여 원하는 텍스트 호출
# print(title['href'])  # 태그의 속성을 가져오고 싶을 경우 ['~~']의 ~~에 태그 속성 입력


# 페이지 크롤링 해보기
# old_content > table > tbody > tr
# 공통 selecter 선언
trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
	# print(tr)
	
	# 영화 이름
	# old_content > table > tbody > tr:nth-child(2) >
	a_tag = tr.select_one('td.title > div > a')
	# print(a_tag)
	
	if a_tag is not None:
		title = a_tag.text
		# print(rank['alt'])
		# print(title)
		# print(rate.text)
		# print(lank['alt'], title, rate.text)
		
		# 영화 랭킹 순위값 불러오기
		# old_content > table > tbody > tr:nth-child(2) >
		rank = tr.select_one('td:nth-child(1) > img')['alt']
		
		# 영화 평점
		# old_content > table > tbody > tr:nth-child(2) >
		rate = tr.select_one('td.point').text
		
		# DB에 크롤링한 영화 data 저장하기
		doc = {
			'rank': rank,
			'title': title,
			'star': rate
		}
		db.movies.insert_one(doc)
