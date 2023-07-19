number_of_people = [0]


def increase_user(human):
    print(f"{human}님 환영합니다!")
    number_of_people[0] += 1
    pass

def create_user(name, age, address):
    increase_user(name)
    user_info = {'name' : name, 'age' : age, 'address' : address}
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


print(list(map(create_user, name, age, address)))


#글로벌 명령어 사용하기
