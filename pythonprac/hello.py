# python 실행 단축 Ctrl + Shift + F10
print('hello sparta!!')

# 가상 환경(virtual environment)이란? - 프로젝트별로 패키지들을 담을 공구함
# 	같은 시스템에서 실행되는 다른 파이썬 응용 프로그램들의 동작에 영향을 주지 않기 위해,
# 	파이썬 배포 패키지들을 설치하거나 업그레이드 하는 것을 가능하게 하는 격리된 싱행 환경


# import requests  # requests 라이브러리 설치 필요
#
# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
#
# gus = rjson['RealtimeCityAir']['row']
#
# for gu in gus:
# 	gu_name = gu['MSRSTE_NM']
# 	gu_mise = gu['IDEX_MVL']
#
# 	if (gu_mise > 100):
# 		print(gu_name, gu_mise)
#
# import requests
# from bs4 import BeautifulSoup


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
	
	# 영화 랭킹 순위값 불러오기
	# old_content > table > tbody > tr:nth-child(2) >
	lank = tr.select_one('td:nth-child(1) > img')
	
	# 영화 이름
	# old_content > table > tbody > tr:nth-child(2) >
	a_tag = tr.select_one('td.title > div > a')
	# print(a_tag)
	
	# 영화 평점
	# old_content > table > tbody > tr:nth-child(2) >
	rate = tr.select_one('td.point')
	
	if a_tag is not None:
		title = a_tag.text
		# print(lank['alt'])
		# print(title)
		# print(rate.text)
		print(lank['alt'], title, rate.text)