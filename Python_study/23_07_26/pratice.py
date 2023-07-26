# 함수는 def 뒤에 함수 이름
# 클래스는 class 뒤에 클래스 이름
# 단, 클래스 name의 컨벤션은 pascalCase를 사용
# 컨벤션은 상호간의 약속이다. 어디서 어떤 라이브러리를 사용하든, PascalCase로 작성된
# 값들은 모두 클래스라는 사실을 내가 별도로 내부 코드를 확인하지 않아도 알 수 있다.
# 의문? list, str, int 얘네는 PascalCase 아닌데요? -> 예외
# Library 클래스에서는
        # 책의 관리 | 책의 정보 : 제목, 작성자, 보유 권수 인스턴스 생성
        # 총 보유 책 권수
        # 대여 시스템 메서드

# User 클래스에서는
        # 유저 정보 관리 | 유저 정보 : 이름, 나이
class Library:
    # 클래스 변수
    # 책이 생성 될 때 마다 1씩 증가
    number_of_book = 0
    # 생성자 : 클래스에 의해 인스턴스가 생성되는 순간, 실행되는 매직 메서드.
    # double underscore 로 작성되는 매서드들은 모두 매직 메서드
    # 파이썬이 내부적으로 특정한 동작을 하도록 만들어놓은 메서드들

    # self의 역할 : 호출 대상 인스턴스 자체를 의미. ex)numbers.append(3) 일때 numbers 라는 함수
    def __init__(self, title, author, volumes):
        self.title = title
        self.author = author
    # 책 정보에 책마다의 보유 권수를 따로 저장하고싶다
    # 일반적으로, 동일한 책은 1권씩 추가가 되고,
    # 특별한 경우에만 여러권 추가된다면?
        self.volumes = volumes
        # 클래스 변수 호출 하여 값 증가
        # 아래 방식은 생성자에서만 허용하는 느낌
        # 되도록이면 클래스 메서드를 호출하는것을 권장

        Library.increase_book(volumes) # 카운트 할때 함수 내가 아닌 라이브러리 에서 올라가는거 확인하기

    #데코레이터 classmethod를 함수 위에 작성시
    # 해당 함수는 첫번째 인자를 호출 주체의 class를 받게된다
    # 인스턴스가 호출시에도 첫번째 인자는 호출한 인스턴스의
        # 클래스를 인자로 넘겨주게된다.
        # 그래서, 인스터스는 클래스 메서드도 호출시
        # 정상적으로 작동하기는 하지만, 그렇게 쓰지는 말자.
    
    # @classmethod 데코레이터 아래에 정의된 메서드는
    # 첫번째 인자로, 호출한 대상의 소속 class를 첫번째 인자로 넘기도록 바꿈
    @classmethod
    def increase_book(cls, volumes):
        cls.number_of_book += volumes
        
    def __str__(self):
        return self.title
    
    # 소멸자
    # def __del__(self):
    #     print(f'{self.title}책을 제거하였습니다!')
    #     return None

    # rental_system 메서드
    # 1. 인자는 유저와 책 인스턴스를 받는다
    # 2. 대여하고자 하는 책 수도 함께 받는다
    @classmethod
    def rental_system(cls, user, book, volumes=1):
        # 3. 대여하고자 하는 책 수만큼 라이브러의 총 잭 감소
        cls.number_of_book -= volumes
        # 4. 대여되는 책의 보유 수량 감소
        # book.volumes -= volumes 도 가능하지만
        book_volumes = book.decrease_volumes(volumes)
        # 5. 유저 이름과 책이름, 대여 권수 출력
        print(f"{user.name}님이 {book.title}책을 {volumes}")
        print(f"{user.title}은 {book_volumes}권 만큼 남았습니다.")

    def decrease_volumes(self, volumes):
        if self.volumes - volumes < 0:
            return False
        else:
            self.volumes -= volumes
            return self.volumes

# Library 클래스에 의해 만들어지는 book1 인스턴스는
# 자신만의 고유한 title과 author 정보를 가질 수 있다.


book1 = Library('홍길동전', '허균', 2)   # 돌아가는 동작 Library라는 클래스 안에 입력 -> 클래스 안의 함수 __init__에 자동 호출됨 title과 author에 할당 -> __str__로 실행되서 결과 나옴
print(book1)
print(book1.title, book1.author, book1.volumes)
book2 = Library('먼나라이웃나라', '모름', 7)
print(book2)
print(book2.title, book2.author, book2.volumes)

# rental_system 메서드
    # 1. 인자는 유저와 책 인스턴스를 받는다
    # 2. 대여하고자 하는 책 수도 함께 받는다
    # 3. 대여하고자 하는 책 수만큼 라이브러리의 총 책수 감소
    # 4. 대여되는 책의 보유 수량 감소
    # 5. 유저 이름과 책이름, 대여 권수 출력


class User:
    NUMBER_OF_PEOPLE = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.increase_user()

    @classmethod
    def increase_user(cls):
        cls.NUMBER_OF_PEOPLE += 1
n = 4
name = ['가', '나', '다', '부']
age = [10, 20, 30, 9]

person1 = User('묵',55)

user_list = []
for index in range(n):
    person = list([name[index],age[index]])
    user_list.append(person)
print(user_list)

Library.rental_system(person1, book1)