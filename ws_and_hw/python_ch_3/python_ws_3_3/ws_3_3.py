# ws_3_3.py

def rental_book(name, number):
    from book import number_of_book, decrease_book
    decrease_book(number)
    print(f"{name}님이 {number}권의 책을 대여하였습니다.")
    pass

rental_book('홍길동', 3)


#북 모듈 밖에다 둬보기