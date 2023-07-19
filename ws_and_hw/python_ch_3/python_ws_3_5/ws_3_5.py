# 실습 번호.py
from book import number_of_book, decrease_book
number_of_people = 0


def increase_user(name):
    global number_of_people
    print(f"{name}님 환영합니다!")
    number_of_people += 1
    return number_of_people


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user(name)
    user_info = {'name' : name, 'age' : age, 'address' : address}
    return user_info

many_user = list(map(create_user, name, age, address))

info = list(map(lambda x: {'name' : x['name'], 'book_mi' : x['age']//10}, many_user)) #info 인자에 사용될 딕셔너리

def rental_book(info):
    decrease_book(info['book_mi'])
    print(f"{info['name']}님이 {info['book_mi']}권의 책을 대여하였습니다.") 

rental_book_print = lambda info: list(map(rental_book, info))

rental_book_print(info)