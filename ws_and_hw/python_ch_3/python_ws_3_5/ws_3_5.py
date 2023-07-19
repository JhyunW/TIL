# 실습 번호.py
number_of_people = [0]


def increase_user(name):
    print(f"{name}님 환영합니다!")
    number_of_people[0] += 1
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user(name)
    user_info = {'name' : name, 'age' : age, 'address' : address}
    return user_info


many_user = list(map(create_user, name, age, address))
info = list(map(lambda x: {'name' : x['name'], 'book_mi' : x['age']//10}, many_user))

add = lambda x,y: x+y

def rental_book(*info):
    print(f"{info}님이 {info}권의 책을 대여하였습니다.")
    pass
rental_book(maplist((lambda y: {y['name'], y['book_mi']}, info)))