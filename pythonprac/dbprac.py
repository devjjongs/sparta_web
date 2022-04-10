# # mongoDB 연결 상태 확인 :  localhost:27017
#
# # pymongoDB 사용을 위한 명령
# from pymongo import MongoClient
#
# # 로컬에서 돌아가는 mongoDB에 연결
# client = MongoClient('localhost', 27017)
# # dbsparta 이름을 가진 DB에 접속
# db = client.dbsparta
#
# # insert / find / update / delete
#
# # 코딩 시작
#
# # insert
# # doc = {'name': 'bobby', 'age': 21}
# # doc = {'name': 'john', 'age': 27}
# # doc = {'name': 'smith', 'age': 30}
# # doc = {'name': 'jane', 'age': 21}
# # db.users.insert_one(doc)
#
#
# # find
# # same_ages = list(db.users.find({'age': 21}, {'_id': False}))
# # 나이가 21세인 사람을 불러오기
# # {'_id': False} : _id는 표시하지 않음
# # print(same_ages)
#
# # find all
# # DB에 저장된 데이터를 조건 없이 여러개 출력할때는
# # db.users.find({}, {'_id': False}) 형식으로 명령
#
# # for문을 이용하여 리스트 형식으로 출력
# # for person in same_ages:
# # 	print(person)
#
# # find_one
# # user = db.users.find_one({'name': 'bobby'}, {'_id': False})
# # print(user)
#
#
# # update
# # update_one
# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
#
# # update_many : 잘 쓰지 않음
#
#
# # delete
# # delete_one
# db.users.delete_one({'name': 'bobby'})
#
# # delete_many : 잘 쓰지 않음

# pymongoDB 코드 요약
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})