# python 실행 단축 Ctrl + Shift + F10
print('hello sparta!!')

# 가상 환경(virtual environment)이란? - 프로젝트별로 패키지들을 담을 공구함
# 	같은 시스템에서 실행되는 다른 파이썬 응용 프로그램들의 동작에 영향을 주지 않기 위해,
# 	파이썬 배포 패키지들을 설치하거나 업그레이드 하는 것을 가능하게 하는 격리된 싱행 환경

import requests  # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
	gu_name = gu['MSRSTE_NM']
	gu_mise = gu['IDEX_MVL']
	
	if (gu_mise > 100):
		print(gu_name, gu_mise)

# print(rjson['RealtimeCityAir']['row'][0]['NO2'])
