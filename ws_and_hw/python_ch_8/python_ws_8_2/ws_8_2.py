# ws_8_2.py

# 아래 클래스를 수정하시오.

# 추가
# from ws_8_1 import nimal
# 을 하면 from 호출시 ws_8_1을 한번 순회 즉 실행을 먼저 함.

class Animal:
    num_of_animal = 0
    
    def __init__(self):
        Animal.num_of_animal += 1 # 클래스 속성 정의

    @classmethod
    def num_plus(self):
        self.num_of_animal += 1

class Dog(Animal):
    def bark(self): # 호출했을시 생성 함수
        print('멍멍')

    pass

class Cat(Animal):
    pass

class Pet(Dog, Cat): # 다중 상속
   @classmethod # 클래스 메소드에 간섭
   def access_num_of_animal(cls): # 함수 호출
       return cls.num_of_animal
   pass
dog1 = Dog()
dog1.bark()
