# ws_8_5.py
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    sound = '멍멍'
    def bark(self):
        print(self)

class Cat(Animal):
    sound = '야옹'
    def meow(self):
        print(self)

class Pet(Dog, Cat):

    @classmethod
    def __str__(cls):
        return f'애완동물은{cls.sound} 소리를 냅니다'


ani = Pet()

print(ani)