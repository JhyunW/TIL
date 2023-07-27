# ws_8_5.py

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

    

class Cat:
   def meow(self):
       print('야옹!')

    

class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(self.sound)

    @classmethod
    def access_num_of_animal(cls):
        return cls.num_of_animal
    
    @classmethod
    def __str__(self):
        return self.sound
    
pet1 = Pet('그르르')
print(pet1)