# ws_8_3.py

# 아래 클래스를 수정하시오.
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

class Cat:
   def meow(self):
      print('야옹!')
   pass

cat1 = Cat()
cat1.meow()