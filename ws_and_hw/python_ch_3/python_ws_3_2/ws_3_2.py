number_of_people = [0]

def increase_user():
    number_of_people[0] += 1
    print('현재 가입된 유저 수 :', number_of_people[0])
    pass

def create_user(name, age, address):
    print('현재 가입된 유저 수 :', number_of_people[0])
    print(f'{name}님 환영합니다!')
    uesr_info = {'name' : name, 'age' : age, 'address' : address}
    print(uesr_info)
    increase_user()
    pass

create_user('홍길동', '30', '서울')