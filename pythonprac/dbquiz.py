# pymongoDB 사용을 위한 명령
from pymongo import MongoClient

# 로컬에서 돌아가는 mongoDB에 연결
client = MongoClient('localhost', 27017)
# dbsparta 이름을 가진 DB에 접속
db = client.dbsparta

# (1) 영화제목 '매트릭스'의 평점을 가져오기
movie = db.movies.find_one({'title': '매트릭스'})
print(movie['star'], "점")

# (2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
target_star = movie['star']
same_star_movies = list(db.movies.find({'star': target_star}, {'_id': False}))

for same_star in same_star_movies:
	print(same_star['title'])

# (3) 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})
