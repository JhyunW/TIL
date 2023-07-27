# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    
    def __init__(self):
        Animal.num_of_animal += 1 # 클래스 속성 정의

    # @classmethod
    # def num_plus(self):
    #     self.num_of_animal += 1

class Dog(Animal):

    pass

class Cat(Animal):
    pass

class Pet(Dog, Cat): # 다중 상속
   @classmethod # 클래스 메소드에 간섭
   def access_num_of_animal(cls): # 함수 호출
       return cls.num_of_animal
   pass

dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())